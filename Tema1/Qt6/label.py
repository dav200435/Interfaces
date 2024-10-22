import sys
import random
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QVBoxLayout, QWidget
from PyQt6.QtCore import Qt

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        widget = QLabel("Hello")

        font = widget.font()
        font.setPointSize(30)
        widget.setFont(font)
        widget.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)
        
        widget2 = QLabel("Hello")

        font2 = widget.font()
        font2.setPointSize(30)
        widget2.setFont(font)
        widget2.setAlignment(Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignRight)

        layout.addWidget(widget)
        layout.addWidget(widget2)
        
        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)

app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec()