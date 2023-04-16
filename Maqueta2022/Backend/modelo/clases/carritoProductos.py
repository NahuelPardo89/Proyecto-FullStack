class CarritoProductos:
    def __init__(self, id, idCliente,idEmpleado, monto, fecha):
        self._id = id
        self._idCliente=idCliente
        self._idEmpleado = idEmpleado
        self._monto= monto
        self._fecha= fecha


   
    #Getter
    def getIdCarrito(self):
        return self._id
    
    def getIdCliente(self):
        return self._idCliente
    
    def getIdEmpleado(self):
        return self._idEmpleado
    
    def getMonto(self):
        return self._monto
    
    def getFecha(self):
        return self._fecha


   
    #Setter
    def setIdCarrito(self,id):
        self._id = id

    def setIdCliente(self,idCliente):
        self._idCliente = idCliente
    
    def setIdEmpleado(self,idempleado):
        self._idEmpleado = idempleado

    def setMonto(self,monto):
        self._monto = monto

    def setFecha(self,fecha):
        self._fecha = fecha



















































