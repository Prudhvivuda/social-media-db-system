from flask import request

from db_utils import connect_to_db

def get_followers_count():
    conn = connect_to_db()
    cursor = conn.cursor()
    data = request.get_json()
    
    print(f"The request is {data}")
    
    user_id = data.get('user_id')
    sql_query = "SELECT COUNT(*) FROM followers WHERE following_user_id = %s"
    cursor.execute(sql_query, (user_id,))
    
    result = cursor.fetchone()

    cursor.close()
    conn.close()

    if result:
        return {"number_of_followers": result[0]}
    else:
        return {"number_of_followers": 0}