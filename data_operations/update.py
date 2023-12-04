from flask import request
from db_utils import connect_to_db

def update_data():
    conn = connect_to_db()
    cursor = conn.cursor()

    data = request.get_json()
    value1 = data['value1']
    value2 = data['value2']
    id = data['id']

    sql_update = "UPDATE table_name SET column1 = %s, column2 = %s WHERE id = %s"
    data = (value1, value2, id)
    cursor.execute(sql_update, data)

    conn.commit()

    cursor.close()
    conn.close()

    return 'Data updated successfully'