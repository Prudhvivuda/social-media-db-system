from flask import request
from db_utils import connect_to_db

def insert_data():
    # Get JSON data from the request
    data = request.get_json()
    
    # Extract the table_name from the JSON data
    table_name = data.get('table_name')  # Assuming the request includes the table_name

    # Check if table_name is present in the request
    if not table_name:
        return 'Table name is required', 400

    try:
        # Establish a connection to the database
        conn = connect_to_db()
        cursor = conn.cursor()

        # Extract columns and values from the JSON data
        columns = list(data.keys())
        values = list(data.values())

        # Remove 'table_name' from columns and values
        columns.remove('table_name')
        values.remove(table_name)

        # Build and execute the SQL query for insertion
        print(f"Inserting into {table_name}")
        sql_query = f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES ({', '.join(['%s' for _ in values])})"
        cursor.execute(sql_query, values)
        
        # Commit changes to the database
        conn.commit()

        # Close cursor and database connection
        cursor.close()
        conn.close()

        # Return success message
        return f"Data inserted into {table_name} successfully!"

    except Exception as e:
        # Handle exceptions and return an error message
        print(f"Error inserting data: {str(e)}")
        return f"Error inserting data: {str(e)}", 500
