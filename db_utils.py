import mysql.connector

def connect_to_db():
    
    print("Connecting to the Social Media Database")
    
    db_connection = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="12345678",
        database="smdb"
    )
    
    print("Connection Established!")
    
    return db_connection
