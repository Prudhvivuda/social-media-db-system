# from flask import Flask, request
# import mysql.connector

# app = Flask(__name__)

# def connect_to_db():
#     print("Connecting to the database")
#     db_connection = mysql.connector.connect(
#         host="127.0.0.1",
#         user="root",
#         password="12345678",
#         database="smdb"
#     )
#     print("Connection established!")
#     return db_connection


# @app.route('/insert_data', methods=['POST'])
# def insert_data():
#     conn = connect_to_db()
#     cursor = conn.cursor()
#     data = request.get_json()
#     print(f"Requested data is {data}")
#     # value1 = data['value1']
#     # value2 = data['value2']
        
#     # sql_insert = "INSERT INTO device (column1, column2) VALUES (%s, %s)"
#     sql_insert = "INSERT INTO user (user_id, user_name, email_id, phone_number, first_name, last_name, created_at, updated_at, gender, date_of_birth, profile_image, bio, is_verified, is_active, is_reported) \
#                     VALUES ('7454c97a-dd6a-41ae-bfde-6abea2e06e00', 'Prudhviii', 'adventure.seeker@example.com', '1234567890', 'John', 'Doe', '2023-01-01 12:00:00', '2023-01-01 12:00:00', 'Male', '1990-01-15', 'profile_img1.jpg', 'Exploring the world one adventure at a time.', true, true, false)"
        
#     # data = (value1, value2)
#     # cursor.execute(sql_insert, data)
#     cursor.execute(sql_insert)

#     conn.commit()
#     print("data inserted!")

#     cursor.close()
#     conn.close()

#     return 'Data inserted successfully'


# @app.route('/update_data', methods=['POST'])
# def update_data():
#     db_connection = mysql.connector.connect(
#         host="localhost",
#         user="username",
#         password="password",
#         database="database_name"
#     )

#     cursor = db_connection.cursor()

#     data = request.get_json()
#     value1 = data['value1']
#     value2 = data['value2']
#     id = data['id']

#     sql_update = "UPDATE table_name SET column1 = %s, column2 = %s WHERE id = %s"
#     data = (value1, value2, id)
#     cursor.execute(sql_update, data)

#     db_connection.commit()

#     cursor.close()
#     db_connection.close()

#     return 'Data updated successfully'


# @app.route('/delete_data', methods=['POST'])
# def delete_data():
#     db_connection = mysql.connector.connect(
#         host="localhost",
#         user="username",
#         password="password",
#         database="database_name"
#     )

#     cursor = db_connection.cursor()

#     data = request.get_json()
#     id = data['id']

#     sql_delete = "DELETE FROM table_name WHERE id = %s"
#     data = (id,)
#     cursor.execute(sql_delete, data)

#     db_connection.commit()

#     cursor.close()
#     db_connection.close()

#     return 'Data deleted successfully'


# if __name__ == '__main__':
#     app.run(debug=True)

# this was initial main file