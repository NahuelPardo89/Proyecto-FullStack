class ModeloCarritoProductos:
    @classmethod
    def addCarritoProductos(self,conn,carrito):
        try:
            cursor=conn.cursor()
            cursor.execute("INSERT INTO `CarritoProductos` ( `idCarrito`, `idEmpleado`, `idCliente`, `monto`, `fecha`)  VALUES (%s,%s,%s,%s,%s)",(
            carrito.getIdCarrito(),carrito.getidEmpleado(),carrito.getidCliente(),carrito.getmonto(),carrito.getfecha()))
            conn.commit()
        except Exception as ex:
            raise Exception(ex)

    def delCarritoProductos(self,conn,carrito):
        try:
            cursor=conn.cursor()
            cursor.execute("DELETE FROM CarritoProductos WHERE idCarrito=%s",(carrito.getId(),))
            conn.commit()
        except Exception as ex:
            raise Exception(ex)   

    def updateCarritoProductos(self,conn,carrito):
        try:
            cursor=conn.cursor()
            cursor.execute("""
                    UPDATE carritoProductos
                    SET idCarrito=%s,
                        idEmpleado%s,
                        idCliente%s,
                        monto=%s,
                        fecha=%s,
                WHERE idCarrito=%s
                """,(carrito.getIdCarrito(),carrito.getidEmpleado(),carrito.getidCliente(),carrito.getmonto(),carrito.getfecha()))
            conn.commit()
        except Exception as ex:
            raise Exception(ex)