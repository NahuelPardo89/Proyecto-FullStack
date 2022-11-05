class CarritoReservas:
    def __init__(self,idCarrito,empleado,cliente,monto,fecha):
        self.idCarritoReserva= idCarrito
        self.idEmpleado=empleado.getIdEmpleado()
        self.idCliente= cliente.getIdCliente()
        self.monto=monto
        self.fecha=fecha

    # Getters
    def getIdCarrito(self):
        return self.idCarritoReserva
    def getIdEmpleado(self):
        return self.idEmpleado
    def getIdCliente(self):
        return self.idCliente
    def getMonto(self):
        return self.monto
    def getFecha(self):
        return self.fecha

    #setters
    def setIdCarritoReserva(self,idCarrito):
        self.idCarritoReserva= idCarrito
        
    def setIdCliente(self,idcliente):
        self.idCliente= idcliente
   
    def setIdEmpleado(self,idempleado):
        self.idEmpleado=idempleado
   
    
    def setMonto(self,monto):
        self.monto=monto

    def setFecha(self,fecha):
        self.fecha= fecha           