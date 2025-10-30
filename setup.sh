#!/bin/bash
# macOS/Linux Setup Script for Batch Username Processor
# This script will set up the Python environment and dependencies

echo "==============================================="
echo "   Batch Username Processor - Setup"
echo "==============================================="
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    if ! command -v python &> /dev/null; then
        echo "ERROR: Python is not installed!"
        echo "Please install Python 3.7+ from https://python.org"
        echo ""
        echo "On macOS, you can also use Homebrew:"
        echo "  brew install python"
        echo ""
        echo "On Ubuntu/Debian:"
        echo "  sudo apt update && sudo apt install python3 python3-pip"
        exit 1
    else
        PYTHON_CMD="python"
    fi
else
    PYTHON_CMD="python3"
fi

echo "✓ Python is installed"
$PYTHON_CMD --version

# Check if pip is available
if ! command -v pip3 &> /dev/null; then
    if ! command -v pip &> /dev/null; then
        echo "ERROR: pip is not available!"
        echo "Please install pip or reinstall Python with pip included"
        exit 1
    else
        PIP_CMD="pip"
    fi
else
    PIP_CMD="pip3"
fi

echo "✓ pip is available"

# Install dependencies
echo ""
echo "Installing Python dependencies..."
echo "-----------------------------------------------"
$PIP_CMD install -r requirements.txt

if [ $? -ne 0 ]; then
    echo ""
    echo "ERROR: Failed to install dependencies!"
    echo "Please check your internet connection and try again"
    echo ""
    echo "You might need to use:"
    echo "  pip3 install --user -r requirements.txt"
    echo "if you don't have system-wide Python permissions"
    exit 1
fi

# Make run script executable
if [ -f "run.sh" ]; then
    chmod +x run.sh
fi

echo ""
echo "==============================================="
echo "   Setup Complete!"
echo "==============================================="
echo ""
echo "You can now run the application using:"
echo "  - Web Interface: ./run.sh"
echo "  - Command Line: $PYTHON_CMD batch_names_to_text.py --help"
echo ""
