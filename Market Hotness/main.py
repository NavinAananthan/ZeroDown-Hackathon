import psycopg2



def insert_into_table():
    return true



try:
    conn = psycopg2.connect(
        host="localhost",
        database="perntodo",
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

    create_index_query = f"CREATE INDEX {index_name} ON {table_name} ({column_name})"
    
    cursor.execute(create_index_query)

    conn.commit()
    cursor.close()

except (Exception, psycopg2.Error) as error:
    print("Error while working with PostgreSQL", error)
    
finally:
    if conn:
        cursor.close()
        conn.close()
        print("Connection closed")






