@echo off
echo ====================================
echo INICIANDO SISTEMA EM MODO PRODUCAO
echo ====================================

set DJANGO_DEBUG=False
set DJANGO_ALLOWED_HOSTS=127.0.0.1,localhost
set DJANGO_SECRET_KEY=dev-secret-chave-local

echo Rodando migracoes...
python manage.py migrate

echo Coletando arquivos estaticos...
python manage.py collectstatic --noinput

echo Iniciando servidor Gunicorn...
gunicorn core.wsgi --bind 127.0.0.1:8000

pause
