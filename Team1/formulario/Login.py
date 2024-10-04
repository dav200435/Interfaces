import sys
from PyQt6.QtWidgets import (
    QPushButton,
    QWidget,
    QLineEdit,
    QGridLayout,
    QLabel,
    QApplication,
    QMessageBox
)

class Login(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login")
        self.mainLayout = QGridLayout()
        self.setItems()
        self.setLayout(self.mainLayout)

    def setItems(self):
        #seteo items username
        textUsername = QLabel(text="Nombre de usuario")
        self.mainLayout.addWidget(textUsername, 0, 0, 1, 2)
        self.username = QLineEdit()
        self.mainLayout.addWidget(self.username, 1, 0, 1, 2)
        #seteo items passwd
        textPasswd = QLabel(text="Contraseña")
        self.mainLayout.addWidget(textPasswd, 2, 0, 1, 2)
        self.passwd = QLineEdit()
        self.passwd.setEchoMode(QLineEdit.EchoMode.Password)
        self.mainLayout.addWidget(self.passwd, 3, 0, 1, 2)
        #hago boton para ver contraseña
        self.toggleButton = QPushButton("Mostrar")
        self.toggleButton.setCheckable(True)
        self.toggleButton.toggled.connect(self.toggle_password)
        self.mainLayout.addWidget(self.toggleButton, 3, 3, 1, 1)
        #hago boton enviar
        self.send=QPushButton("enviar")
        self.send.clicked.connect(self.sendForm)
        self.mainLayout.addWidget(self.send)

    def toggle_password(self, checked):
        #funcion para mostrar u ocultar contraseña
        if checked:
            #mostrar texto
            self.passwd.setEchoMode(QLineEdit.EchoMode.Normal)
            self.toggleButton.setText('Ocultar')
        else:
            #ocultar texto
            self.passwd.setEchoMode(QLineEdit.EchoMode.Password)
            self.toggleButton.setText('Mostrar')

    def sendForm(self):
        data={}
        data['username']=self.username.text()
        data['password']=self.passwd.text()
        
        if data['username']!='' and data['password']!='':
            self.username.setText('')
            self.passwd.setText('')
            self.printData(data)
            self.check(data)
        
        
    def printData(self,data):
        for dato, value in data.items():
            print(f"{dato} = {value}")
            
    def check(self,data):
        mensaje = QMessageBox()
        mensaje.setWindowTitle("Login success")
        mensaje.setText(f"Bienvenido {data['username']}")
        mensaje.setIcon(QMessageBox.Icon.Information)
        mensaje.setStandardButtons(QMessageBox.StandardButton.Ok)
        
        mensaje.exec()
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Login()
    window.show()
    sys.exit(app.exec())