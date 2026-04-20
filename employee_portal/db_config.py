import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host="127.0.0.2",
        user="root",
        password="1234",
        database="employee_portal"
    )