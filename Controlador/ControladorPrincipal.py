import sys
import os
miDirectorio= os.getcwd()
sys.path.append(miDirectorio) 
 
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox

from database.conexion import connection 
from Modelo.registros import Registros

class ControladorPrincipal():
    
    def __init__ (self, interfaz_principal): 
        self.registros= Registros(connection())
        self.vista_principal=interfaz_principal
    
    def listarRegistros(self): #funcion que da utilidad al boton Listar de la vista ppal
        tabla_registros= self.vista_principal.tabla_registrosBD   #almaceno tabla de la vista en tabla_registros
        registros= self.registros.obtener_registros() #almaceno los datos de la tabla de MYSQL
        tabla_registros.setRowCount(0)  #setear contador de filas en 0 (pyqt5 propiedad)
        for numero_fila, datos_fila in enumerate(registros):
            tabla_registros.insertRow(numero_fila)
            for numero_columna, datos_columna in enumerate(datos_fila):
                tabla_registros.setItem(numero_fila, numero_columna, QtWidgets.QTableWidgetItem(str(datos_columna)))
        
    def actualizar(self):
        tabla_registro= self.vista_principal.tabla_registrosBD
        registros= []
        fila= []
        for numero_fila in range (tabla_registro.rowCount()):
            for numero_columna in range (tabla_registro.columnCount()):
                if tabla_registro.item(numero_fila, numero_columna) != None:
                    fila.append(tabla_registro.item(numero_fila, numero_columna).text())
            if len(fila)>0:
                registros.append(fila)
            fila=[]
        if len(registros)>0:
            for cliente in registros:  #por cada cliente en registros
                self.registros.ActualizarRegistros(cliente[0],cliente[1],cliente[2],cliente[3])   #instancia de la clase mediante variable "registros" que almacena la clase constructor del modelo
        
        self.listarRegistros()
                
                
    def BorrarCliente(self):
        tabla_registro= self.vista_principal.tabla_registrosBD
        if tabla_registro.currentItem() != None:
            cedula= tabla_registro.currentItem().text()
            registro= self.registros.obtener_registros()    
            if registro:
                self.registros.BorrarRegistro(cedula) 
        self.listarRegistros 
    
    
    def VentanaNueva(self, Ui_Principal2):
        self.vista_principal.Form= QtWidgets.QMainWindow()
        self.vista_principal.ui= Ui_Principal2()
        self.vista_principal.ui.setupUi(self.vista_principal.Form)
        self.vista_principal.Form.show()
                       
        
        