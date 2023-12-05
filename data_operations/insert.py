from flask import request
from db_utils import connect_to_db

def insert_data():
    data = request.get_json()
    table_name = data.get('table_name')  # Assuming the request includes the table_name

    if not table_name:
        return 'Table name is required', 400

    try:
        conn = connect_to_db()
        cursor = conn.cursor()

        columns = list(data.keys())
        values = list(data.values())
        
        columns.remove('table_name')
        values.remove(table_name)
        
        print(f"Inserting into {table_name}")
        sql_query = f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES ({', '.join(['%s' for _ in values])})"

        cursor.execute(sql_query, values)
        conn.commit()

        print(f"Data inserted into {table_name} successfully!")

        cursor.close()
        conn.close()

        return f"Data inserted into {table_name} successfully!"

    except Exception as e:
        print(f"Error inserting data: {str(e)}")
        return f"Error inserting data: {str(e)}", 500
