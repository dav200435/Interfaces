import sys
from PyQt6 import QtWidgets, uic
import time

#importamos las librerías necesarias
import sys
from PyQt6 import QtWidgets, uic

#Carga la interfaz gráfica y conecta los botones
class Ventana(QtWidgets.QMainWindow):
    '''Esta es la clase principal'''
    #Inicializamos la ventana y conectamos los botones
    def __init__(self, padre=None):
        #Inicializa la ventana
        QtWidgets.QMainWindow.__init__(self, padre)
        uic.loadUi("ejemplo.ui",self) #Lee el archivo de QtDesigner
        
        #Conectar botón a función
        self.botonA = self.findChild(QtWidgets.QPushButton, 'botonA')
        self.botonA.clicked.connect(self.funcionA)
        self.botonB = self.findChild(QtWidgets.QPushButton, 'botonB')
        self.botonB.clicked.connect(self.funcionB)
        
        self.textA = self.findChild(QtWidgets.QLabel, 'TextA')
        self.textA.setText("")
        self.textB = self.findChild(QtWidgets.QLabel, 'TextB')
        self.textB.setText("")
        
    def funcionB(self):
        if self.textB.text() == "":
            self.textB.setText("Hola clase")
        else:
            self.textB.setText("")
        
    def funcionA(self):
        if self.textA.text() == "":
            self.textA.setText("¿Que tal?")
        else:
            self.textA.setText("")


# se crea la instancia de la aplicación
app = QtWidgets.QApplication(sys.argv)
# se crea la instancia de la ventana
miVentana = Ventana()
# se muestra la ventana 
miVentana.show()
# se entrega el control al sistema operativo
sys.exit(app.exec())