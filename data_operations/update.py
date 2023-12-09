from flask import request
from db_utils import connect_to_db

def update_data():
    data = request.get_json()
    table_name = data.get('table_name')  # Assuming the request includes the table_name

    if not table_name:
        return 'Table name is required', 400

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
        conn = connect_to_db()
        cursor = conn.cursor()

        columns = list(data.keys())
        values = list(data.values())
        #user_id = data.get("user_id")

        columns.remove('table_name')
        values.remove(table_name)
        #columns.remove('user_id')
        #values.remove(user_id)

        primary_key = primary_keys.get(table_name)
        
        set_clause = ', '.join([f"{col} = %s" for col in columns])
        sql_update = f"UPDATE {table_name} SET {set_clause} WHERE {primary_key} = %s"

        print(f"Updating {table_name}")

        print(set_clause)
        print(values)
        print(sql_update)

        cursor.execute(sql_update, values + [data[primary_key]])
        
        conn.commit()

        print(f"Data updated in {table_name} successfully!")

        cursor.close()
        conn.close()

        return 'Data updated successfully'

    except Exception as e:
        print(f"Error Updating data: {str(e)}")
        return f"Error Updating data: {str(e)}", 500