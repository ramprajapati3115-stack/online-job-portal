#!/bin/bash

# Job Portal Django Setup Script for Linux/Mac

echo "================================"
echo "Job Portal - Django Setup"
echo "================================"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python 3 is not installed"
    exit 1
fi

echo "[1/6] Installing Python dependencies..."
pip install -r requirements.txt
if [ $? -ne 0 ]; then
    echo "ERROR: Failed to install dependencies"
    exit 1
fi

echo ""
echo "[2/6] Running database migrations..."
python3 manage.py makemigrations
python3 manage.py migrate
if [ $? -ne 0 ]; then
    echo "ERROR: Migration failed"
    exit 1
fi

echo ""
echo "[3/6] Creating superuser (admin account)..."
echo "Please enter superuser credentials:"
python3 manage.py createsuperuser
if [ $? -ne 0 ]; then
    echo "ERROR: Failed to create superuser"
    exit 1
fi

echo ""
echo "================================"
echo "Setup Complete!"
echo "================================"
echo ""
echo "To start the development server, run:"
echo "  python3 manage.py runserver"
echo ""
echo "Then visit: http://127.0.0.1:8000/"
echo "Admin panel: http://127.0.0.1:8000/admin/"
echo ""
