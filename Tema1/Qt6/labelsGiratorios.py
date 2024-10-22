import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt6.QtCore import QTimer
from math import cos, sin, pi

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.widget1 = QLabel("Hello", self)
        self.widget2 = QLabel("Hello", self)

        font = self.widget1.font()
        font.setPointSize(30)
        self.widget1.setFont(font)
        self.widget2.setFont(font)

        self.resize(800, 600)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.move_widgets)
        self.timer.start(30)

        self.angle = 0

    def move_widgets(self):
        window_width = self.width()
        window_height = self.height()

        radius = min(window_width, window_height) // 2 - 100
        radians = self.angle * (pi / 180)

        center_x = window_width // 2
        center_y = window_height // 2

        x1 = int(center_x + radius * cos(radians))
        y1 = int(center_y + radius * sin(radians))

        x2 = int(center_x + radius * cos(radians + pi))
        y2 = int(center_y + radius * sin(radians + pi))

        self.widget1.move(x1, y1)
        self.widget2.move(x2, y2)

        self.angle = (self.angle + 2) % 360

app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec()