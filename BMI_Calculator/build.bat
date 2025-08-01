@echo off
REM Install dependencies
pip install pyinstaller pillow

REM Create icon if doesn't exist
if not exist "icon.ico" (
    python create_icon.py
)

REM Build executable with simplified name
pyinstaller --onefile --windowed --icon=icon.ico --name BMICalculator bmi_calculator.py

REM Check if build succeeded
if exist "dist\BMICalculator.exe" (
    echo Build successful!
) else (
    echo Build failed! Check for errors.
    pause
    exit /b 1
)