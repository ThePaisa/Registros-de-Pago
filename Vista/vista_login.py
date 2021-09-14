import sys
import os
miDirectorio= os.getcwd()
sys.path.append(miDirectorio)  #importamos funciones propias del sistema necesarias para el programa

  #asi la vista se comunica con el controlador y el controlador con el modelo#
from Controlador.LoginControlador import LoginControlador

#importamos los archivos de la vista
from PyQt5 import QtCore, QtGui, QtWidgets
from Vista.vista_principal import Ui_Principal

class Ui_Login(object):
    
    
    def __init__(self):
        self.login_controler= LoginControlador(self)   #instanciamos el controlador y le pasamos la vistaLogin que solicita su constructorla cual es self pues hace referencia a la misma clase la cual es la propia vista debido a que estamos en esta claseVistaLogin
        
    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.resize(342, 298)
        self.centralwidget = QtWidgets.QWidget(Login)
        self.centralwidget.setObjectName("centralwidget")
        self.label_login_titulo = QtWidgets.QLabel(self.centralwidget)
        self.label_login_titulo.setEnabled(True)
        self.label_login_titulo.setGeometry(QtCore.QRect(50, 10, 411, 101))
        font = QtGui.QFont()
        font.setFamily("Wide Latin")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(50)
        self.label_login_titulo.setFont(font)
        self.label_login_titulo.setObjectName("label_login_titulo")
        self.label_usuario_titulo = QtWidgets.QLabel(self.centralwidget)
        self.label_usuario_titulo.setGeometry(QtCore.QRect(30, 120, 101, 16))
        font = QtGui.QFont()
        font.setFamily("High Tower Text")
        font.setPointSize(15)
        self.label_usuario_titulo.setFont(font)
        self.label_usuario_titulo.setObjectName("label_usuario_titulo")
        self.label_contrasena_titulo = QtWidgets.QLabel(self.centralwidget)
        self.label_contrasena_titulo.setGeometry(QtCore.QRect(10, 180, 111, 16))
        font = QtGui.QFont()
        font.setFamily("High Tower Text")
        font.setPointSize(15)
        self.label_contrasena_titulo.setFont(font)
        self.label_contrasena_titulo.setObjectName("label_contrasena_titulo")
        self.txt_usuario = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_usuario.setGeometry(QtCore.QRect(120, 120, 171, 20))
        self.txt_usuario.setObjectName("txt_usuario")
        self.txt_contrasena = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_contrasena.setGeometry(QtCore.QRect(120, 180, 171, 20))
        self.txt_contrasena.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txt_contrasena.setObjectName("txt_contrasena")
        self.btn_entrar = QtWidgets.QPushButton(self.centralwidget)
        self.btn_entrar.setGeometry(QtCore.QRect(130, 240, 101, 31))
        font = QtGui.QFont()
        font.setFamily("High Tower Text")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btn_entrar.setFont(font)
        self.btn_entrar.setObjectName("btn_entrar")
        Login.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Login)
        self.statusbar.setObjectName("statusbar")
        Login.setStatusBar(self.statusbar)

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

#---------------------- dando accion a los botones----------------------------------------------


        self.logeo= self.btn_entrar.clicked.connect(lambda: self.login_controler.LogIn(self.txt_usuario.text(), self.txt_contrasena.text(), Ui_Principal, Login)) #Mediante la variable que instancio la clase del Controlador, instanciamos la funcion que recibe usuario y contraseña,<logincontrolador> y como todo esta conectado mediante los parametros anteriores funciona el registro si se ingresa texto






#-----------------------fin de los eventos------------------------------------------------------

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "Inicio de Sesion"))
        self.label_login_titulo.setText(_translate("Login", "INICIAR SESION "))
        self.label_usuario_titulo.setText(_translate("Login", "Usuario :"))
        self.label_contrasena_titulo.setText(_translate("Login", "Contraseña :"))
        self.txt_usuario.setPlaceholderText(_translate("Login", " Usuario"))
        self.txt_contrasena.setPlaceholderText(_translate("Login", " Contraseña"))
        self.btn_entrar.setText(_translate("Login", "Entrar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Login = QtWidgets.QMainWindow()
    ui = Ui_Login()
    ui.setupUi(Login)
    Login.show()
    sys.exit(app.exec_())
