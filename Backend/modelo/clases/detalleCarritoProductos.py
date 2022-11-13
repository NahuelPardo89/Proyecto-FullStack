class DetalleCarritoProductos():
    def __init__(self, id,idCarritoProductos,idProducto,cantidad):
        
        self._id=id
        self._idCarritoProductos= idCarritoProductos
        self._idProducto=idProducto
        self._cantidad= cantidad
    
    #getters
    def getId(self):
        return self._id

    def getIdCarritoProductos(self):
        return self._idCarritoProductos

    def getIdproducto(self):
        return self._idProducto

    def getCantidad(self):
        return self._cantidad

    #setters

    def setId(self,id):
        self._id=id

    def setIdCarritoProductos(self,idCarritoProductos):
        self._idCarritoProductos= idCarritoProductos

    def setIdproducto(self,idproducto):
        self._idProducto= idproducto

    def setCantidad(self,cantidad):
        self._cantidad= cantidad

