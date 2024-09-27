import sys
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QApplication, QLabel, QComboBox, QMainWindow, QVBoxLayout, QWidget
from math import cos, sin, pi


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Desplegable")

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.main_layout = QVBoxLayout(self.central_widget)

        self.desplegable = QComboBox()
        self.desplegable.addItems(["Imagen Gato", "Textos Giratorios"])
        self.main_layout.addWidget(self.desplegable)

        self.content_widget = QWidget(self)
        self.content_layout = QVBoxLayout(self.content_widget)
        self.main_layout.addWidget(self.content_widget)

        self.desplegable.currentTextChanged.connect(self.on_option_changed)

        self.widget1 = QLabel("Texto 1", self)
        self.widget2 = QLabel("Texto 2", self)
        font = self.widget1.font()
        font.setPointSize(30)
        self.widget1.setFont(font)
        self.widget2.setFont(font)

        self.angle = 0
        self.timer = None

        # Inicialmente ocultar los textos giratorios
        self.widget1.hide()
        self.widget2.hide()

    def on_option_changed(self, text):
        # Detener el timer si existe y ocultar los textos giratorios
        if self.timer is not None:
            self.timer.stop()
            self.widget1.hide()
            self.widget2.hide()

        # Limpiar el contenido dinámico antes de agregar nuevo contenido
        for i in reversed(range(self.content_layout.count())):
            widget_to_remove = self.content_layout.itemAt(i).widget()
            if widget_to_remove is not None:
                widget_to_remove.setParent(None)

        if text == "Imagen Gato":
            label = QLabel(self)
            pixmap = QPixmap("gato.jpg")
            if not pixmap.isNull():
                label.setPixmap(pixmap)
                label.setAlignment(Qt.AlignmentFlag.AlignCenter)
                self.content_layout.addWidget(label)
                self.resize(pixmap.width(), pixmap.height())
            else:
                label.setText("Image not found!")
                self.content_layout.addWidget(label)
                self.resize(400, 200)

        elif text == "Textos Giratorios":
            self.widget1.setParent(self)  # Asignar a la ventana
            self.widget2.setParent(self)  # Asignar a la ventana
            self.widget1.show()
            self.widget2.show()

            self.resize(800, 600)

            if self.timer is None:
                self.timer = QTimer(self)
                self.timer.timeout.connect(self.move_widgets)

            self.timer.start(30)

    def move_widgets(self):
        window_width = self.width()
        window_height = self.height()

        radius = min(window_width, window_height) // 2 - 100
        radians = self.angle * (pi / 180)

        center_x = window_width // 2
        center_y = window_height // 2

        x1 = int(center_x + radius * cos(radians)) - self.widget1.width() // 2
        y1 = int(center_y + radius * sin(radians)) - self.widget1.height() // 2

        x2 = int(center_x + radius * cos(radians + pi)) - self.widget2.width() // 2
        y2 = int(center_y + radius * sin(radians + pi)) - self.widget2.height() // 2

        self.widget1.move(x1, y1)
        self.widget2.move(x2, y2)

        self.angle = (self.angle + 2) % 360


app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec()
