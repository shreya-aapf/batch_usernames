import streamlit as st
import pandas as pd
import io
from pathlib import Path
import re
import zipfile
import base64


def excel_col_letter_to_index(letter: str) -> int:
    """
    Convert Excel column letter(s) to zero-based index.
    e.g., 'A' -> 0, 'B' -> 1, ..., 'Z' -> 25, 'AA' -> 26, etc.
    """
    letter = letter.strip().upper()
    if not re.fullmatch(r"[A-Z]+", letter):
        raise ValueError(f"Invalid Excel column letter: {letter}")
    idx = 0
    for ch in letter:
        idx = idx * 26 + (ord(ch) - ord('A') + 1)
    return idx - 1  # zero-based


def resolve_column(series_df: pd.DataFrame, column_arg: str) -> pd.Series:
    """
    Accepts a column spec as:
      - Header name (exact match),
      - Excel letter(s) like 'A', 'B', 'AA',
      - Zero-based numeric index like '0', '1', ...
    Returns the selected Series.
    """
    # Exact header name
    if column_arg in series_df.columns:
        return series_df[column_arg]

    # Try Excel letters
    try:
        col_idx = excel_col_letter_to_index(column_arg)
        return series_df.iloc[:, col_idx]
    except Exception:
        pass

    # Try numeric index
    if column_arg.isdigit():
        col_idx = int(column_arg)
        return series_df.iloc[:, col_idx]

    # If nothing worked: helpful error
    cols = list(map(str, series_df.columns))
    raise ValueError(
        f"Could not resolve column '{column_arg}'. "
        f"Available headers: {cols}. "
        f"You can also pass a column letter like 'A' or a zero-based index like '0'."
    )


def chunk_list(items, chunk_size=50):
    """Split list into chunks of specified size."""
    for i in range(0, len(items), chunk_size):
        yield items[i:i + chunk_size]


def create_download_link(content, filename, link_text):
    """Create a download link for text content."""
    b64 = base64.b64encode(content.encode()).decode()
    href = f'<a href="data:file/txt;base64,{b64}" download="{filename}">{link_text}</a>'
    return href


def main():
    st.set_page_config(
        page_title="Batch Username Processor",
        page_icon="📊",
        layout="wide"
    )

    st.title("📊 Batch Username Processor")
    st.markdown("Upload an Excel file and create batched text output with an easy-to-use interface!")

    # Sidebar for file upload and settings
    with st.sidebar:
        st.header("⚙️ Settings")
        
        # File upload
        uploaded_file = st.file_uploader(
            "Choose an Excel file",
            type=['xlsx', 'xls'],
            help="Upload your Excel file containing usernames or names"
        )
        
        if uploaded_file is not None:
            # Read the Excel file
            try:
                # Get sheet names
                excel_file = pd.ExcelFile(uploaded_file)
                sheet_names = excel_file.sheet_names
                
                # Sheet selection
                sheet_name = st.selectbox(
                    "Select Sheet",
                    sheet_names,
                    help="Choose which sheet to read from"
                )
                
                # Read the selected sheet
                df = pd.read_excel(uploaded_file, sheet_name=sheet_name, engine='openpyxl')
                
                st.success(f"✅ File loaded! {len(df)} rows found.")
                
                # Column selection
                st.subheader("Column Selection")
                columns = list(df.columns)
                
                # Show preview of first few rows
                st.write("**Preview of data:**")
                st.dataframe(df.head(3))
                
                # Column input methods
                column_method = st.radio(
                    "How do you want to specify the column?",
                    ["By Header Name", "By Excel Letter (A, B, C...)", "By Index (0, 1, 2...)"],
                    help="Choose how you want to identify the column containing your data"
                )
                
                if column_method == "By Header Name":
                    selected_column = st.selectbox("Select Column", columns)
                elif column_method == "By Excel Letter (A, B, C...)":
                    selected_column = st.text_input(
                        "Enter Excel Letter", 
                        value="A",
                        help="Enter column letter like A, B, C, AA, AB, etc."
                    ).strip().upper()
                else:  # By Index
                    max_index = len(columns) - 1
                    selected_column = str(st.number_input(
                        "Enter Column Index", 
                        min_value=0, 
                        max_value=max_index,
                        value=0,
                        help=f"Enter column index (0 to {max_index})"
                    ))
                
                # Batch size
                batch_size = st.number_input(
                    "Batch Size",
                    min_value=1,
                    max_value=1000,
                    value=50,
                    help="Number of names per batch"
                )
                
                # Output filename
                output_filename = st.text_input(
                    "Output Filename",
                    value="batch_output",
                    help="Name for the output file (without extension)"
                )
            
            except Exception as e:
                st.error(f"Error loading Excel file: {str(e)}")
                st.info("Please check your file and try again.")
                return

    # Main content area
    if uploaded_file is not None:
        try:
            # Process the column
            series = resolve_column(df, selected_column)
            
            # Convert to list, preserving blanks and order
            values = series.astype(object).where(pd.notna(series), "").tolist()
            
            # Create batches
            batches = list(chunk_list(values, chunk_size=batch_size))
            
            col1, col2 = st.columns([2, 1])
            
            with col2:
                st.subheader("📈 Statistics")
                st.metric("Total Names", len(values))
                st.metric("Total Batches", len(batches))
                st.metric("Batch Size", batch_size)
                
                # Create full output for download
                full_output = ""
                for batch in batches:
                    full_output += ", ".join(map(str, batch)) + "\n\n"
                
                # Download button
                st.download_button(
                    label="📥 Download Full Output",
                    data=full_output,
                    file_name=f"{output_filename}.txt",
                    mime="text/plain",
                    help="Download all batches as a text file"
                )
            
            with col1:
                st.subheader("📋 Batch Viewer")
                
                if len(batches) > 0:
                    # Initialize session state for batch navigation
                    if 'current_batch' not in st.session_state:
                        st.session_state.current_batch = 0
                    
                    # Navigation controls
                    nav_col1, nav_col2, nav_col3, nav_col4, nav_col5 = st.columns([1, 1, 2, 1, 1])
                    
                    with nav_col1:
                        if st.button("⏮️ First", disabled=(st.session_state.current_batch == 0)):
                            st.session_state.current_batch = 0
                    
                    with nav_col2:
                        if st.button("◀️ Previous", disabled=(st.session_state.current_batch == 0)):
                            st.session_state.current_batch -= 1
                    
                    with nav_col3:
                        st.write(f"**Batch {st.session_state.current_batch + 1} of {len(batches)}**")
                    
                    with nav_col4:
                        if st.button("Next ▶️", disabled=(st.session_state.current_batch >= len(batches) - 1)):
                            st.session_state.current_batch += 1
                    
                    with nav_col5:
                        if st.button("Last ⏭️", disabled=(st.session_state.current_batch >= len(batches) - 1)):
                            st.session_state.current_batch = len(batches) - 1
                    
                    # Display current batch
                    current_batch = batches[st.session_state.current_batch]
                    batch_text = ", ".join(map(str, current_batch))
                    
                    # Create a text area that's easy to copy from
                    st.text_area(
                        f"Batch {st.session_state.current_batch + 1} ({len(current_batch)} names)",
                        value=batch_text,
                        height=150,
                        help="Click in the text area and press Ctrl+A to select all, then Ctrl+C to copy"
                    )
                    
                    # Alternative: Show as a code block (also easy to copy)
                    st.code(batch_text, language=None)
                    
                    # Quick copy buttons for different formats
                    st.subheader("🔄 Quick Copy Options")
                    
                    copy_col1, copy_col2 = st.columns(2)
                    
                    with copy_col1:
                        # Comma-separated (default)
                        st.text_area(
                            "Comma-separated:",
                            value=batch_text,
                            height=60,
                            key=f"comma_{st.session_state.current_batch}"
                        )
                    
                    with copy_col2:
                        # Line-separated
                        line_separated = "\n".join(map(str, current_batch))
                        st.text_area(
                            "Line-separated:",
                            value=line_separated,
                            height=60,
                            key=f"lines_{st.session_state.current_batch}"
                        )
                    
                    # Batch selector (alternative navigation)
                    st.subheader("🎯 Jump to Batch")
                    selected_batch = st.selectbox(
                        "Select batch number:",
                        range(1, len(batches) + 1),
                        index=st.session_state.current_batch,
                        format_func=lambda x: f"Batch {x} ({len(batches[x-1])} names)"
                    )
                    
                    if selected_batch - 1 != st.session_state.current_batch:
                        st.session_state.current_batch = selected_batch - 1
                        st.rerun()
                
                else:
                    st.warning("No data found in the selected column.")
        
        except Exception as e:
            st.error(f"Error processing the file: {str(e)}")
            st.info("Please check your column selection and try again.")
    
    else:
        # Welcome message when no file is uploaded
        st.markdown("""
        ## Welcome! 👋
        
        This tool helps you process Excel files containing names or usernames and creates batched output that's easy to copy and use.
        
        ### How to use:
        1. **Upload** your Excel file using the sidebar
        2. **Select** the sheet and column containing your data
        3. **Set** your preferred batch size
        4. **Navigate** through batches using the controls
        5. **Copy** the text directly from the interface
        6. **Download** the complete output as a text file
        
        ### Features:
        - 📂 Support for multiple Excel sheets
        - 🎯 Flexible column selection (by name, letter, or index)
        - ⚙️ Configurable batch sizes
        - 🧭 Easy batch navigation
        - 📋 Multiple copy formats
        - 💾 Download complete output
        - 🔄 Preserves original order and blank entries
        
        **Get started by uploading an Excel file!**
        """)


if __name__ == "__main__":
    main()
