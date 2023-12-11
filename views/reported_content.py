# Importing the connect_to_db function from the db_utils module
from db_utils import connect_to_db

def get_reported_content():
    """
    Retrieves reported content from the database.

    Returns:
    - result (list): A list of dictionaries representing the fetched data.
    """
    # Establishing a database connection
    conn = connect_to_db()
    cursor = conn.cursor()
    
    # Fetching reported content data
    print("Fetching reported content...")
    sql_query = "SELECT * FROM reported_content_view"
    cursor.execute(sql_query)
    
    # Extracting column names
    columns = [column[0] for column in cursor.description]
    
    # Fetching all rows and converting them into dictionaries
    rows = cursor.fetchall()
    result = [dict(zip(columns, row)) for row in rows]
        
    # Logging the result
    print(result)
    
    # Closing the database cursor and connection
    cursor.close()
    conn.close()

    # Returning the fetched data
    return result
