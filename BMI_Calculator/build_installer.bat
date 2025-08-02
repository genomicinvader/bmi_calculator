@echo off
REM Run build script
call build.bat

REM Check if build succeeded before creating installer
if not exist "dist\BMICalculator.exe" (
    echo Build failed! Cannot create installer.
    pause
    exit /b 1
)

REM Build installer
"C:\Program Files (x86)\Inno Setup 6\ISCC.exe" setup.iss

REM Open output directory if installer was created
if exist "installer\BMI_Calculator_Setup.exe" (
    explorer installer
) else (
    echo Installer creation failed!
    pause
)