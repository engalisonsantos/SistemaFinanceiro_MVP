@echo off
cd /d "%~dp0"
start cmd /k py manage.py runserver
timeout /t 3 > nul
start http://127.0.0.1:8000
