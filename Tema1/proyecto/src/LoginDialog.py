from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QDialog, QWidget, QDialogButtonBox, QVBoxLayout, QLabel

class LoginDialog(QDialog):
    
    def __init__(self, parent: QWidget | None = None, flags: Qt.WindowType = Qt.WindowType.Dialog) -> None:
        super().__init__(parent, flags)
        self.setWindowTitle("Login Status")
        
    def success(self, user):
        msg = QLabel(f'Welcome back {user}!')
        QBtn = (
            QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel
        )

        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        layout = QVBoxLayout()
        layout.addWidget(msg)
        layout.addWidget(self.buttonBox)
        self.setLayout(layout)
    
    def failed(self):
        msg = QLabel('Login failed. Please try again.')
        QBtn = QDialogButtonBox.StandardButton.Ok

        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)

        layout = QVBoxLayout()
        layout.addWidget(msg)
        layout.addWidget(self.buttonBox)
        self.setLayout(layout)
