import sys
import os
miDirectorio= os.getcwd()
sys.path.append(miDirectorio)

from Controlador.ControladorPrincipal import ControladorPrincipal #importamos el controlador a la vista para tener comunicacion con el
from Vista.vista_vender import Ui_Principal2
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Principal(object):
    
    def __init__(self):
        self.controlador_principal= ControladorPrincipal(self) #instancia de la clase del Controlador principal (recordar los parentesis y el self) 
    
    def setupUi(self, Principal):
        Principal.setObjectName("Principal")
        Principal.resize(492, 331)
        self.centralwidget = QtWidgets.QWidget(Principal)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(110, 20, 331, 16))
        font = QtGui.QFont()
        font.setFamily("High Tower Text")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(150, 50, 331, 16))
        font = QtGui.QFont()
        font.setFamily("High Tower Text")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.tabla_registrosBD = QtWidgets.QTableWidget(self.centralwidget)
        self.tabla_registrosBD.setGeometry(QtCore.QRect(30, 80, 421, 151))
        self.tabla_registrosBD.setRowCount(3)
        self.tabla_registrosBD.setObjectName("tabla_registrosBD")
        self.tabla_registrosBD.setColumnCount(4)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_registrosBD.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_registrosBD.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_registrosBD.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_registrosBD.setHorizontalHeaderItem(3, item)
        self.btn_vender = QtWidgets.QPushButton(self.centralwidget)
        self.btn_vender.setGeometry(QtCore.QRect(40, 260, 75, 23))
        self.btn_vender.setObjectName("btn_vender")
        self.btn_listar = QtWidgets.QPushButton(self.centralwidget)
        self.btn_listar.setGeometry(QtCore.QRect(150, 260, 75, 23))
        self.btn_listar.setObjectName("btn_listar")
        self.btn_eliminar = QtWidgets.QPushButton(self.centralwidget)
        self.btn_eliminar.setGeometry(QtCore.QRect(360, 260, 75, 23))
        self.btn_eliminar.setObjectName("btn_eliminar")
        self.btn_actualizar = QtWidgets.QPushButton(self.centralwidget)
        self.btn_actualizar.setGeometry(QtCore.QRect(250, 260, 75, 23))
        self.btn_actualizar.setObjectName("btn_actualizar")
        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton.setGeometry(QtCore.QRect(450, 0, 41, 19))
        self.toolButton.setObjectName("toolButton")
        Principal.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Principal)
        self.statusbar.setObjectName("statusbar")
        Principal.setStatusBar(self.statusbar)

        self.retranslateUi(Principal)
        QtCore.QMetaObject.connectSlotsByName(Principal)
        
        #---------------------- dando accion a los botones----------------------------------------------


        self.list= self.btn_listar.clicked.connect(lambda: self.controlador_principal.listarRegistros()) 
        self.actualizar= self.btn_actualizar.clicked.connect(lambda: self.controlador_principal.actualizar())
        self.borrar= self.btn_eliminar.clicked.connect(lambda: self.controlador_principal.BorrarCliente())
        self.vender= self.btn_vender.clicked.connect(lambda: self.controlador_principal.VentanaNueva(Ui_Principal2))



#-----------------------fin de los eventos--------------------------------

    def retranslateUi(self, Principal):
        _translate = QtCore.QCoreApplication.translate
        Principal.setWindowTitle(_translate("Principal", "ELECTRORIENTE S.I Registros de Pago "))
        self.label.setText(_translate("Principal", "REGISTROS DE PAGO "))
        self.label_2.setText(_translate("Principal", "ELECTRORIENTE S.I"))
        item = self.tabla_registrosBD.horizontalHeaderItem(0)
        item.setText(_translate("Principal", "CEDULA"))
        item = self.tabla_registrosBD.horizontalHeaderItem(1)
        item.setText(_translate("Principal", "NOMBRE"))
        item = self.tabla_registrosBD.horizontalHeaderItem(2)
        item.setText(_translate("Principal", "TELEFONO"))
        item = self.tabla_registrosBD.horizontalHeaderItem(3)
        item.setText(_translate("Principal", "SALDO A PAGAR"))
        self.btn_vender.setText(_translate("Principal", "Vender"))
        self.btn_listar.setText(_translate("Principal", "Listar"))
        self.btn_eliminar.setText(_translate("Principal", "Eliminar"))
        self.btn_actualizar.setText(_translate("Principal", "Actualizar"))
        self.toolButton.setText(_translate("Principal", "ayuda"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Principal = QtWidgets.QMainWindow()
    ui = Ui_Principal()
    ui.setupUi(Principal)
    Principal.show()
    sys.exit(app.exec_())
