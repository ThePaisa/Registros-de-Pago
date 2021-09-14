
import sys
import os 
miDirectorio= os.getcwd()
sys.path.append(miDirectorio)

from PyQt5 import QtWidgets

from database.conexion import connection  # traemos la funcion que contiene mi conexion a la base de datos
from Modelo.login import ModeloLogin #traemos la clase Modelo que recibe la conexion cuando se ejecuta su constructor 
#tambien apartir de este momento se crea la tabla en la base de datos gracias al constructor de la clase Login que realizo la sentencia sql

""" con las lineas anteriores tengo la conexion a la base de datos, 
las herramientas de pyqt5 e importo del modelo la clase login del archivo login"""



class LoginControlador():
    
    def __init__(self, interfaz_login):  #para ejecutarse necesita un parametro, en las vistas/vista_login dentro de su clase que hace referencia a la interfaz_login creamos un constructor que invoque la clase LoginControlador actual, alli se ejecuta este constructor recibiendo ""self", que se traduce en recibir todos los componentes de la clase de donde se le invoca, osea la interfaz login.
        self.login= ModeloLogin(connection())    # traigo conexion a la base de datos y la almaceno en login
        self.Interfaz_login= interfaz_login   # En esta variable almacenamos la interfaz login#
                                                #este constructor se activa cuando se instancia la clase del controlador, genera la conexion con la base de datos y con la interfazdatetime A combination of a date and a time. Attributes: () 
                                                #el controlador pide Vistalogin para poder acceder a dicha interfaz con sus funciones 
         
    def LogIn(self, n_usuario, n_contrasena, Ui_Principal, Ui_Login ):     #el nombre del objeto es el mismo que en PYQT5
        
        if n_usuario and n_contrasena: #si los usuarios ingresados existen entonces
            datos = self.login.Traedatos(n_usuario, n_contrasena) #en login se almacena toda la informacion de la clase Modelo
           
            if datos:  #si el usuario ingresado existe en la base de datos entonces
                
                Ui_Login.hide() #escondemos interfaz login
                self.Interfaz_login.Form= QtWidgets.QMainWindow() #creamos nueva interfaz en blanco
                self.Interfaz_login.ui= Ui_Principal() #llamamos la variable que contiene la interfaz login y la cambiamos por la nueva interfaz a mostrar
                self.Interfaz_login.ui.setupUi(self.Interfaz_login.Form) #mediante el comando setup ingresamos la nueva ventana para que almacene los datos de laventana a mostrar
                self.Interfaz_login.Form.show()
                
                print("los datos ingresados son correctos")
            else:
                print("DATOS INCORRECTOS, No se puede ingresar al sistema")
 
            
                
            
        
        
        
