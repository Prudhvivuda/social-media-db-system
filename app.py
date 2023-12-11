# Importing the Flask class from the flask module
from flask import Flask

# Importing functions for data operations, queries, and views
from data_operations.insert import insert_data
from data_operations.delete import delete_data
from data_operations.update import update_data
from queries.parser import parse_query
from views.parser import parse_views

# Creating a Flask web application instance
app = Flask(__name__)

# Defining route for inserting data
@app.route('/insert_data', methods=['POST'])
def insert_data_route():
    """
    Endpoint for inserting data into the database.

    Returns:
    - response (str): A string indicating the success or failure of the data insertion.
    """
    return insert_data()

# Defining route for updating data
@app.route('/update_data', methods=['POST'])
def update_data_route():
    """
    Endpoint for updating data in the database.

    Returns:
    - response (str): A string indicating the success or failure of the data update.
    """
    return update_data()

# Defining route for deleting data
@app.route('/delete_data', methods=['POST'])
def delete_data_route():
    """
    Endpoint for deleting data from the database.

    Returns:
    - response (str): A string indicating the success or failure of the data deletion.
    """
    return delete_data()

# Defining route for querying data
@app.route('/query/<query_type>', methods=['POST'])
def query_data_route(query_type):
    """
    Endpoint for executing queries on the database.

    Args:
    - query_type (str): The type of query to be executed.

    Returns:
    - response (str): A string containing the result of the executed query.
    """
    return parse_query(query_type)

# Defining route for fetching views data
@app.route('/views/<query_type>', methods=['GET'])
def views_data_route(query_type):
    """
    Endpoint for fetching data based on predefined views.

    Args:
    - query_type (str): The type of view to be fetched.

    Returns:
    - response (str): A string containing the result of the fetched view.
    """
    return parse_views(query_type)

# Running the Flask application if the script is executed directly
if __name__ == '__main__':
    app.run(debug=True)
