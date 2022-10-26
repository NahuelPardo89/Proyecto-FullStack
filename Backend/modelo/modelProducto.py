

#from conexionDb import Conexion
from .clases.producto import Producto



###
#conn=Conexion()
#conn1=conn.getConn()
####
    
def addProducto(conn,producto):
        cursor=conn.connection.cursor()
        cursor.execute("INSERT INTO `productos` ( `idProveedor`, `Nombre`, `marca`, `descripcion`, `precio`, `stock`, `foto`)  VALUES (%s,%s,%s,%s,%s,%s,%s)",(
        producto.getIdProveedor(),producto.getNombre(),producto.getMarca(),producto.getDescripcion(),producto.getPrecio(), producto.getStock(),producto.getFoto()))
        conn.commit()
        conn.close()

def updateProducto(conn,producto):
    cursor=conn.connection.cursor()
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
    conn.close()

def deleteProducto(conn,producto):
    
    cursor=conn.cursor()
    cursor.execute("DELETE FROM productos WHERE idProd=%s",(producto.getId(),))
    conn.commit()
    conn.close()

def selectOne(conn,producto):
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM productos WHERE idProd=%s",(producto.getId(),))
    fila=cursor.fetchall()
    return fila

def selectAll(conn):
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM productos")
    data = cursor.fetchall()
    return data
    
#producto = Producto(5,1,"zpa","adidas","chica",23,2,"fototruca.jpg")
#addProducto(conn1,producto)
##updateProducto(conn1,producto)
#deleteProducto(conn1,producto)
#prod=selectProducto(conn1,producto)
#print(prod)
#data=selectAll(conn1)
#print(data)