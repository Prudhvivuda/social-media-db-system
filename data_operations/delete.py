from flask import request
from db_utils import connect_to_db

def delete_data():
    conn = connect_to_db()
    cursor = conn.cursor()

    data = request.get_json()
    id = data['id']

    sql_delete = "DELETE FROM table_name WHERE id = %s"
    data = (id,)
    cursor.execute(sql_delete, data)

    conn.commit()

    cursor.close()
    conn.close()

    return 'Data deleted successfully'