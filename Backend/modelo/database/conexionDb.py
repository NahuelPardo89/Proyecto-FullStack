import mysql.connector
from mysql.connector import Error 


class Conexion:
    def __init__(self):
        self.connection=""
        try:
            connection=mysql.connector.connect(host='localhost',database='ampaDB',user='root',password='copado34414604')
            if connection.is_connected():
                    db_Info=connection.get_server_info()
                    print("Connected to MySQL Server version", db_Info)
                    self.connection=connection
                    
        except Error as e:
            print ("Error while connecting to MySQL", e)
    
