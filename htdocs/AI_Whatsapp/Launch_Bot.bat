@echo off
echo ============================
echo   Lancement du bot WhatsApp
echo ============================

cd /d "%~dp0"

REM ============================
REM Activation du venv existant
REM ============================
call venv\Scripts\activate

echo.
echo Installation des dependances...
python -m pip install -r "API\requirements.txt"

echo.
echo Installation des navigateurs Playwright...
python -m playwright install

echo.
echo Lancement du bot...
python "API\main_ai.py"

echo.
echo Bot arrete.
pause
