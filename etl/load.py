from db.mysql_client import get_connection

def load_to_mysql(df, table_name):
    connection = get_connection()
    cursor = connection.cursor()

    insert_query = f"""
    INSERT INTO {table_name} (id, name, department, salary)
    VALUES (%s, %s, %s, %s)
    """

    data = [tuple(row) for _, row in df.iterrows()]
    cursor.executemany(insert_query, data)

    connection.commit()
    cursor.close()
    connection.close()
