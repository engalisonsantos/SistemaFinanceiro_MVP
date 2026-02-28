SISTEMA FINANCEIRO (Django) - MVP

1) Pré-requisitos
- Python 3.10+ instalado

2) Instalar dependências
No terminal/prompt dentro da pasta do projeto:
    pip install -r requirements.txt

3) Criar banco e tabelas
    python manage.py makemigrations
    python manage.py migrate

4) Criar usuário Master (admin)
    python manage.py createsuperuser

5) Rodar
    python manage.py runserver

6) Abrir no navegador
    http://127.0.0.1:8000/lancamentos/

CADASTROS (somente Master)
- Entre em http://127.0.0.1:8000/admin/
- Cadastre Groups e Subgroups
- Crie a secretária em Users e defina role = ENTRY

RELATÓRIOS (somente Master)
- http://127.0.0.1:8000/relatorios/periodo/
- Exportações: Excel e PDF (links na tela)

Obs.: A secretária (role ENTRY) não vê relatórios nem admin no menu, e é bloqueada nos endpoints.
