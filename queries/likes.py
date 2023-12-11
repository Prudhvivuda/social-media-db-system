from flask import request
from db_utils import connect_to_db

def get_likes_count():
    # Establish a connection to the database
    conn = connect_to_db()
    cursor = conn.cursor()

    # Get JSON data from the request
    data = request.get_json()

    # Print information for debugging
    print(f"The request is {data}")

    # Extract post_id from the JSON data
    post_id = data.get('post_id')

    # Define SQL query to count the number of likes for a post
    sql_query = "SELECT COUNT(*) FROM likes WHERE post_id = %s"
    
    # Execute the SQL query with the provided post_id as a parameter
    cursor.execute(sql_query, (post_id,))
    
    # Fetch the result of the SQL query
    result = cursor.fetchone()

    # Close cursor and database connection
    cursor.close()
    conn.close()

    # Check if the result is not empty
    if result:
        # Return the number of likes as a dictionary
        return {"number_of_likes": result[0]}
    else:
        # If the result is empty, return zero likes
        return {"number_of_likes": 0}
