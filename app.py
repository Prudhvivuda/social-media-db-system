from flask import Flask
from data_operations.insert import insert_data
from data_operations.delete import delete_data
from data_operations.update import update_data

app = Flask(__name__)

@app.route('/insert_data', methods=['POST'])
def insert_data_route():
    return insert_data()

@app.route('/update_data', methods=['POST'])
def update_data_route():
    return update_data()

@app.route('/delete_data', methods=['POST'])
def delete_data_route():
    return delete_data()

if __name__ == '__main__':
    app.run(debug=True)
