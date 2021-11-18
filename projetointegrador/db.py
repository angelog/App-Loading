from flask import Flask
from flask_mysqldb import MySQL

app = Flask("JETSOFT")
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '97855818'
app.config['MYSQL_DB'] = 'mydb'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app) 

class DatabaseManager:

    def Insert_Drop(self,query):
        cursor = mysql.connection.cursor()
        cursor.execute(query)
        cursor.connection.commit()

    def Filtrar(self,query):
        cursor=mysql.connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()
