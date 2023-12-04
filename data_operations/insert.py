from flask import request
from db_utils import connect_to_db

def insert_data():
    conn = connect_to_db()
    cursor = conn.cursor()
    data = request.get_json()
    print(f"Requested data is {data}")
    
    sql_insert = "INSERT INTO user (user_id, user_name, email_id, phone_number, first_name, last_name, created_at, updated_at, gender, date_of_birth, profile_image, bio, is_verified, is_active, is_reported) \
                    VALUES ('7454c97a-dd6a-41ae-bfde-6abea2e06ee0', 'Prrudhviii', 'adventure.seeker@example.com', '1234567890', 'John', 'Doe', '2023-01-01 12:00:00', '2023-01-01 12:00:00', 'Male', '1990-01-15', 'profile_img1.jpg', 'Exploring the world one adventure at a time.', true, true, false)"
        
    cursor.execute(sql_insert)
    conn.commit()
    print("Data inserted!")

    cursor.close()
    conn.close()

    return 'Data inserted successfully'