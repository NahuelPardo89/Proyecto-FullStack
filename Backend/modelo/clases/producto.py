class Producto:
    def __init__(self, id,proveedor,nombre,marca,descripcion,precio,stock,foto):
        
        self._id= id
        self._idProveedor = proveedor
        self._nombre= nombre
        self._marca= marca
        self._descripcion= descripcion
        self._precio= precio
        self._stock= stock
        self._foto = foto
    #Getters
   
    def getAtributos(self):
        return (self._id,self._idProveedor,self._nombre,self._marca,self._descripcion,self._precio, self._stock,self._foto)
    
    def getId(self):
        return self._id
        
    def getNombre(self):
        return self._nombre
    
    def getMarca(self):
        return self._marca
    
    def getDescripcion(self):
        return self._descripcion

    def getPrecio(self):
        return self._precio

    def getStock(self):
        return self._stock

    def getIdProveedor(self):
        return self._idProveedor

    def getFoto(self):
        return self._foto
        
    #setters
    def setId(self, id):
        self._id= id
        
    def setNombre(self,nombre):
        self._nombre= nombre
    
    def setMarca(self,marca):
        self._marca= marca
    
    def setDescripcion(self,descripcion):
        self._descripcion= descripcion

    def setPrecio(self, precio):
        self._precio= precio
    
    def setStock(self, stock):
        self._stock= stock

    def setProveedor(self, proveedor):
        self._idProveedor= proveedor

    def setFoto(self,foto):
        self._foto= foto

    #methods
    def vender(self):
        if self._stock>0:
            self._stock-=1
        else:
            raise ValueError

    def reponer(self,cantidad):
        self._stock+=cantidad