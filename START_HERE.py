#!/usr/bin/env python3
"""
Universal starter script for Batch Username Processor
Works on Windows, macOS, and Linux - no setup required!

Just double-click this file or run: python START_HERE.py
"""

import sys
import subprocess
import os
from pathlib import Path


def run_command(cmd, shell=False):
    """Run a command and return success status."""
    try:
        result = subprocess.run(cmd, shell=shell, check=True, 
                              capture_output=True, text=True)
        return True, result.stdout
    except subprocess.CalledProcessError as e:
        return False, e.stderr
    except FileNotFoundError:
        return False, "Command not found"


def check_dependencies():
    """Check if dependencies are installed."""
    try:
        import streamlit
        import pandas
        import openpyxl
        return True
    except ImportError:
        return False


def install_dependencies():
    """Install required dependencies."""
    print("📦 Installing dependencies...")
    print("This may take a minute...")
    
    # Try pip3 first, then pip
    for pip_cmd in ['pip3', 'pip']:
        success, output = run_command([pip_cmd, 'install', '-r', 'requirements.txt'])
        if success:
            print("✅ Dependencies installed successfully!")
            return True
        
    # Try with --user flag
    for pip_cmd in ['pip3', 'pip']:
        success, output = run_command([pip_cmd, 'install', '--user', '-r', 'requirements.txt'])
        if success:
            print("✅ Dependencies installed successfully!")
            return True
    
    print("❌ Failed to install dependencies.")
    print("Please try running setup.bat (Windows) or ./setup.sh (macOS/Linux)")
    return False


def start_app():
    """Start the Streamlit app."""
    print("\n🚀 Starting Batch Username Processor...")
    print("Your web browser should open automatically.")
    print("If not, go to: http://localhost:8501")
    print("\nPress Ctrl+C to stop the application")
    print("-" * 50)
    
    # Try streamlit command
    try:
        subprocess.run(['streamlit', 'run', 'app.py'], check=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        # Try with python -m streamlit
        try:
            python_cmd = 'python3' if sys.platform != 'win32' else 'python'
            subprocess.run([python_cmd, '-m', 'streamlit', 'run', 'app.py'], check=True)
        except Exception as e:
            print(f"❌ Failed to start app: {e}")
            return False
    
    return True


def main():
    """Main function."""
    print("=" * 60)
    print("   🎯 Batch Username Processor - Universal Launcher")
    print("=" * 60)
    print("")
    
    # Check if we're in the right directory
    if not Path('app.py').exists():
        print("❌ Error: app.py not found!")
        print("Make sure you're running this from the project directory.")
        input("\nPress Enter to exit...")
        return
    
    # Check if dependencies are installed
    if not check_dependencies():
        print("📋 Dependencies not found. Installing now...")
        if not install_dependencies():
            input("\nPress Enter to exit...")
            return
        
        # Check again after installation
        if not check_dependencies():
            print("❌ Installation failed. Please run setup manually.")
            input("\nPress Enter to exit...")
            return
    
    print("✅ All dependencies ready!")
    
    # Start the app
    if not start_app():
        print("\n❌ Failed to start the application.")
        print("Try running:")
        if sys.platform.startswith('win'):
            print("  - setup.bat (to install)")
            print("  - run.bat (to start)")
        else:
            print("  - ./setup.sh (to install)")
            print("  - ./run.sh (to start)")
        
        input("\nPress Enter to exit...")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Application stopped by user.")
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        print("Please try using the setup scripts instead:")
        if sys.platform.startswith('win'):
            print("  - Double-click setup.bat")
            print("  - Double-click run.bat")
        else:
            print("  - Run ./setup.sh")
            print("  - Run ./run.sh")
        
        input("\nPress Enter to exit...")
