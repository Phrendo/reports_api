import pyodbc
from app.settings import Settings

def get_db_connection():
    settings = Settings()
    return pyodbc.connect(settings.DATABASE_URL)
