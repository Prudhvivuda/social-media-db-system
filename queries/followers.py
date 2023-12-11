from flask import request
from db_utils import connect_to_db

def get_followers_count():
    # Establish a connection to the database
    conn = connect_to_db()
    cursor = conn.cursor()

    # Get JSON data from the request
    data = request.get_json()

    # Print information for debugging
    print(f"The request is {data}")

    # Extract user_id from the JSON data
    user_id = data.get('user_id')

    # Define SQL query to count the number of followers for a user
    sql_query = "SELECT COUNT(*) FROM followers WHERE following_user_id = %s"
    
    # Execute the SQL query with the provided user_id as a parameter
    cursor.execute(sql_query, (user_id,))
    
    # Fetch the result of the SQL query
    result = cursor.fetchone()

    # Close cursor and database connection
    cursor.close()
    conn.close()

    # Check if the result is not empty
    if result:
        # Return the number of followers as a dictionary
        return {"number_of_followers": result[0]}
    else:
        # If the result is empty, return zero followers
        return {"number_of_followers": 0}
