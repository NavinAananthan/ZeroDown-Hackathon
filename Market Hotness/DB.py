import psycopg2


def select_data(conn, cursor,tablename):
    select_query = f"SELECT * FROM {tablename}"
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

    # Creating the Table market
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS market (
            id INT NOT NULL PRIMARY KEY,
            name TEXT,
            market_level TEXT,
            city TEXT,
            state TEXT
        );
        """
    )


    # Creating the table market_metrics
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS market_metrics (
            market_id INT,
            time_bucket DATE,
            new_listings_count BIGINT,
            sold_homes_count BIGINT,
            homes_sold_over_list_price_count BIGINT,
            median_list_price_psqft FLOAT,
            median_sale_price_psqft FLOAT,
            median_sale_price FLOAT,
            median_sale_to_list_ratio FLOAT,
            days_to_pending FLOAT,
            days_to_sell FLOAT
        );
        """
    )

    
    index_name = "idx_market_metrics_market_id"
    table_name = "market_metrics"
    column_name = "market_id"

    create_index_query = f"CREATE INDEX IF NOT EXISTS {index_name} ON {table_name} ({column_name})"
    
    cursor.execute(create_index_query)




    # This command is to dump the data into the table market
    with open("E:\Zero-Down Hackathon\Market Hotness\market.sql", "r") as file:
        sql_file = file.read()

    cursor.execute(sql_file)

    # This Command is used to dump into the table market metrics
    with open("E:\Zero-Down Hackathon\Market Hotness\market_metrics.sql", "r") as file:
        sql_file = file.read()

    cursor.execute(sql_file)

    select_data(conn,cursor,'market_metrics')

    conn.commit()
    cursor.close()


except (Exception, psycopg2.Error) as error:
    print("Error while working with PostgreSQL", error)
    

finally:
    if conn:
        cursor.close()
        conn.close()
        print("Connection closed")






