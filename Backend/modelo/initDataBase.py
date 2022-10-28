from sys import path
#PARA IMPORTAR DESDE MODELO
path.append('C:\\Users\\nanit\\Desktop\\proyecto\\Proyecto-FullStack\\Backend')

#CONEXION
from modelo.conexionDb import Conexion

#MODELOS
from modelo.modelProducto import ModelProducto
from modelo.modelUser import ModelUser
from modelo.modelInstalacion import ModelInstalacion
from modelo.modelProveedor import ModelProveedor

#CLASES
from modelo.clases.users import Empleado
from modelo.clases.proveedor import Proveedor
from modelo.clases.producto import Producto
from modelo.clases.instalaciones import Instalacion

class InitDb():
    def __init__(self):

        #inicializacion de bd

        db=Conexion()
        conn=db.connection
        if  conn.is_connected():
            self.database=db
            #CARGA DE DATOS: EMPLEADOS, PRODUCTOS, INSTALACIONES, PROVEEDORES

            #########################################  TABLA INSTALACIONES  ###########################
                                # ID | NOMBRE   |PRECIO USO HORA
            gimnasio=Instalacion( 1, "Gimnasio",400)
            paddle  =Instalacion( 2, "PADDLE",  1000)
            futbol  =Instalacion( 3, "Gimnasio",2000)
            
            ######################################################################################
            
            
            #########################################  TABLA EMPELADOS  ########################################################## ##############                                                           
                            #   DNI     | NOMBRE  | APELLIDO  |TELEFONO   |DIRECCION       CONTRASEÑA| IDEMPLEADO | INSTALACION  |HORARIO
            empleado1=Empleado(25492666, "Juana",   "funes",    "351461325","Maipu 166",    "JuanaFu25",      1,         gimnasio,   "8:00-14:00")
            empleado2=Empleado(25492555, "Pedro",   "Gonzalez", "351444333","Estrada 166",  "Hola123456",     2,         paddle,     "8:00-14:00")
            empleado3=Empleado(40111222, "David",   "Gimenez",  "351444666","9 de Julio 25","David321",       3,         futbol,     "14:00-22:00")
            empleado4=Empleado(14555621, "Vilma",   "Stefanini","351444666","San Juan 1122","Vilma28",        4,         futbol,     "14:00-22:00")
            
            ####################################################################################################################################

            
            ########################################  TABLA PROVEEDORES  ##########################################
                            #  ID| NOMBRE   |MARCA     | TELEFONO   |EMPLEADO ASIGNADO
            proveedor1=Proveedor(1, "Ricardo","DECATLON","03584672268",empleado1)
            proveedor2=Proveedor(2, "Manuel", "ADIDAS",  "03584672338",empleado1)
                
            ######################################################################################################

            
            
            ########################################  TABLA PRODUCTOS  ##############################################################
            
                                #ID| ID PROVEEDOR  | NOMBRE      | MARCA   |DESCRIPCION        |PRECIO  |STOCK   | FOTO
            cantimplora = Producto( 1 ,     1,       "Cantiplora","Decatlon","1 ltrs frio/calor",1800     ,50,     "cantimplora.jpg" )
            zapatilla   = Producto( 2 ,     2,       "Zapatilla", "Adidas",  "talle 42",         5400,     15,     "zapaAdidas.jpg")

            #########################################################################################################################    
            
            
            
            #################################### INSERT A BASE DE DATOS##################################################
        
            #INSERT INSTALACION
            #ModelInstalacion.addInstalacion(conn,instalacion) falta implementar
        
            
            #INSERT EMPLEADOS
            ModelUser.addEmpleado(conn,empleado1)
            ModelUser.addEmpleado(conn,empleado2)
            ModelUser.addEmpleado(conn,empleado3)
            ModelUser.addEmpleado(conn,empleado4)
            
            #INSERT PROVEEDORES
            #ModelProveedor.addProveedor(conn,proveedor1) METODOS SIN IMPLEMENTAR
            #ModelProveedor.addProveedor(conn,proveedor2)
            
            #INSERT PRODUCTOS
            ModelProducto.addProducto(conn,cantimplora)
            ModelProducto.addProducto(conn,zapatilla)

            #devuelvo database
            
    
    
    

    
    