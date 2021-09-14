import sys
import os
miDirectorio= os.getcwd()
sys.path.append(miDirectorio) 
from database.conexion import connection 
from Modelo.registros import Registros

class ControladorVender():
    def __init__(self, Ui_principal2):
        self.product= Registros(connection())    #poner el mismo nombre del otro controlador si genera error
        self.vista_principal2= Ui_principal2
    
    def CrearVenta(self,cedula, nombre, telefono, cantidad, precio, vista_vender):
        x1= cantidad
        x2=precio
        q1=float(x1)
        q2=float(x2)
        if cedula and nombre and telefono  and q1 and q2:
            x= q1*q2
            self.product.Vender(cedula, nombre, telefono, x)
            vista_vender.hide()
        
    