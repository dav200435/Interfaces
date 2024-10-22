import json

class Controller:
    def __init__(self):
        self.filePath = './data/inventory.json'
        self.data = []
        self.readFile()

    def readFile(self):
        try:
            with open(self.filePath, 'r') as file:
                self.data = json.load(file)
                print("Datos cargados:", self.data)  # Agrega esta línea para verificar la carga
        except FileNotFoundError:
            self.data = []
            print(f"El archivo {self.filePath} no existe, creando uno nuevo.")
        except json.JSONDecodeError:
            print("Error al leer el archivo JSON. Asegúrate de que el formato sea correcto.")

    def saveFile(self):
        with open(self.filePath, 'w') as file:
            json.dump(self.data, file, indent=4)

    def addItem(self, newItem):
        self.data.append(newItem)
        self.saveFile()

    def editItem(self, itemId, tipeData, updatedData):
        for item in self.data:
            if item['id'] == itemId:
                match tipeData:
                    case 'name':
                        item['name'] = updatedData
                    case 'unitPrice':
                        item['unitPrice'] = updatedData
                    case 'stock':
                        item['stock'] = updatedData
                self.saveFile()
                return

    def deleteItem(self, itemId):
        for item in self.data:
            if item['id'] == itemId:
                self.data.remove(item)
                self.saveFile()
                return True 
        return False 

    def getAllItems(self):
        return self.data

    def getItemById(self, itemId):
        for item in self.data:
            if item['id'] == itemId:
                return item
        return None

    def getNextId(self):
        """Obtiene el siguiente ID disponible para un nuevo ítem."""
        if not self.data:
            return 1  # Si no hay datos, comienza con 1
        else:
            return max(item['id'] for item in self.data) + 1  # Devuelve el ID máximo + 1