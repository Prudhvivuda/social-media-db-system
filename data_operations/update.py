from flask import request
from db_utils import connect_to_db

def update_data():
    # Get JSON data from the request
    data = request.get_json()
    
    # Extract the table_name from the JSON data
    table_name = data.get('table_name')  # Assuming the request includes the table_name

    # Check if table_name is present in the request
    if not table_name:
        return 'Table name is required', 400

    # Define primary keys for each table
    primary_keys = {
        "user": "user_id",
        "user_auth": "user_id",
        "report": "report_id",
        "device": "device_id",
        "messages": "message_id",
        "followers": "follower_id",
        "posts": "post_id",
        "video": "video_id",
        "photo": "photo_id",
        "likes": "like_id",
        "bookmarks": "bookmark_id",
        "comments": "comment_id",
        "comment_likes": "comment_like_id",
        "comment_reply": "comment_reply_id",
        "tag": "tag_id",
        "repost": "repost_id",
        "mentions": "mention_id",
        "groupss": "group_id",
        "block_list": "id"
    }

    try:
        # Establish a connection to the database
        conn = connect_to_db()
        cursor = conn.cursor()

        # Extract columns and values from the JSON data
        columns = list(data.keys())
        values = list(data.values())

        # Remove 'table_name' from columns and values
        columns.remove('table_name')
        values.remove(table_name)

        # Extract the primary key for the specified table
        primary_key = primary_keys.get(table_name)
        
        # Construct the SET clause for the SQL update query
        set_clause = ', '.join([f"{col} = %s" for col in columns])
        sql_update = f"UPDATE {table_name} SET {set_clause} WHERE {primary_key} = %s"

        print(f"Updating {table_name}")

        # Print information for debugging
        print(set_clause)
        print(values)
        print(sql_update)

        # Execute the SQL update query
        cursor.execute(sql_update, values + [data[primary_key]])
        
        # Commit changes to the database
        conn.commit()

        print(f"Data updated in {table_name} successfully!")

        # Close cursor and database connection
        cursor.close()
        conn.close()

        # Return success message
        return 'Data updated successfully'

    except Exception as e:
        # Handle exceptions and return an error message
        print(f"Error updating data: {str(e)}")
        return f"Error updating data: {str(e)}", 500
