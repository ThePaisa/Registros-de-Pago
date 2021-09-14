class ModeloLogin():
    
    def __init__(self, conn): # se recibe como parametro la conexion en el constructor de la clase MODELO
        self.miconexion= conn    #almacena la base de datos en miconexion
        with self.miconexion.cursor() as cursor: #creamos el cursor y ejecutamos sentencia sql para crear tabla user
            sql= """ CREATE TABLE IF NOT EXISTS cliente
                    (usuario VARCHAR (21) NOT NULL,
                      contrasena VARCHAR (191) NOT NULL)"""  #campos donde iran el usuario y contra correcto
            cursor.execute(sql)
            self.miconexion.commit()
            
    def Traedatos(self, n_usuario, n_contrasena): #lleva datos al constructor de la base de datos, y la tabla login
   
        with self.miconexion.cursor() as cursor:                                                                    #creamos el cursor y ejecutamos sentencia sql para crear tabla user
            sql= """ SELECT usuario, usuario FROM cliente WHERE usuario= %s AND contrasena= %s"""                                                                                                  #SELECT nos trae la tablalogin con su usuario y contraseña
            cursor.execute(sql, (n_usuario,n_contrasena)) 
            datos= cursor.fetchone() #guarda y envia datos ingresados a datos
            return datos  #regresa lo que lleno el usuario en User y Contrasena