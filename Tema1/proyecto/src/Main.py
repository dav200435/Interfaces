from PyQt6.QtWidgets import QApplication
from Login import Login

if __name__ == '__main__':
    app = QApplication([])
    window = Login()
    window.show()
    app.exec()
