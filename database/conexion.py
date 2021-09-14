"""" aqui creamos la funcion que nos otorga la conexion con la base de datos"""

import pymysql

def connection():
     conn= pymysql.connect(
          host="localhost", port=3306, user="root", password="", db="miconexion_bd"
     )
     print("conexion exitosa a la base de datos")
     return conn