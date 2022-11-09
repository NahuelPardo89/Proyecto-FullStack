from sys import path
#PARA IMPORTAR DESDE MODELO
path.append('C:\\Users\\nanit\\OneDrive\\Escritorio\\Proyecto\\Proyecto-FullStack')

#DATABASE
from Backend.modelo.database.conexionDb import Conexion
from Backend.modelo.database.createTables import CreateTables
from Backend.modelo.database.initDataBase import InitDb

#MODELOS

from Backend.modelo.modelProducto import ModelProducto
from Backend.modelo.modelUser import ModelUser
from Backend.modelo.modelInstalacion import ModelInstalacion

#CLASES
from Backend.modelo.clases.users import User,Empleado,Cliente
from Backend.modelo.clases.proveedor import Proveedor
from Backend.modelo.clases.producto import Producto
from Backend.modelo.clases.instalaciones import Instalacion



#CONEXION CON BASE DE DATOS ampaDB
db=Conexion()
conn= db.connection

#CREACION DE TABLAS
#CreateTables(conn)

#CARGA DE DATOS INICIALES EN TABLAS
#InitDb(conn)


########################################################################################
#SIMULACION DE OBTENCION DE DATOS DEL FORMULARIO REGISTRO

if  conn.is_connected():
    
    
    #VARIABLES ESTATICAS
      
    #idCliente =1   idCliente (se asigna automatico en bd)
    #socio     =1   =true socio (funcionalidad futura)
    
    #simulacion de formilario de Registro
    
    dni= int(input('Ingrese numero de DNI:\n'))
    nombre=input('ingrese nombre:\n')
    apellido=input('ingrese apellido:\n')
    telefono=input('ingrese numero de telefono:\n')
    direccion=input('ingrese direccion:\n')
    contrasena=input('íngrese contraseña:\n')
    #usuario rellena campos requeridos y pulsa enviar
    #                                                       DATOS CAPTURADOS                     |necesarias para contructor de la clase Cliente
    #                   dni   |  nombre   | apellido  | telefono   | direccion     |contraseña   |
    cliente =Cliente(   dni,   nombre  ,   apellido,   telefono ,  direccion,       contrasena,   1 , 1)
    
    #AGREGO CLIENTE A LA BASE DE DATOS
    ModelUser.addCliente(conn,cliente)
    print('Registro exitoso')

    











usuarioLogged=ModelUser.login(conn,cliente)
print(usuarioLogged.getContraseña())

#ModelUser.addCliente(conn,cliente)
#ModelUser.addUser(conn,user2)
#ModelUser.addEmpleado(conn,empleado)
#print (empleado.getId(),empleado.getIdEmpleado(), empleado.getIdInstalacion(),empleado.getHorario())

