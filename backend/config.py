import os

DB_USER = os.getenv("DB_USER", "api_connection")
DB_PASSWORD = os.getenv("DB_PASSWORD", "4P1R3ST")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5453")
DB_NAME = os.getenv("DB_NAME", "hireflowdb")

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"