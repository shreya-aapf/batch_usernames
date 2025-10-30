# Batch Username Processor

A Python utility that reads names/usernames from Excel files and outputs them in comma-separated batches. Available as both a **user-friendly web interface** and a command-line tool.

## 🚀 Super Quick Start

**Just downloaded? Get running in 30 seconds:**

### Step-by-Step Instructions
#### Windows
1. **Double-click `START_HERE.bat`** - Does setup and starts the app in one go!

*Or manually:*
1. Double-click `setup.bat` to install dependencies
2. Double-click `run.bat` to start the app

#### macOS/Linux  
1. **Double-click `START_HERE.sh`** - Does setup and starts the app in one go!

*Or manually:*
1. Double-click `setup.sh` (or run `./setup.sh` in terminal) to install dependencies
2. Double-click `run.sh` (or run `./run.sh` in terminal) to start the app

> 📋 **See [QUICK_START.md](QUICK_START.md) for detailed instructions and troubleshooting**

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

## 📖 Detailed Usage

### Web Interface (Recommended)

**Quick Start:** Run `setup.bat` (Windows) or `./setup.sh` (macOS/Linux), then `run.bat` or `./run.sh`

**Manual Installation:**
```bash
pip install -r requirements.txt
streamlit run app.py
```

This will open a web browser with an intuitive interface where you can:
- 📁 Upload your Excel file
- 🎯 Select columns and sheets visually  
- ⚙️ Set batch size with a slider
- 🧭 Navigate through batches with next/previous buttons
- 📋 Copy batches with one click
- 💾 Download the complete output

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

## Output Format

The script creates a text file with comma-separated names, with each line containing up to the specified batch size:

```
name1, name2, name3, ..., name50

name51, name52, name53, ..., name100

...
```

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
