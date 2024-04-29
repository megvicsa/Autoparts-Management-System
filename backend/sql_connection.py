import mysql.connector 

__cnx = None

def get_sql_connection():
    global __cnx
    cnx = mysql.connector.connect(user='root', password='m3g1-1n@', host='127.0.0.1', database='CS348-Information-System')

    return cnx
