from db.mysql_client import get_connection

def load_to_mysql(df, table_name):
    connection = get_connection()
    cursor = connection.cursor()

    insert_query = f"""
    INSERT INTO {table_name} (id, name, department, salary)
    VALUES (%s, %s, %s, %s)
    """

    for _, row in df.iterrows():
        cursor.execute(insert_query, tuple(row))

    connection.commit()
    cursor.close()
    connection.close()