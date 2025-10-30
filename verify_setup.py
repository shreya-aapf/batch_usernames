#!/usr/bin/env python3
"""
Verification script to ensure the environment is set up correctly
for the Batch Username Processor.
"""

import sys
import subprocess
import importlib
from pathlib import Path


def check_python_version():
    """Check if Python version is compatible."""
    print("🐍 Checking Python version...")
    version = sys.version_info
    if version.major == 3 and version.minor >= 7:
        print(f"   ✅ Python {version.major}.{version.minor}.{version.micro} - OK")
        return True
    else:
        print(f"   ❌ Python {version.major}.{version.minor}.{version.micro} - Need Python 3.7+")
        return False


def check_dependencies():
    """Check if required packages are installed."""
    print("\n📦 Checking dependencies...")
    
    required_packages = {
        'streamlit': 'streamlit>=1.28.0',
        'pandas': 'pandas>=1.5.0',
        'openpyxl': 'openpyxl>=3.0.0'
    }
    
    all_ok = True
    
    for package, requirement in required_packages.items():
        try:
            module = importlib.import_module(package)
            version = getattr(module, '__version__', 'unknown')
            print(f"   ✅ {package} {version} - OK")
        except ImportError:
            print(f"   ❌ {package} - NOT INSTALLED")
            print(f"      Install with: pip install {requirement}")
            all_ok = False
    
    return all_ok


def check_files():
    """Check if required files exist."""
    print("\n📁 Checking required files...")
    
    required_files = [
        'app.py',
        'batch_names_to_text.py',
        'requirements.txt',
        'README.md'
    ]
    
    all_ok = True
    
    for file in required_files:
        if Path(file).exists():
            print(f"   ✅ {file} - OK")
        else:
            print(f"   ❌ {file} - MISSING")
            all_ok = False
    
    return all_ok


def check_downloads_folder():
    """Check if Downloads folder is accessible."""
    print("\n💾 Checking Downloads folder access...")
    
    try:
        downloads_dir = Path.home() / "Downloads"
        downloads_dir.mkdir(parents=True, exist_ok=True)
        
        # Try to create a test file
        test_file = downloads_dir / "batch_processor_test.txt"
        test_file.write_text("test")
        test_file.unlink()  # Remove test file
        
        print(f"   ✅ Downloads folder accessible: {downloads_dir}")
        return True
    except Exception as e:
        print(f"   ❌ Downloads folder issue: {e}")
        return False


def main():
    """Run all verification checks."""
    print("=" * 50)
    print("  Batch Username Processor - Setup Verification")
    print("=" * 50)
    
    checks = [
        check_python_version(),
        check_dependencies(),
        check_files(),
        check_downloads_folder()
    ]
    
    print("\n" + "=" * 50)
    
    if all(checks):
        print("🎉 All checks passed! You're ready to go!")
        print("\nTo start the web interface:")
        if sys.platform.startswith('win'):
            print("   Double-click run.bat")
        else:
            print("   Run ./run.sh")
    else:
        print("❌ Some checks failed. Please fix the issues above.")
        print("\nTry running the setup script:")
        if sys.platform.startswith('win'):
            print("   Double-click setup.bat")
        else:
            print("   Run ./setup.sh")
    
    print("=" * 50)


if __name__ == "__main__":
    main()
