from flask import request
from db_utils import connect_to_db

def delete_data():
    conn = connect_to_db()
    cursor = conn.cursor()

    data = request.get_json()
    # Extract the table name from the data
    table_name = data['table_name']

    # Remove the table name key-value pair from the data dictionary
    del data['table_name']

    # Get the field name and value from the data dictionary
    id_field_name, id_value = next(iter(data.items()))

    # Use a parameterized query to prevent SQL injection
    sql_delete = "DELETE FROM {} WHERE {} = %s".format(table_name, id_field_name)

   
    #data = (id,)
    cursor.execute(sql_delete, (id_value,))
    # #cursor.execute(sql_delete)

    conn.commit()

    cursor.close()
    conn.close()

    return 'Data deleted successfully'