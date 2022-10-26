
class Proveedor:
    def __init__(self, id,nombre,empresa,telefono,empleado):
        
        self._id= id
        self._nombre= nombre
        self._empresa= empresa
        self._telefono= telefono
        self._idEmpleado= empleado.getIdEmpleado()
       
    #Getters
    def getId(self):
        return self._id
        
    def getNombre(self):
        return self._nombre
    
    def getEmpresa(self):
        return self._empresa

    def getTelefono(self):
        return self._telefono
    
    def getPersonalId(self):
        return self._personalId
   
    def setId(self, id):
        self._id= id
    
    #setters    
    def setNombre(self,nombre):
        self._nombre= nombre
    
    def setDescripcion(self,empresa):
        self._empresa= empresa

    def setTelefono(self, telefono):
        self._telefono= telefono
       
    def setPersonal(self, empleado):
        self._idEmpleado= empleado.getIdEmpleado()