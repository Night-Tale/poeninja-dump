@echo off
setlocal

cd ..
echo [INFO] Current directory: %CD%

if not exist venv (
    echo [WARN] Can't find venv.
    echo First run scripts\install.bat
    pause
    exit /b 1
)

echo [INFO] Activate venv...
call venv\Scripts\activate.bat

echo [INFO] Export data into Google Sheets...
python -m src.main
if errorlevel 1 (
    echo [ERROR] Export error.
    pause
    exit /b 1
)

echo.
echo [OK] Done.
echo.

pause
endlocal
exit /b 0