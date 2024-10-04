import sys
import random
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget,
QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QGridLayout, QPushButton, QStackedLayout)
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
        horizontal_layout2 = QHBoxLayout()

        horizontal_layout.addWidget(QPushButton("Botón 1"))
        horizontal_layout.addWidget(QPushButton("Botón 2"))
        horizontal_layout.addWidget(QPushButton("Botón 3"))

        vertical_layout.addWidget(Color('yellow'))

        widget = QWidget()
        widget.setLayout(vertical_layout)
        self.setCentralWidget(widget)
        
        layoutStacked = QStackedLayout()

        layoutStacked.addWidget(Color("red"))
        layoutStacked.addWidget(Color("green"))
        layoutStacked.addWidget(Color("blue"))
        layoutStacked.addWidget(Color("yellow"))

        layoutStacked.setCurrentIndex(1)
        
        button_red = QPushButton("Red")
        button_green = QPushButton("Green")
        button_blue = QPushButton("Blue")
        button_yellow = QPushButton("Yellow")
        
        button_red.pressed.connect(lambda: layoutStacked.setCurrentIndex(0))
        button_green.pressed.connect(lambda: layoutStacked.setCurrentIndex(1))
        button_blue.pressed.connect(lambda: layoutStacked.setCurrentIndex(2))
        button_yellow.pressed.connect(lambda: layoutStacked.setCurrentIndex(3))
        
        horizontal_layout2.addWidget(button_red)
        horizontal_layout2.addWidget(button_green)
        horizontal_layout2.addWidget(button_blue)
        horizontal_layout2.addWidget(button_yellow)
        
        vertical_layout.addLayout(horizontal_layout)
        vertical_layout.addLayout(layoutStacked)
        vertical_layout.addLayout(horizontal_layout2)

        widget = QWidget()


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
