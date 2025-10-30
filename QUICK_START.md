# 🚀 Quick Start Guide

Get up and running in under 2 minutes!

## Super Easy Way (Recommended)

### Windows Users
1. **Double-click `START_HERE.bat`** - That's it! 
2. Upload your Excel file when the browser opens

### macOS/Linux Users  
1. **Double-click `START_HERE.sh`** - That's it!
2. Upload your Excel file when the browser opens

## Manual Way (If above doesn't work)

### Windows Users
1. **Double-click** `setup.bat` to install dependencies
2. **Double-click** `run.bat` to start the web interface
3. Open your browser to the URL shown (usually http://localhost:8501)

### macOS/Linux Users
1. **Right-click** on `setup.sh` → "Open with Terminal" (or open terminal and run `./setup.sh`)
2. **Right-click** on `run.sh` → "Open with Terminal" (or run `./run.sh`)
3. Open your browser to the URL shown (usually http://localhost:8501)

## Alternative: Command Line

If the scripts don't work, you can run these commands:

```bash
# Install dependencies
pip install -r requirements.txt

# Start web interface  
streamlit run app.py

# Or use command line tool
python batch_names_to_text.py --help
```

## What You Need

- **Python 3.7+** (Download from https://python.org)
- **Excel file** with your data

## Troubleshooting

- **Python not found**: Install Python and make sure it's added to your PATH
- **Permission denied**: Try running as administrator (Windows) or with `sudo` (macOS/Linux)
- **Dependencies fail**: Try `pip install --user -r requirements.txt`

That's it! 🎉
