import os

# Railway Variables
BOT_TOKEN = os.getenv("BOT_TOKEN")
DB_NAME = os.getenv("DB_NAME", "railway")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "vUSQNQBEGyuVWQRKkfVbkKfpSGyMyjEr")
DB_HOST = os.getenv("DB_HOST", "postgres.railway.internal")
DB_PORT = os.getenv("DB_PORT", "5432")
