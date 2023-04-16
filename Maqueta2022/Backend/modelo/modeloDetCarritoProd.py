class ModeloDetalleCarritoProductos:
    @classmethod
    def addDetalleCarritoProducto(self,conn,detcarritoProducto):
        try:
            cursor=conn.cursor()
            cursor.execute("INSERT INTO `detallecarritoproductos` (`idDetalleProducto`, `idCarritoProductos`, `idProducto`, `cantidad`)  VALUES (%s,%s,%s,%s)",(
            detcarritoProducto.getId(),detcarritoProducto.getIdCarritoProductos(),detcarritoProducto.getIdproducto(),detcarritoProducto.getCantidad()))
            conn.commit()
        except Exception as ex:
            raise Exception(ex)

    def delDetalleCarritoProducto(self,conn,detcarritoProducto):
        try:
            cursor=conn.cursor()
            cursor.execute("DELETE FROM detallecarritoproductos WHERE idDetalleProducto=%s",(detcarritoProducto.getId(),))
            conn.commit()
        except Exception as ex:
            raise Exception(ex)   

    def updateDetalleCarritoProducto(self,conn,detcarritoProducto):
        try:
            cursor=conn.cursor()
            cursor.execute("""
                    UPDATE detallecarritoproductos
                    SET idCarritoProductos=%s,
                        idProducto=%s,
                        cantidad=%s
                    WHERE idDetalleProducto=%s
                """,(detcarritoProducto.getIdCarritoProductos(),detcarritoProducto.getIdproducto(),detcarritoProducto.getCantidad(),detcarritoProducto.getId()))
            conn.commit()
        except Exception as ex:
            raise Exception(ex)

    def selectOneCarritoProducto(self,conn,detcarritoProducto):
        try:
            cursor=conn.cursor()
            cursor.execute("SELECT * FROM detallecarritoproductos WHERE idDetalleProducto=%s",(detcarritoProducto.getId(),))
            filacarrito =cursor.fetchone()
        
            return filacarrito
        except Exception as ex:
            raise Exception(ex)

    def selectAllCarritoProducto(self,conn):
        try:
            cursor=conn.cursor()
            cursor.execute("SELECT * FROM detallecarritoproductos")
            datacarrito = cursor.fetchall()
            
            return datacarrito
        except Exception as ex:
            raise Exception(ex)