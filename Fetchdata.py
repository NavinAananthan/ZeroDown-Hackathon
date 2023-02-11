import psycopg2
import csv


def data_csv(cursor,filename,tablename):

    query=f"select * from {tablename};"
    cursor.execute(query)
    rows=cursor.fetchall()
    
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([i[0] for i in cursor.description])
        writer.writerows(rows)


try:
    conn = psycopg2.connect(
        host="localhost",
        database="zerodown",
        user="postgres",
        password="navin123$"
    )

    cursor = conn.cursor()

    #data_csv(cursor,'market.csv','market')
    data_csv(cursor,'market_metrics.csv','market_metrics')

    conn.commit()




except (Exception, psycopg2.Error) as error:
    print("Error while working with PostgreSQL", error)
    
finally:
    if conn:
        cursor.close()
        conn.close()
        print("Connection closed")


