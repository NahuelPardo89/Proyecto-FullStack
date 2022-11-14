class ModeloDetalleCarritoReservas:
    @classmethod
    def addDetalleCarritoReserva(self,conn,DetcarritoReserva):
        try:
            cursor=conn.cursor()
            cursor.execute("INSERT INTO `detallecarritoreservas` (`idDetalleReserva`, `idCarritoReservas`, `idInstalacion`)  VALUES (%s,%s,%s)",(
            DetcarritoReserva.getId(), DetcarritoReserva.getIdCarritoReserva(), DetcarritoReserva.getIdInstalacion()))
            conn.commit()
        except Exception as ex:
            raise Exception(ex)

    def delDetalleCarritoReserva(self,conn,DetcarritoReserva):
        try:
            cursor=conn.cursor()
            cursor.execute("DELETE FROM detallecarritoreservas WHERE idDetalleReserva=%s",(DetcarritoReserva.getId(),))
            conn.commit()
        except Exception as ex:
            raise Exception(ex)   

    def updateDetalleCarritoReserva(self,conn,DetcarritoReserva):
        try:
            cursor=conn.cursor()
            cursor.execute("""
                    UPDATE detallecarritoreservas
                    SET idCarritoReservas=%s,
                        idInstalacion=%s,
                    WHERE idDetalleReserva=%s
                """,(DetcarritoReserva.getIdCarritoReserva(),DetcarritoReserva.getIdInstalacion(),DetcarritoReserva.getId()))
            conn.commit()
        except Exception as ex:
            raise Exception(ex)

    def selectOneCarritoReserva(self,conn,DetcarritoReserva):
        try:
            cursor=conn.cursor()
            cursor.execute("SELECT * FROM detallecarritoreservas WHERE idDetalleReserva=%s",(DetcarritoReserva.getId(),))
            filacarrito =cursor.fetchone()
        
            return filacarrito
        except Exception as ex:
            raise Exception(ex)

    def selectAllCarritoReserva(self,conn):
        try:
            cursor=conn.cursor()
            cursor.execute("SELECT * FROM detallecarritoreservas")
            datacarrito = cursor.fetchall()
            
            return datacarrito
        except Exception as ex:
            raise Exception(ex)