import sys
import os
miDirectorio= os.getcwd()
sys.path.append(miDirectorio) 

from Controlador.ControladorVender import ControladorVender
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Principal2(object):
    
    def __init__(self):
        self.vender_producto= ControladorVender(self)
        
    def setupUi(self, Principal2):
        Principal2.setObjectName("Principal2")
        Principal2.resize(384, 439)
        self.centralwidget = QtWidgets.QWidget(Principal2)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(150, 20, 121, 31))
        font = QtGui.QFont()
        font.setFamily("High Tower Text")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(110, 80, 81, 16))
        font = QtGui.QFont()
        font.setFamily("High Tower Text")
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 120, 191, 16))
        font = QtGui.QFont()
        font.setFamily("High Tower Text")
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(100, 160, 111, 16))
        font = QtGui.QFont()
        font.setFamily("High Tower Text")
        font.setPointSize(15)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 190, 211, 16))
        font = QtGui.QFont()
        font.setFamily("High Tower Text")
        font.setPointSize(15)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(90, 230, 101, 16))
        font = QtGui.QFont()
        font.setFamily("High Tower Text")
        font.setPointSize(15)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(110, 270, 81, 16))
        font = QtGui.QFont()
        font.setFamily("High Tower Text")
        font.setPointSize(15)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.txt_cedula = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_cedula.setGeometry(QtCore.QRect(200, 80, 113, 20))
        self.txt_cedula.setObjectName("txt_cedula")
        self.txt_ncliente = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_ncliente.setGeometry(QtCore.QRect(200, 120, 113, 20))
        self.txt_ncliente.setObjectName("txt_ncliente")
        self.txt_telefono = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_telefono.setGeometry(QtCore.QRect(210, 160, 113, 20))
        self.txt_telefono.setObjectName("txt_telefono")
        self.txt_nproducto = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_nproducto.setGeometry(QtCore.QRect(210, 190, 113, 20))
        self.txt_nproducto.setObjectName("txt_nproducto")
        self.txt_cantidad = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_cantidad.setGeometry(QtCore.QRect(210, 230, 113, 20))
        self.txt_cantidad.setObjectName("txt_cantidad")
        self.txt_precio = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_precio.setGeometry(QtCore.QRect(200, 270, 113, 20))
        self.txt_precio.setObjectName("txt_precio")
        self.btn_crear = QtWidgets.QPushButton(self.centralwidget)
        self.btn_crear.setGeometry(QtCore.QRect(180, 330, 75, 23))
        self.btn_crear.setObjectName("btn_crear")
        Principal2.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Principal2)
        self.statusbar.setObjectName("statusbar")
        Principal2.setStatusBar(self.statusbar)

        self.retranslateUi(Principal2)
        QtCore.QMetaObject.connectSlotsByName(Principal2)
        
        #---------------------- dando accion a los botones----------------------------------------------
        x1=self.txt_cantidad
        x2= self.txt_precio
        
        self.vender= self.btn_crear.clicked.connect(lambda: self.vender_producto.CrearVenta(self.txt_cedula.text(), self.txt_ncliente.text(), self.txt_telefono.text(), self.txt_cantidad.text(), self.txt_precio.text(),Principal2))






        #-----------------------fin de los eventos------------------------------------------------------

    def retranslateUi(self, Principal2):
        _translate = QtCore.QCoreApplication.translate
        Principal2.setWindowTitle(_translate("Principal2", "Vender"))
        self.label.setText(_translate("Principal2", "VENDER"))
        self.label_2.setText(_translate("Principal2", "Cedula :"))
        self.label_3.setText(_translate("Principal2", "Nombre del Cliente :"))
        self.label_4.setText(_translate("Principal2", "Telefono :"))
        self.label_5.setText(_translate("Principal2", "Nombre Producto :"))
        self.label_6.setText(_translate("Principal2", "Cantidad :"))
        self.label_7.setText(_translate("Principal2", "Precio :"))
        self.btn_crear.setText(_translate("Principal2", "Crear"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Principal2 = QtWidgets.QMainWindow()
    ui = Ui_Principal2()
    ui.setupUi(Principal2)
    Principal2.show()
    sys.exit(app.exec_())
