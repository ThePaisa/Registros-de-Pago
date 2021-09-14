class Registros():
    
    def __init__(self, conn): # se recibe como parametro la conexion en el constructor de la clase MODELO
        self.miconexion= conn    #almacena la base de datos en miconexion
        with self.miconexion.cursor() as cursor: #creamos el cursor y ejecutamos sentencia sql para crear tabla user
            sql= """ CREATE TABLE IF NOT EXISTS registros
                    (Cedula VARCHAR (21) NOT NULL PRIMARY KEY,
                      Nombre VARCHAR (191) NOT NULL,
                      Telefono VARCHAR (50) NOT NULL,
                      SALDO FLOAT (50) NOT NULL)""" #campos donde iran el usuario y contra correcto
            cursor.execute(sql)
            self.miconexion.commit()
            
    def obtener_registros(self):
        with self.miconexion.cursor() as cursor:                                 #creamos el cursor y ejecutamos sentencia sql para crear tabla use                           #creamos el cursor y ejecutamos sentencia sql para crear tabla user
            sql= """ SELECT * FROM registros""" #selecciono todo lo almacenado en la tabla registros
            cursor.execute(sql)
            result= cursor.fetchall()
            return result
    
    def ActualizarRegistros(self, cedula, nombre, telefono, saldo):
        with self.miconexion.cursor() as cursor:
            sql= """UPDATE registros SET nombre= %s, telefono= %s, saldo= %s WHERE cedula= %s"""
            cursor.execute(sql, (nombre, telefono, saldo, cedula))
            self.miconexion.commit()
    
    def BorrarRegistro(self, cedula):
        with self.miconexion.cursor() as cursor:
            sql= """DELETE FROM registros WHERE cedula= %s"""
            cursor.execute(sql,(cedula))
            self.miconexion.commit()
    
    
    def Vender(self, cedula, nombre, telefono,x):
        with self.miconexion.cursor() as cursor:
            sql= """INSERT INTO registros (Cedula, Nombre, Telefono, SALDO ) VALUES (%s, %s,%s, %s)"""
            sql2= """ SELECT Cedula COUNT (Cedula) FROM registros GROUP BY 1 HAVING COUNT(*)>1"""                                                                                                    # IF NOT EXISTS (SELECT 1 FROM registros WHERE URL= "Cedula") """
            cursor.execute(sql, (cedula, nombre, telefono, x))
            
               #si la cedula se repite entonces permitir q ignore el duplicado y sumarle a saldo el valor actual  
            self.miconexion.commit()
    
    def Multiplicar(self, cantidad, precio):
        if cantidad and precio:
            x= cantidad*precio
            return x   
        