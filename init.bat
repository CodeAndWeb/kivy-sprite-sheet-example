@echo off
setlocal enabledelayedexpansion

echo Setting up Kivy Sprite Sheet Animation Example...

REM Create virtual environment
echo Creating virtual environment...
python -m venv venv
if !errorlevel! neq 0 (
    echo Error creating virtual environment
    pause
    exit /b 1
)

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat
if !errorlevel! neq 0 (
    echo Error activating virtual environment
    pause
    exit /b 1
)

REM Upgrade pip
echo Upgrading pip...
python -m pip install --upgrade pip

REM Install dependencies
echo Installing dependencies...
pip install -r requirements.txt
if !errorlevel! neq 0 (
    echo Error installing dependencies
    pause
    exit /b 1
)

echo Setup complete! Run 'run.bat' to start the application.
pause
