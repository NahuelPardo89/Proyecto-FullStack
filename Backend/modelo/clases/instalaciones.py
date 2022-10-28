class Instalacion():
    def __init__(self, id,nombre,precio):
        
        self._id= id
        self._nombre= nombre
        self._precio= precio
        
    #Getters

    def getidInstalacion(self):
        return self._id
        