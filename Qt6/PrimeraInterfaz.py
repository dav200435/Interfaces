import sys
import random
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton

def move_window():
    screen_geometry = app.primaryScreen().geometry()
    screen_width = screen_geometry.width()
    screen_height = screen_geometry.height()

    random_x = random.randint(0, screen_width - window.width())
    random_y = random.randint(0, screen_height - window.height())

    window.move(random_x, random_y)

class MovingButton(QPushButton):
    def enterEvent(self, event):
        move_window()
        super().enterEvent(event)

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("window")

button = MovingButton("Try To Push Me!", window)
button.setGeometry(50, 30, 100, 40)

window.resize(200, 100)
window.show()

sys.exit(app.exec())