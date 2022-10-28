from sys import path

path.append('C:\\Users\\nanit\\Desktop\\proyecto\\Proyecto-FullStack\\Backend')


from modelo.conexionDb import Conexion
from modelo.modelProducto import ModelProducto
from modelo.modelUser import ModelUser
from modelo.clases.users import User,Empleado,Cliente
from modelo.clases.proveedor import Proveedor
from modelo.clases.producto import Producto
from modelo.clases.instalaciones import Instalacion

#inicializacion de bd
db=Conexion()
conn=db.connection
if  conn.is_connected():

    #CARGA DE DATOS: EMPLEADOS, PRODUCTOS, INSTALACIONES, PROVEEDORES

    #########################################  INSTALACIONES  ###########################
                        # ID | NOMBRE   |PRECIO USO HORA
    gimnasio=Instalacion( 1, "Gimnasio",400)
    paddle  =Instalacion( 2, "PADDLE",  1000)
    futbol  =Instalacion( 3, "Gimnasio",400)
    
    ######################################################################################
    
     
    #########################################  EMPELADOS  ########################################################## ##############                                                           
                    #   DNI     | NOMBRE  | APELLIDO  |TELEFONO   |DIRECCION       CONTRASEÑA| IDEMPLEADO | INSTALACION  |HORARIO
    empleado1=Empleado(25492666, "Juana",   "funes",    "351461325","Maipu 166",    "JuanaFu25",      1,         gimnasio,   "8:00-14:00")
    empleado2=Empleado(25492555, "Pedro",   "Gonzalez", "351444333","Estrada 166",  "Hola123456",     2,         paddle,     "8:00-14:00")
    empleado3=Empleado(40111222, "David",   "Gimenez",  "351444666","9 de Julio 25","David321",       3,         futbol,     "14:00-22:00")
    empleado4=Empleado(14555621, "Vilma",   "Stefanini","351444666","San Juan 1122","Vilma28",        4,         futbol,     "14:00-22:00")
    ####################################################################################################################################

    
    ########################################  PROVEEDORES  ##########################################
    proveedor1=Proveedor(1,"Ricardo","DECATLON","03584672268",empleado1)
    
    proveedor2=Proveedor(2,"Manuel","ADIDAS",   "03584672338",empleado1)
   
   
   
    ########################################################################################

    
    
    ########################################  PRODUCTOS  ###############################################
    
                          #ID| ID PROVEEDOR  | NOMBRE      | MARCA   |DESCRIPCION        |PRECIO  |STOCK   | FOTO
    cantimplora = Producto( 1 ,     1,       "Cantiplora","Decatlon","1 ltrs frio/calor",1800     ,50,     "cantimplora.jpg" )
    zapatilla   = Producto( 2 ,     2,       "Zapatilla", "Adidas",  "talle 42",         5400,     15,     "zapaAdidas.jpg")
    #addProducto(conn1,producto)
    ##updateProducto(conn1,producto)
    #deleteProducto(conn1,producto)
    #prod=selectProducto(conn1,producto)
    #print(prod)
    #data=selectAll(conn1)
    #print(data)
    
    
    
    ########################################################################################
    #SIMULACION DE OBTENCION DE DATOS DEL FORMULARIO


    #VARIABLES ESTATICAS
      
    #idCliente =1   idCliente (se asigna automatico en bd)
    #socio     =1   =true socio (funcionalidad futura)
    #usuario rellena campos requeridos y pulsa Submit

    #                                                       DATOS CAPTURADOS                     |necesarias para contructor de la clase Cliente
    #                   dni   |  nombre   | apellido  | telefono   | direccion     |contraseña   |
    cliente =Cliente(33000111,"ricardo"  ,"montaner",   "123456"  ,"estrada 1433", "admin123",   1 , 1)


    











instalacion=Instalacion(1,"gym",20)

empleado= Empleado(5,"pablo","carrizo","123456","maipo 100","admin123",23,instalacion,"horario")
provedor= Proveedor(1,"mario","tate","123456",empleado)

usuarioLogged=ModelUser.login(conn,empleado)
print(usuarioLogged)

#ModelUser.addCliente(conn,cliente)
#ModelUser.addUser(conn,user2)
#ModelUser.addEmpleado(conn,empleado)
#print (empleado.getId(),empleado.getIdEmpleado(), empleado.getIdInstalacion(),empleado.getHorario())