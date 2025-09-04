@echo off
echo 🚀 ConferenceHub-Live Update Script
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python not found. Please install Python 3.8+ and try again.
    pause
    exit /b 1
)

REM Install requirements if needed
echo 📦 Installing requirements...
pip install -r requirements.txt

REM Run the update
echo 🔄 Updating conferences...
python update_conferences.py

REM Check if successful
if errorlevel 1 (
    echo ❌ Update failed. Check error messages above.
    pause
    exit /b 1
)

echo ✅ Update completed successfully!
echo 📄 Check README.md for updated conference table
echo.
pause
