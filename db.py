import psycopg

def get_site_elements():
    conn = psycopg.connect(
        dbname="pks_1",
        user="postgres",
        password="997299",
        host=os.getenv("DB_HOST"),
        port="5432"
    )
    cur = conn.cursor()
    cur.execute("SELECT * FROM site_elements;")
    data = cur.fetchall()
    cur.close()
    conn.close()
    return data
