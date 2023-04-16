
class User:
    def __init__(self, id,nombre,apellido,telefono,direccion,contraseña):
        
        self._id= id
        self._nombre= nombre
        self._apellido= apellido
        self._telefono= telefono
        self._direccion= direccion
        self._contraseña= contraseña
       
    #Getters
    def getId(self):
        return self._id
        
    def getNombre(self):
        return self._nombre
            
    def getApellido(self):
        return self._apellido

    def getTel(self):
        return self._telefono

    def getDireccion(self):
        return self._direccion

    def getContraseña(self):
        return self._contraseña

    
        
        
    #setters
    def setId(self,id):
        self._id=id
        
    def setNombre(self,nombre):
        self._nombre=nombre
            
    def setApellido(self,apellido):
        self._apellido=apellido

    def setTel(self,telefono):
        self._telefono=telefono

    def setDireccion(self,direccion):
        self._direccion=direccion

    def setContraseña(self,contraseña):
       self._contraseña=contraseña

    #methods

class Empleado(User):
    def __init__(self, id,nombre,apellido,telefono,direccion,contraseña,idEmpleado,instalacion,horario,):
        super().__init__(id,nombre,apellido,telefono,direccion,contraseña)
        self._idEmpleado    = idEmpleado
        self._horario       = horario
        self._idInstalacion = instalacion
       
    #Getters
       
    def getIdInstalacion(self):
        return self._idInstalacion
    
    def getIdEmpleado(self):
        return self._idEmpleado
        
    def getHorario(self):
        return self._horario

  
        
    #setters
    def setIdEmpleado(self,id):
        self._idEmpleado=id
    
       
    def setIdInstalacion(self,id):
        self._idInstalacion=id    
         
    def setHorario(self,Horario):
        self._horario=Horario
    #methods



class Cliente(User):
  
    def __init__(self, id,nombre,apellido,telefono,direccion,contraseña,idCliente,socio):
        super().__init__(id,nombre,apellido,telefono,direccion,contraseña)
        self._IdCliente = idCliente
        self._socio = socio
    #setters
    def getIdCliente(self):
        return self._IdCliente
    
    def getSocio(self):
        return self._socio
    #getters
    
    def setIdCliente(self,idCliente):
        self._IdCliente=idCliente
    
    def setSocio(self,socio):
        self._socio= socio
