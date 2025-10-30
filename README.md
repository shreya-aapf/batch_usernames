# Batch Username Processor

A Python utility that reads names/usernames from Excel files and outputs them in comma-separated batches. Available as both a **user-friendly web interface** and a command-line tool.

## 🚀 Quick Start - Get Running in 2 Minutes!

**Just downloaded? Here's how to get started:**

### Super Easy Way (Recommended)

#### Windows Users
1. **Double-click `START_HERE.bat`** - That's it! 
2. Upload your Excel file when the browser opens

#### macOS/Linux Users  
1. **Double-click `START_HERE.sh`** - That's it!
2. Upload your Excel file when the browser opens

### Manual Way (If above doesn't work)

#### Windows Users
1. **Double-click** `setup.bat` to install dependencies
2. **Double-click** `run.bat` to start the web interface
3. Open your browser to the URL shown (usually http://localhost:8501)

#### macOS/Linux Users
1. **Right-click** on `setup.sh` → "Open with Terminal" (or open terminal and run `./setup.sh`)
2. **Right-click** on `run.sh` → "Open with Terminal" (or run `./run.sh`)
3. Open your browser to the URL shown (usually http://localhost:8501)

### Command Line Alternative

If the scripts don't work, you can run these commands:

```bash
# Install dependencies
pip install -r requirements.txt

# Start web interface  
streamlit run app.py

# Or use command line tool
python batch_names_to_text.py --help
```

## 🛠️ What You Need

- **Python 3.7+** (Download from https://python.org)
- **Excel file** with your data

## 🚨 Troubleshooting

- **Python not found**: Install Python and make sure it's added to your PATH
- **Permission denied**: Try running as administrator (Windows) or with `sudo` (macOS/Linux)
- **Dependencies fail**: Try `pip install --user -r requirements.txt`

## 🌟 Features

- **Web Interface**: Easy-to-use drag-and-drop interface (recommended for most users)
- **Command Line**: Power-user CLI interface for automation and scripting
- **Cross-Platform**: Works on Windows, macOS, and Linux
- **Easy Setup**: Automated installation scripts included
- Read from any column in Excel files (.xlsx/.xls format)
- Flexible column specification (by header name, Excel letter like 'A'/'AA', or zero-based index)
- Configurable batch sizes (default: 50 per line)
- Interactive batch navigation with copy functionality
- Preserves original order and includes blank/empty entries
- Support for multiple Excel sheets
- Download complete output as text file

## 🎯 For Your Teammates

This project is designed to be **teammate-friendly**! When sharing:

1. **Zip the entire folder** and send it
2. **No code changes needed** - everything works out of the box
3. **Cross-platform** - works on Windows, macOS, and Linux
4. **Simple setup** - just run the setup script for their OS

## 🎨 Web Interface Features

The Streamlit web app provides:

- **File Upload**: Drag & drop Excel files (.xlsx/.xls)
- **Sheet Selection**: Visual dropdown to choose Excel sheets
- **Column Selection**: Three methods - by header name, Excel letter, or index
- **Data Preview**: See your data before processing
- **Batch Navigation**: Next/Previous buttons and jump-to-batch selector
- **Copy Options**: Multiple formats (comma-separated, line-separated)
- **Statistics**: Real-time counts of names and batches
- **Download**: Get complete output as a text file
- **Responsive Design**: Works on desktop and mobile

## 💻 Command Line Usage (Advanced)

```bash
python batch_names_to_text.py --excel path/to/your/file.xlsx --column A --outfile output_filename
```

### Parameters

- `--excel`: Path to the Excel file (.xlsx)
- `--column`: Column to read from (header name, Excel letter like 'A'/'AA', or zero-based index like '0')
- `--outfile`: Base output filename (without extension) - file will be saved in Downloads folder
- `--sheet-index`: Zero-based sheet index (default: 0 for first sheet)
- `--batch-size`: Number of names per batch/line (default: 50)

### Examples

```bash
# Read from column A, output batches of 50
python batch_names_to_text.py --excel data/users.xlsx --column A --outfile user_batches

# Read from column named "Username", batches of 25
python batch_names_to_text.py --excel data/users.xlsx --column Username --batch-size 25 --outfile usernames

# Read from second sheet (index 1), column B
python batch_names_to_text.py --excel data/users.xlsx --column B --sheet-index 1 --outfile sheet2_names
```

## 📄 Output Format

The script creates a text file with comma-separated names, with each line containing up to the specified batch size:

```
name1, name2, name3, ..., name50

name51, name52, name53, ..., name100

...
```

## 📋 Requirements

All dependencies are listed in `requirements.txt`:
- streamlit>=1.28.0
- pandas>=1.5.0  
- openpyxl>=3.0.0

## 📝 Notes

- Empty/blank cells are preserved as empty strings in the output
- No trimming of whitespace is performed - names are kept as-is
- Output files are automatically saved to your system's Downloads folder (CLI) or downloaded via browser (Web)
- The script handles duplicate names and maintains original order
- Web interface runs locally on your machine - no data is sent to external servers

---

**That's it! 🎉 Your teammates should be up and running in minutes.**