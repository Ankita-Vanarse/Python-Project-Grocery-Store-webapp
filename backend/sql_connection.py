import mysql.connector
import datetime

__cnx = None


def get_sql_connection():
    print("opening mysql connection")
    global __cnx

    if __cnx is None:
        __cnx = mysql.connector.connect(
                user='root',
                host="localhost",
                password="1234",
                database='gs')
    return __cnx

