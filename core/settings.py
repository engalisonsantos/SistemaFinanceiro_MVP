# ===============================
# DATABASE
# ===============================
DATABASE_URL = os.environ.get("DATABASE_URL", "")

# Correções de esquema caso venha diferente
if DATABASE_URL.startswith("railwaypostgresql://"):
    DATABASE_URL = DATABASE_URL.replace("railwaypostgresql://", "postgresql://", 1)

if DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

if DATABASE_URL:
    DATABASES = {
        "default": dj_database_url.parse(
            DATABASE_URL,
            conn_max_age=600,
            ssl_require=True
        )
    }
else:
    # fallback local (não crasha se estiver sem var no ambiente)
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }
