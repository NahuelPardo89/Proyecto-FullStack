
class ModeloCarritoReservas:
    @classmethod
    def addCarritoReserva(self,conn,carrito):
        try:
            cursor=conn.cursor()
            cursor.execute("INSERT INTO `CarritoReservas` ( `idCarrito`, `idEmpleado`, `idCliente`, `monto`, `fecha`)  VALUES (%s,%s,%s,%s,%s)",(
            carrito.getIdCarrito(),carrito.getidEmpleado(),carrito.getidCliente(),carrito.getmonto(),carrito.getfecha()))
            conn.commit()
        except Exception as ex:
            raise Exception(ex)

    def delCarritoReserva(self,conn,carrito):
        try:
            cursor=conn.cursor()
            cursor.execute("DELETE FROM CarritoReservas WHERE idCarrito=%s",(carrito.getId(),))
            conn.commit()
        except Exception as ex:
            raise Exception(ex)   

    def updateCarritoReserva(self,conn,carrito):
        try:
            cursor=conn.cursor()
            cursor.execute("""
                    UPDATE carritoreserva
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

    def selectOneCarritoReserva(self,conn,carrito):
        try:
            cursor=conn.cursor()
            cursor.execute("SELECT * FROM CarritoReservas WHERE idCarrito=%s",(carrito.getId(),))
            filacarrito =cursor.fetchone()
        
            return filacarrito
        except Exception as ex:
            raise Exception(ex)

    def selectAllCarritoReserva(self,conn):
        try:
            cursor=conn.cursor()
            cursor.execute("SELECT * FROM CarritoReservas")
            datacarrito = cursor.fetchall()
            
            return datacarrito
        except Exception as ex:
            raise Exception(ex)