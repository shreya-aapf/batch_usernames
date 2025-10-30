@echo off
REM Windows Launcher for Batch Username Processor Web Interface

echo ===============================================
echo   Batch Username Processor - Web Interface
echo ===============================================
echo.
echo Starting the web application...
echo Your browser should open automatically.
echo If not, go to: http://localhost:8501
echo.
echo Press Ctrl+C to stop the application
echo.

REM Start Streamlit
streamlit run app.py

echo.
echo Application stopped.
pause
