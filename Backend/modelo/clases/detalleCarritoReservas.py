class DetalleCarritoReservas():
    def __init__(self, id,idCarritoReserva,idInstalacion):
        
        self._id=id
        self._idCarritoReserva= idCarritoReserva
        self._idInstalacion=idInstalacion
        self._cantidad= cantidad
    
    #getters
    def getId(self):
        return self._id

    def getIdCarritoReserva(self):
        return self._idCarritoReserva

    def getIdInstalacion(self):
        return self._idInstalacion

    

    #setters

    def setId(self,id):
        self._id=id

    def setIdCarritoReserva(self,idCarritoReserva):
        self._idCarritoProductos= idCarritoReserva

    def setIdInstalacion(self,idInstalacion):
        self._idProducto= idInstalacion

   