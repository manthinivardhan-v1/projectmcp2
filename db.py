import psycopg2
from config import settings

def get_connection():
    return psycopg2.connect(settings.DATABASE_URL)


def run_query(sql: str):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(sql)

    columns = [desc[0] for desc in cur.description]
    rows = cur.fetchall()

    cur.close()
    conn.close()

    return [dict(zip(columns, row)) for row in rows]