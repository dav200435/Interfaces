# Login.py

from PyQt6.QtWidgets import QMainWindow, QLineEdit, QCheckBox, QPushButton, QDialog
from PyQt6 import uic
from abc import abstractmethod
from LoginDialog import LoginDialog

class Login(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Inventario")
        uic.loadUi("./Windows/LogIn.ui", self)
        self.user = self.findChild(QLineEdit, 'User')
        self.passwd = self.findChild(QLineEdit, 'Passwd')
        self.passwd.setEchoMode(QLineEdit.EchoMode.Password)
        
        self.checkbox = self.findChild(QCheckBox, 'checkBox')
        self.checkbox.clicked.connect(self.togglePassword)
        
        self.login = self.findChild(QPushButton, 'pushButton')
        self.login.clicked.connect(self.loginSucces)
        
    def togglePassword(self, checked):
        if checked:
            self.passwd.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self.passwd.setEchoMode(QLineEdit.EchoMode.Password)
    
    def loginSucces(self):
        user_text = self.user.text()
        passwd_text = self.passwd.text()

        if user_text and passwd_text:
            dlg = LoginDialog(self)
            dlg.success(user_text)
            if dlg.exec() == QDialog.DialogCode.Accepted:
                from Manager import Manager
                self.mng = Manager(self)
                self.mng.show()
                self.hide()
                self.user.setText("")
                self.passwd.setText("")
        else:
            dlg = LoginDialog(self)
            dlg.failed()
            dlg.exec()
            self.passwd.setText('')
            self.user.setText('')

    @abstractmethod
    def logout(self):
        self.show()
