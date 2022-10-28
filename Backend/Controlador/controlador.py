from sys import path
#PARA IMPORTAR DESDE MODELO
path.append('C:\\Users\\nanit\\Desktop\\proyecto\\Proyecto-FullStack\\Backend')

#CONEXION
from modelo.conexionDb import Conexion

#MODELOS
from modelo.initDataBase import InitDb
from modelo.modelProducto import ModelProducto
from modelo.modelUser import ModelUser
from modelo.modelInstalacion import ModelInstalacion

#CLASES
from modelo.clases.users import User,Empleado,Cliente
from modelo.clases.proveedor import Proveedor
from modelo.clases.producto import Producto
from modelo.clases.instalaciones import Instalacion

#inicializacion de bd

db=InitDb()
conn=db.database  


if  conn.is_connected():

    

    
    
    
    ########################################################################################
    #SIMULACION DE OBTENCION DE DATOS DEL FORMULARIO REGISTRO


    #VARIABLES ESTATICAS
      
    #idCliente =1   idCliente (se asigna automatico en bd)
    #socio     =1   =true socio (funcionalidad futura)
    
    
    #usuario rellena campos requeridos y pulsa Submit

    #                                                       DATOS CAPTURADOS                     |necesarias para contructor de la clase Cliente
    #                   dni   |  nombre   | apellido  | telefono   | direccion     |contraseña   |
    cliente =Cliente(33000111,"ricardo"  ,"montaner",   "123456"  ,"estrada 1433", "Admin123",   1 , 1)

    ModelUser.addCliente(conn,cliente)
    













#usuarioLogged=ModelUser.login(conn,empleado)
#print(usuarioLogged)

#ModelUser.addCliente(conn,cliente)
#ModelUser.addUser(conn,user2)
#ModelUser.addEmpleado(conn,empleado)
#print (empleado.getId(),empleado.getIdEmpleado(), empleado.getIdInstalacion(),empleado.getHorario())