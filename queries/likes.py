from flask import request

from db_utils import connect_to_db

def get_likes_count():
    conn = connect_to_db()
    cursor = conn.cursor()
    data = request.get_json()
    
    print(f"The request is {data}")
    
    post_id = data.get('post_id')
    sql_query = "SELECT COUNT(*) FROM likes WHERE post_id = %s"
    cursor.execute(sql_query, (post_id,))
    
    result = cursor.fetchone()

    cursor.close()
    conn.close()

    if result:
        return {"number_of_likes": result[0]}
    else:
        return {"number_of_likes": 0}