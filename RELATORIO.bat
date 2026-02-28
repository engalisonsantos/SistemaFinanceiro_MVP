@echo off
setlocal

REM ===========================
REM  RELATORIO - Sistema Financeiro (Django)
REM  - Inicia o servidor (se ainda não estiver rodando)
REM  - Abre o relatório por período no navegador
REM ===========================

REM Vai para a pasta onde este .bat está (coloque este arquivo na raiz do projeto, ao lado do manage.py)
cd /d "%~dp0"

REM Inicia o servidor em uma nova janela
start "Servidor Django" cmd /k py manage.py runserver

REM Aguarda um pouco para o servidor subir
timeout /t 2 /nobreak >nul

REM Abre o relatório no navegador padrão
start "" "http://127.0.0.1:8000/relatorios/periodo/"

echo.
echo Relatorio aberto no navegador.
echo Se aparecer erro de conexao, aguarde alguns segundos e atualize (F5).
echo.
endlocal
