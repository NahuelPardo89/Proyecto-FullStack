from Backend.modelo.clases.producto import Producto
class ModelProducto:
    @classmethod    
    def addProducto(self,conn,producto):
            try:
                cursor=conn.cursor()
                cursor.execute("INSERT INTO `productos` ( `idProveedor`, `Nombre`, `marca`, `descripcion`, `precio`, `stock`, `foto`)  VALUES (%s,%s,%s,%s,%s,%s,%s)",(
                producto.getIdProveedor(),producto.getNombre(),producto.getMarca(),producto.getDescripcion(),producto.getPrecio(), producto.getStock(),producto.getFoto()))
                conn.commit()
            except Exception as ex:
                raise Exception(ex)
    @classmethod  
    def updateProducto(self,conn,producto):
        try:
            cursor=conn.cursor()
            cursor.execute("""
                    UPDATE productos
                    SET idProveedor=%s,
                        Nombre=%s,
                        marca=%s,
                        descripcion=%s,
                        precio=%s,
                        stock=%s,
                        foto=%s
                WHERE idProd=%s
                """,(producto.getIdProveedor(),producto.getNombre(),producto.getMarca(),producto.getDescripcion(),producto.getPrecio(), producto.getStock(),producto.getFoto(),producto.getId()))
            conn.commit()
        except Exception as ex:
            raise Exception(ex)
    @classmethod
    def deleteProducto(self,conn,producto):
        try:
            cursor=conn.cursor()
            cursor.execute("DELETE FROM productos WHERE idProd=%s",(producto.getId(),))
            conn.commit()
        except Exception as ex:
            raise Exception(ex)       
    @classmethod
    def selectOneProducto(self,conn,id):
        try:
            cursor=conn.cursor()
            cursor.execute("SELECT * FROM productos WHERE idProd=%s",(id,))
            row=cursor.fetchone()
            
            producto=Producto(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7])
            return producto
        except Exception as ex:
            raise Exception(ex)

    def selectAllProducto(conn):
        try:
            cursor=conn.cursor()
            cursor.execute("SELECT * FROM productos")
            data = cursor.fetchall()
            
            return data
        except Exception as ex:
            raise Exception(ex)
