# Deploy Sistema Financeiro - Railway

## 1) Preparação Local

py -m pip install gunicorn dj-database-url psycopg2-binary whitenoise python-dotenv
py -m pip freeze > requirements.txt

Certifique-se que existem:
- Procfile
- runtime.txt
- .gitignore

---

## 2) Subir para GitHub

git init
git add .
git commit -m "Deploy ready"
git branch -M main
git remote add origin URL_DO_SEU_REPO
git push -u origin main

---

## 3) Criar projeto no Railway

1. Acesse https://railway.app
2. New Project -> Deploy from GitHub
3. Selecione o repositório

---

## 4) Adicionar PostgreSQL

No Railway:
Plugins -> Add Plugin -> PostgreSQL

---

## 5) Variáveis de Ambiente

Adicionar no Railway:

DJANGO_SECRET_KEY = (gerar chave segura)
DJANGO_DEBUG = False
DJANGO_ALLOWED_HOSTS = dominio.railway.app

---

## 6) Rodar Migrações

python manage.py migrate
python manage.py createsuperuser
python manage.py collectstatic --noinput

Sistema pronto para uso online.
