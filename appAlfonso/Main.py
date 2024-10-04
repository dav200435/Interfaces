import sys
import os
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication,
    QPushButton,
    QWidget,
    QLineEdit,
    QGridLayout,
    QVBoxLayout,
    QLabel
)

class Calculadora(QWidget):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculadora")
        self.operado=False
        self.resultado = QLabel()
        self.mainPantalla=QVBoxLayout()
        self.resultado.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.pantalla = QGridLayout()
        self.mainPantalla.addWidget(self.resultado)
        self.setButtons()
        self.setLayout(self.mainPantalla)
        
        self.mainPantalla.addLayout(self.pantalla)
        
    def setButtons(self):
        
        calculos=["+","-","*","/"]
        numero = 1
        for i in range(1, 4):
            for j in range(0, 3):
                boton = QPushButton(str(numero))
                self.pantalla.addWidget(boton, i, j)
                boton.clicked.connect(self.pressButton)
                numero += 1
        boton=QPushButton("0")
        self.pantalla.addWidget(boton, 4, 1)
        boton.clicked.connect(self.pressButton)
        boton.setShortcut("0")
        
        for i, operador in enumerate(calculos):
            if i == 3:
                boton=QPushButton(operador)
                self.pantalla.addWidget(boton, i + 1, 2)
                boton.clicked.connect(self.pressButton)
                boton.setShortcut(f"{str(i + 1)}")
            else:    
                boton=QPushButton(operador)
                self.pantalla.addWidget(boton, i + 1, 3)
                boton.clicked.connect(self.pressButton)
                boton.setShortcut(f"{str(i + 1)}")
        boton=QPushButton("=")
        self.pantalla.addWidget(boton, 4, 3)
        boton.clicked.connect(self.pressButton)
        boton.setShortcut("intro")
        boton=QPushButton(".")
        self.pantalla.addWidget(boton, 4, 0)
        boton.clicked.connect(self.pressButton)
        boton.setShortcut(".")
        boton=QPushButton("cls")
        self.pantalla.addWidget(boton,0,5)
        boton.clicked.connect(self.pressButton)
        boton.setShortcut("esc")
        
    def pressButton(self):
        calculos=["+","-","*","/"]
        sender = self.sender()
        try:
            if self.operado:
                self.resultado.setText("")
                self.operado=False
                
            if sender.text() in calculos:
                self.num1=self.resultado.text()
                self.operacion=sender.text()
                self.resultado.setText("")
            elif sender.text()=="=":
                self.num2=self.resultado.text()
                self.resultado.setText(str(eval(f"{self.num1}{self.operacion}{self.num2}")))
                self.operado=True
            elif sender.text()=="cls":
                self.num1=""
                self.operacion=""
                self.num2=""
                self.resultado.setText("")
            else:
                self.resultado.setText(self.resultado.text()+sender.text())
        except Exception as e:
            self.resultado.setText(str(e))
            self.operado=True
            
            

if __name__ == "__main__":
    os.environ["QT_ENABLE_HIGHDPI_SCALING"]   = "1"
    os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    os.environ["QT_SCALE_FACTOR"]             = "1"
    app = QApplication(sys.argv)
    calc = Calculadora()
    calc.show()
    sys.exit(app.exec())