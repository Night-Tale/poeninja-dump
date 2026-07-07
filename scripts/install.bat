@echo off
setlocal

cd ..
echo [INFO] Current directory: %CD%

if exist venv (
    echo [INFO] Venv already exists: venv
) else (
    echo [INFO] Create venv...
    python -m venv venv
    if errorlevel 1 (
        echo [ERROR] Can't create venv.
        pause
        exit /b 1
    )
)

echo [INFO] Activate venv and install requirements.txt...
call venv\Scripts\activate.bat

pip install --upgrade pip
pip install -r requirements.txt
if errorlevel 1 (
    echo [ERROR] Can't install requirements.
    pause
    exit /b 1
)

echo.
echo [OK] Install finished.
echo.

pause
endlocal
exit /b 0