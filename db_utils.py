# Importing the MySQL Connector module for establishing a connection to the database
import mysql.connector

def connect_to_db():
    """
    Function to establish a connection to the Social Media Database.

    Returns:
    - db_connection (mysql.connector.connection.MySQLConnection): A connection object to the database.
    """
    # Printing a message indicating the start of the connection process
    print("Connecting to the Social Media Database")
    
    # Creating a MySQL database connection
    db_connection = mysql.connector.connect(
        host="127.0.0.1",    # Database host address
        user="root",         # Database username
        password="12345678",  # Database password
        database="smdb"       # Database name
    )
    
    # Printing a message indicating the successful establishment of the connection
    print("Connection Established!")
    
    # Returning the connection object
    return db_connection
