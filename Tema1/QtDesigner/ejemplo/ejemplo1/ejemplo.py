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
        self.bt_saludar = self.findChild(QtWidgets.QPushButton, 'actionButton')
        self.bt_saludar.clicked.connect(self.funcion)
        
        self.progressBar.setMinimum(0)
        self.progressBar.setMaximum(100)
        
        self.progressBar.setValue(0)
        
        
    def funcion(self):
        if self.label.text() == "":
            self.label.setText("Hola clase")
        else:
            self.label.setText("")
        value=1
        while int(self.progressBar.value()) != self.progressBar.maximum:
            self.progressBar.setValue(value)
            value+=1
            time.sleep(0.1)
            


# se crea la instancia de la aplicación
app = QtWidgets.QApplication(sys.argv)
# se crea la instancia de la ventana
miVentana = Ventana()
# se muestra la ventana 
miVentana.show()
# se entrega el control al sistema operativo
sys.exit(app.exec())