import psycopg2
from config import *

def get_connection():
    return psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )

def get_site_elements():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT name, complexity_id FROM site_elements;")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows
