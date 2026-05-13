@echo off
REM Job Portal Django Setup Script for Windows

echo ================================
echo Job Portal - Django Setup
echo ================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    pause
    exit /b 1
)

echo [1/6] Installing Python dependencies...
pip install -r requirements.txt
if errorlevel 1 (
    echo ERROR: Failed to install dependencies
    pause
    exit /b 1
)

echo.
echo [2/6] Running database migrations...
python manage.py makemigrations
python manage.py migrate
if errorlevel 1 (
    echo ERROR: Migration failed
    pause
    exit /b 1
)

echo.
echo [3/6] Creating superuser (admin account)...
echo Please enter superuser credentials:
python manage.py createsuperuser
if errorlevel 1 (
    echo ERROR: Failed to create superuser
    pause
    exit /b 1
)

echo.
echo ================================
echo Setup Complete!
echo ================================
echo.
echo To start the development server, run:
echo   python manage.py runserver
echo.
echo Then visit: http://127.0.0.1:8000/
echo Admin panel: http://127.0.0.1:8000/admin/
echo.
pause
