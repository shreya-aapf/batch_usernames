#!/bin/bash
# Universal macOS/Linux Launcher - Double-click friendly!

echo "==============================================="
echo "   Batch Username Processor - Quick Start"
echo "==============================================="
echo ""

# Determine Python command
if command -v python3 &> /dev/null; then
    PYTHON_CMD="python3"
    PIP_CMD="pip3"
elif command -v python &> /dev/null; then
    PYTHON_CMD="python"
    PIP_CMD="pip"
else
    echo "ERROR: Python is not installed!"
    echo "Please install Python 3.7+ from https://python.org"
    echo ""
    echo "On macOS: brew install python"
    echo "On Ubuntu/Debian: sudo apt install python3 python3-pip"
    echo ""
    read -p "Press Enter to exit..."
    exit 1
fi

echo "Found Python: $($PYTHON_CMD --version)"

echo "Checking dependencies..."

# Try to import required packages
$PYTHON_CMD -c "import streamlit, pandas, openpyxl" 2>/dev/null
if [ $? -ne 0 ]; then
    echo "Dependencies not found. Installing now..."
    echo "This may take a minute..."
    echo ""
    
    $PIP_CMD install -r requirements.txt
    if [ $? -ne 0 ]; then
        echo ""
        echo "Failed with $PIP_CMD. Trying user install..."
        $PIP_CMD install --user -r requirements.txt
        if [ $? -ne 0 ]; then
            echo ""
            echo "ERROR: Could not install dependencies!"
            echo "Try running ./setup.sh first"
            read -p "Press Enter to exit..."
            exit 1
        fi
    fi
    echo ""
    echo "Dependencies installed successfully!"
fi

echo ""
echo "==============================================="
echo "   Starting Web Interface..."
echo "==============================================="
echo ""
echo "Your browser should open automatically."
echo "If not, go to: http://localhost:8501"
echo ""
echo "Press Ctrl+C to stop the application"
echo ""

# Start Streamlit - try multiple methods
$PYTHON_CMD -m streamlit run app.py 2>/dev/null
if [ $? -ne 0 ]; then
    streamlit run app.py 2>/dev/null
    if [ $? -ne 0 ]; then
        echo ""
        echo "ERROR: Could not start Streamlit!"
        echo "Try running: $PIP_CMD install streamlit"
        read -p "Press Enter to exit..."
        exit 1
    fi
fi

echo ""
echo "Application stopped."
