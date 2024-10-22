from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

class PdfConverter:
    def __init__(self, data):
        self.data = data

    def createPdf(self, file_path):
        """Genera un archivo PDF con los datos y lo guarda en la ubicación especificada"""
        pdf = canvas.Canvas(file_path, pagesize=A4)
        pdf.setTitle("Informe de Inventario")
        
        width, height = A4
        pdf.drawString(100, height - 50, "Informe de Inventario")
        
        y_position = height - 100
        pdf.drawString(100, y_position, "ID     Nombre     Precio Unitario     Stock")
        
        y_position -= 30
        for item in self.data:
            pdf.drawString(100, y_position, f"{item['id']}     {item['name']}     {item['unitPrice']}     {item['stock']}")
            y_position -= 20
            if y_position < 50: 
                pdf.showPage()
                y_position = height - 50

        pdf.save()
