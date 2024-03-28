import mysql.connector as mysql

def connect_db():
    return mysql.connect(
        user='root',
        password='5033677oki',
        host='localhost',
        database='agence'
    )