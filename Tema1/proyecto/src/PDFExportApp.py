import os
from PyQt6.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QWidget

from PdfConverter import PdfConverter

class PDFExportApp(QMainWindow):
    def __init__(self, data):
        super().__init__()
        self.data = data

        self.setWindowTitle('Exportar Informe a PDF')
        self.setGeometry(100, 100, 400, 200)
        
        layout = QVBoxLayout()
        export_button = QPushButton('Exportar Informe a PDF')
        export_button.clicked.connect(self.exportPdf)

        layout.addWidget(export_button)
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def exportPdf(self):
        """Genera el informe PDF y lo guarda en la carpeta 'data'"""
        # Define la ruta del archivo PDF en la carpeta 'data'
        file_path = './data/informe_inventario.pdf'

        # Asegúrate de que la carpeta 'data' existe
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        report_generator = PdfConverter(self.data)
        report_generator.createPdf(file_path)
        print(f"Informe PDF guardado en: {file_path}")
        
        # Cierra la ventana emergente después de guardar el PDF
        self.close()
