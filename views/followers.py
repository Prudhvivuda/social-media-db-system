from db_utils import connect_to_db

def get_followers():
    conn = connect_to_db()
    cursor = conn.cursor()
    
    print("Fetching followers...")
    sql_query = "SELECT * FROM followers_view"
    cursor.execute(sql_query)
    
    columns = [column[0] for column in cursor.description]
    rows = cursor.fetchall()
    result = [dict(zip(columns, row)) for row in rows]
        
    print(result)
    
    cursor.close()
    conn.close()

    return result