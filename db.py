import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

db_name = os.getenv("DB_NAME")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")


def get_db_connection():
    conn = psycopg2.connect(dbname=db_name, user=db_user, password=db_password)
    return conn
