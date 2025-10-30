@echo off
REM Universal Windows Launcher - Double-click friendly!

echo ===============================================
echo   Batch Username Processor - Quick Start
echo ===============================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Python is not installed!
    echo Please install Python from https://python.org
    echo Make sure to check "Add Python to PATH" during installation
    echo.
    pause
    exit /b 1
)

echo Checking dependencies...

REM Try to import required packages
python -c "import streamlit, pandas, openpyxl" 2>nul
if %errorlevel% neq 0 (
    echo Dependencies not found. Installing now...
    echo This may take a minute...
    echo.
    
    python -m pip install -r requirements.txt
    if %errorlevel% neq 0 (
        echo.
        echo Failed to install with pip. Trying user install...
        python -m pip install --user -r requirements.txt
        if %errorlevel% neq 0 (
            echo.
            echo ERROR: Could not install dependencies!
            echo Try running setup.bat first
            pause
            exit /b 1
        )
    )
    echo.
    echo Dependencies installed successfully!
)

echo.
echo ===============================================
echo   Starting Web Interface...
echo ===============================================
echo.
echo Your browser should open automatically.
echo If not, go to: http://localhost:8501
echo.
echo Press Ctrl+C to stop the application
echo.

REM Start Streamlit - try multiple methods
python -m streamlit run app.py 2>nul
if %errorlevel% neq 0 (
    streamlit run app.py 2>nul
    if %errorlevel% neq 0 (
        echo.
        echo ERROR: Could not start Streamlit!
        echo Try running: python -m pip install streamlit
        pause
        exit /b 1
    )
)

echo.
echo Application stopped.
pause
