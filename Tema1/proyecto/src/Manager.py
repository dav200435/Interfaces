from PyQt6.QtWidgets import QWidget, QPushButton, QInputDialog, QLineEdit, QMessageBox, QTableView
from PyQt6.QtGui import QStandardItem, QStandardItemModel
from PyQt6 import uic
from Controller import Controller
from PDFExportApp import PDFExportApp

class Manager(QWidget):
    def __init__(self, login_window) -> None:
        super().__init__()
        self.setWindowTitle("Inventario")
        uic.loadUi('./Windows/Manager.ui', self)

        self.controller = Controller()
        self.login_window = login_window

        # Find buttons
        self.exportPdfbtn = self.findChild(QPushButton, 'exportPdf')
        self.addButton = self.findChild(QPushButton, 'add')
        self.removeButton = self.findChild(QPushButton, 'remove')
        self.editButton = self.findChild(QPushButton, 'edit')
        self.logOut = self.findChild(QPushButton, 'logOut')

        # Connect buttons to their respective methods
        self.exportPdfbtn.clicked.connect(self.openExportDialog)
        self.addButton.clicked.connect(self.addItem)
        self.removeButton.clicked.connect(self.removeItem)
        self.editButton.clicked.connect(self.editItem)
        self.logOut.clicked.connect(self.logout)

        # Initialize the QTableView model
        self.tableView = self.findChild(QTableView, 'table')
        self.model = QStandardItemModel()
        self.tableView.setModel(self.model)

        # Load data into the table
        self.getData()

    def getData(self):
        """Obtiene los datos del inventario y los carga en el QTableView"""
        self.data = self.controller.getAllItems()
        self.model.setRowCount(0)  # Clear existing rows

        # Populate the table with data
        for item in self.data:
            row = [
                QStandardItem(str(item['id'])),
                QStandardItem(item['name']),
                QStandardItem(str(item['unitPrice'])),
                QStandardItem(str(item['stock']))
            ]
            self.model.appendRow(row)

    def openExportDialog(self):
        """Abre la ventana para exportar el informe a PDF"""
        self.export_app = PDFExportApp(self.data)
        self.export_app.show()

    def addItem(self):
        """Add a new item to the inventory"""
        name, ok_name = QInputDialog.getText(self, 'Agregar nuevo ítem', 'Nombre del ítem:')
        
        if ok_name and name:
            price, ok_price = QInputDialog.getDouble(self, 'Agregar nuevo ítem', 'Precio unitario:')
            
            if ok_price:
                stock, ok_stock = QInputDialog.getInt(self, 'Agregar nuevo ítem', 'Stock disponible:')
                stock = max(stock, 0)  # Establece el stock a 0 si es negativo
                
                new_item = {
                    'id': self.controller.getNextId(),
                    'name': name,
                    'unitPrice': price,
                    'stock': stock
                }
                self.controller.addItem(new_item)
                QMessageBox.information(self, 'Éxito', 'Ítem agregado correctamente.')
                self.getData()  # Refresh data


    def removeItem(self):
        """Remove an item from the inventory"""
        selected_item_id, ok = QInputDialog.getInt(self, 'Eliminar ítem', 'ID del ítem a eliminar:')
        if ok:
            if self.controller.deleteItem(selected_item_id):
                QMessageBox.information(self, 'Éxito', 'Ítem eliminado correctamente.')
                self.getData()  # Refresh data
            else:
                QMessageBox.warning(self, 'Error', 'No se encontró el ítem con el ID especificado.')

    def editItem(self):
        """Edit an existing item in the inventory"""
        selected_item_id, ok = QInputDialog.getInt(self, 'Editar ítem', 'ID del ítem a editar:')
        if ok:
            item = self.controller.getItemById(selected_item_id)
            if item:
                new_name, ok_name = QInputDialog.getText(
                    self, 
                    'Editar ítem', 
                    'Nombre del ítem:', 
                    QLineEdit.EchoMode.Normal,  # Corrected here
                    item['name']
                )
                if ok_name and new_name:
                    new_price, ok_price = QInputDialog.getDouble(
                        self, 
                        'Editar ítem', 
                        'Precio unitario:', 
                        value=item['unitPrice']
                    )
                    if ok_price:
                        new_stock, ok_stock = QInputDialog.getInt(
                            self, 
                            'Editar ítem', 
                            'Stock disponible:', 
                            value=item['stock']
                        )
                        if ok_stock:
                            self.controller.editItem(selected_item_id, 'name', new_name)
                            self.controller.editItem(selected_item_id, 'unitPrice', new_price)
                            self.controller.editItem(selected_item_id, 'stock', new_stock)
                            QMessageBox.information(self, 'Éxito', 'Ítem editado correctamente.')
                            self.getData()  # Refresh data
            else:
                QMessageBox.warning(self, 'Error', 'No se encontró el ítem con el ID especificado.')

    def logout(self):
        self.login_window.logout()
        self.close()