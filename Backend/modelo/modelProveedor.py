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