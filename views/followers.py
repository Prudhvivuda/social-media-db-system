# Importing the database connection function from the db_utils module
from db_utils import connect_to_db

def get_followers():
    """
    Fetches followers data from the database view.

    Returns:
    - result (list of dicts): List of dictionaries representing the fetched followers data.
    """
    # Establishing a connection to the database
    conn = connect_to_db()
    # Creating a cursor to execute SQL queries
    cursor = conn.cursor()
    
    # Printing a message indicating the fetching of followers data
    print("Fetching followers...")
    
    # SQL query to select all records from the 'followers_view' database view
    sql_query = "SELECT * FROM followers_view"
    cursor.execute(sql_query)
    
    # Extracting column names from the cursor description
    columns = [column[0] for column in cursor.description]
    # Fetching all rows from the cursor
    rows = cursor.fetchall()
    # Converting the fetched rows into a list of dictionaries
    result = [dict(zip(columns, row)) for row in rows]
    
    # Printing the fetched followers data
    print(result)
    
    # Closing the cursor and the database connection
    cursor.close()
    conn.close()

    # Returning the result (list of dictionaries)
    return result
