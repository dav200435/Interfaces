import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget,
QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QGridLayout, QPushButton)
from PyQt6.QtGui import QPalette, QColor


class Color(QWidget):

    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)
        
class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")

        vertical_layout = QVBoxLayout()

        horizontal_layout = QHBoxLayout()

        horizontal_layout.addWidget(QPushButton("Botón 1"))
        horizontal_layout.addWidget(QPushButton("Botón 2"))
        horizontal_layout.addWidget(QPushButton("Botón 3"))

        vertical_layout.addLayout(horizontal_layout)

        vertical_layout.addWidget(Color('yellow'))

        widget = QWidget()
        widget.setLayout(vertical_layout)
        self.setCentralWidget(widget)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
