import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QVBoxLayout, QWidget
from PyQt6.QtGui import QPalette, QColor, QPixmap

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Window")
        label =QLabel("Hello")
        pixmap = QPixmap("gato.jpg")
        label.setPixmap(pixmap)
        self.setCentralWidget(label)
        self.resize(pixmap.height(),pixmap.height())
        
        



app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec()