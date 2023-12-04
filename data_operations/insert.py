from flask import request
from db_utils import connect_to_db

# def insert_data():
#     conn = connect_to_db()
#     cursor = conn.cursor()
#     data = request.get_json()
#     print(f"Requested data is {data}")
    
#     sql_insert = "INSERT INTO user (user_id, user_name, email_id, phone_number, first_name, last_name, created_at, updated_at, gender, date_of_birth, profile_image, bio, is_verified, is_active, is_reported) \
#                     VALUES ('1114c97a-dd6a-41ae-bfde-6abea2e06ee0', 'pv', 'adventure.seeker@example.com', '1234567890', 'John', 'Doe', '2023-01-01 12:00:00', '2023-01-01 12:00:00', 'Male', '1990-01-15', 'profile_img1.jpg', 'Exploring the world one adventure at a time.', true, true, false)"
        
#     cursor.execute(sql_insert)
#     conn.commit()
    
#     print("Data Inserted Successfully!")

#     cursor.close()
#     conn.close()

#     return 'Data Inserted Successfully'


##############

def insert_data():
    data = request.get_json()
    table_name = data.get('table_name')  # Assuming the request includes the table_name

    if not table_name:
        return 'Table name is required', 400

    try:
        conn = connect_to_db()
        cursor = conn.cursor()

        columns = list(data.keys())
        values = list(data.values())
        
        columns.remove('table_name')
        values.remove(table_name)
        
        print(f"Inserting into {table_name}")
        sql_insert = f"INSERT INTO user ({', '.join(columns)}) VALUES ({', '.join(['%s' for _ in values])})"

        cursor.execute(sql_insert, values)
        conn.commit()

        print(f"Data inserted into {table_name} successfully!")

        cursor.close()
        conn.close()

        return f"Data inserted into {table_name} successfully!"

    except Exception as e:
        print(f"Error inserting data: {str(e)}")
        return f"Error inserting data: {str(e)}", 500