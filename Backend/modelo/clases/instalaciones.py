class Instalacion():
    def __init__(self, id,nombre,precio):
        
        self._idInstalacion= id
        self._nombre= nombre
        self._precio= precio
        
    
#Getters

    def getidInstalacion(self):
        return self._idInstalacion
    def getnombre(self):
        return self._nombre
    def getprecio(self):
        return self._precio

#Setters
    def setidInstalacion(self, id):
        self._idInstalacion = id
    def setnombre(self, nombre):
        self._nombre = nombre    
    def setprecio(self, precio):
        self._precio = precio



    
        