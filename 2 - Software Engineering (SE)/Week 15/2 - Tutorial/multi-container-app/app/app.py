from flask import Flask, jsonify
import mysql.connector
import os
from env_variables import *

app = Flask(__name__)

@app.route('/')
def index():
    return {"message":"This is a test"}

@app.route('/data', methods=["GET"])
def get_data():
    connection = mysql.connector.connect(
        host=HOST_DB,
        port=DB_PORT,
        user=ADMIN_USER,
        password=os.getenv('MYSQL_ROOT_PASSWORD'),
        database=DB_NAME,
    )
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM {TABLE_NAME}")
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=FLASK_PORT)