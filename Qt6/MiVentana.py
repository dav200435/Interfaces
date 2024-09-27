import sys
import random
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Window")
        
        self.button = QPushButton("My Button", self)
        self.button.setCheckable(True)
        self.button.clicked.connect(self.the_button_was_clicked)
        self.button.clicked.connect(self.the_button_was_toggled)

    def the_button_was_clicked(self):
        print("Clicked")
        
    def the_button_was_toggled(self, checked):
        print("checked? ",checked)
        
        if checked:
            self.var=random.randint(0,100)
            print(self.var)
        



app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec()