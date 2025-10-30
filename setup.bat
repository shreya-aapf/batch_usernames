@echo off
REM Windows Setup Script for Batch Username Processor
REM This script will set up the Python environment and dependencies

echo ===============================================
echo   Batch Username Processor - Windows Setup
echo ===============================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Python is not installed or not in PATH!
    echo Please install Python from https://python.org
    echo Make sure to check "Add Python to PATH" during installation
    pause
    exit /b 1
)

echo ✓ Python is installed
python --version

REM Check if pip is available
pip --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: pip is not available!
    echo Please reinstall Python with pip included
    pause
    exit /b 1
)

echo ✓ pip is available

REM Install dependencies
echo.
echo Installing Python dependencies...
echo -----------------------------------------------
pip install -r requirements.txt

if %errorlevel% neq 0 (
    echo.
    echo ERROR: Failed to install dependencies!
    echo Please check your internet connection and try again
    pause
    exit /b 1
)

echo.
echo ===============================================
echo   Setup Complete! 
echo ===============================================
echo.
echo You can now run the application using:
echo   - Web Interface: run.bat
echo   - Command Line: python batch_names_to_text.py --help
echo.
echo Press any key to continue...
pause >nul
