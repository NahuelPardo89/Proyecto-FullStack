from sys import path

path.append('C:\\Users\\nanit\\Desktop\\proyecto\\Proyecto-FullStack\\Backend')


from modelo.conexionDb import Conexion
from modelo.modelProducto import ModelProducto
from modelo.modelUser import ModelUser
from modelo.clases.users import User,Empleado,Cliente
from modelo.clases.proveedor import Proveedor
from modelo.clases.producto import Producto
from modelo.clases.instalaciones import Instalacion


db=Conexion()
conn=db.getConn()
instalacion=Instalacion(1,"gym",20)
user1= User(3,"ricardo","montaner","123456","estrada 1433","admin123")
user2=User(5,"pablo","carrizo","123456","maipo 100","admin123")
empleado= Empleado(user2.getId(),user2.getNombre(),user2.getApellido(),user2.getTel(),user2.getDireccion(),user2.getContraseña(),23,instalacion,"horario")
provedor= Proveedor(1,"mario","tate","123456",empleado)

cliente =Cliente(user1.getId(),user1.getNombre(),user1.getApellido(),user1.getTel(),user1.getDireccion(),user1.getContraseña(),1,1)
#ModelUser.addCliente(conn,cliente)
#ModelUser.addUser(conn,user2)
#ModelUser.addEmpleado(conn,empleado)
#print (empleado.getId(),empleado.getIdEmpleado(), empleado.getIdInstalacion(),empleado.getHorario())