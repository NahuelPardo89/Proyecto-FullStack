class ModelProveedor:
    @classmethod
    def addProveedor(self,conn,proveedor):
        try:
            cursor=conn.cursor()
            cursor.execute("INSERT INTO `proveedores`(`idProveedor`,`idEmpleado`,`Nombre`,`empresa`,`telefono`) VALUES (%s,%s,%s,%s,%s)",(
            proveedor.getId(),proveedor.getIdEmpleado(),proveedor.getNombre(),proveedor.getEmpresa(),proveedor.getTelefono()))
            conn.commit()
        except Exception as ex:
            raise Exception(ex)
    
    def updateProveedor(self,conn,proveedor):
        try:
            cursor=conn.cursor()
            cursor.execute("""
                    UPDATE proveedores
                    SET idEmpleado=%s,
                        Nombre=%s,
                        empresa=%s,
                        telefono=%s
                        
                WHERE idProveedor=%s
                """,(proveedor.getIdEmpleado(),proveedor.getNombre(),proveedor.getEmpresa(),proveedor.getTelefono(),proveedor.getId()))
            conn.commit()
        except Exception as ex:
            raise Exception(ex)

    def deleteProveedor(self,conn,proveedor):
        try:
            cursor=conn.cursor()
            cursor.execute("DELETE FROM proveedores WHERE idProveedor=%s",(proveedor.getId(),))
            conn.commit()
        except Exception as ex:
            raise Exception(ex)       

    def selectOneProveedor(self,conn,proveedor):
        try:
            cursor=conn.cursor()
            cursor.execute("SELECT * FROM proveedores WHERE idProveedor=%s",(proveedor.getId(),))
            fila=cursor.fetchall()
        
            return fila
        except Exception as ex:
            raise Exception(ex)

    def selectAllProveedores(conn):
        try:
            cursor=conn.cursor()
            cursor.execute("SELECT * FROM proveedores")
            data = cursor.fetchall()
            
            return data
        except Exception as ex:
            raise Exception(ex)
