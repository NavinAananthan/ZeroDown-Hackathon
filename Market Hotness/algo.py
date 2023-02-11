import psycopg2
import pandas as pd

def select_data(conn, cursor,tablename,id):
    select_query = f"SELECT * FROM {tablename} where id={id};"
    cursor.execute(select_query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)

try:
    conn = psycopg2.connect(
        host="localhost",
        database="zerodown",
        user="postgres",
        password="navin123$"
    )

    cursor = conn.cursor()

    # SELECT
    select_data(conn, cursor, 'market','372492')

    conn.commit()




except (Exception, psycopg2.Error) as error:
    print("Error while working with PostgreSQL", error)
    
finally:
    if conn:
        cursor.close()
        conn.close()
        print("Connection closed")


