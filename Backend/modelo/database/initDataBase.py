from sys import path
#PARA IMPORTAR DESDE MODELO
path.append('C:\\Users\\nanit\\Desktop\\proyecto\\Proyecto-FullStack\\Backend')




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
    def __init__(self,conn):

        

        
        
        if  conn.is_connected():
            
            #CARGA DE DATOS: EMPLEADOS, PRODUCTOS, INSTALACIONES, PROVEEDORES

            #########################################  TABLA INSTALACIONES  ###########################
                                # ID | NOMBRE   |PRECIO USO HORA
            gimnasio= Instalacion( 1, "Gimnasio A.M.P.A",2800)
            paddle  = Instalacion( 2, "Cancha de Paddle A.M.PA.",  1000)
            futbol  = Instalacion( 3, "Cancha de Futbol A.M.P.A.",1000)
            basquet = Instalacion( 4, "Cancha de Basquet A.M.P.A.",1000)
            salon_eventos  = Instalacion( 5, "Salon de eventos A.M.P.A.",20000)

            
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
            
                                  #ID| ID PROVEEDOR   | NOMBRE           | MARCA       |DESCRIPCION        |PRECIO  |STOCK   | FOTO
            cantimplora = Producto( 1 ,     1,        "BotellaTérmica"  ,"Everlast"   ,"1 ltrs frio/calor"  ,2584     ,50,    "botella-everlast-entrenamiento.jpg" )
            zapatilla   = Producto( 2 ,     2,        "Zapatilla"       ,"NikeAirMax" ,"talle 42"           ,35899    , 5,    "nike-airmax-correlate.jpg")
            zapatilla   = Producto( 3 ,     2,        "Zapatilla"       ,"NikeAirMax" ,"talle 41"           ,35899    , 5,    "nike-airmax-correlate.jpg")
            zapatilla   = Producto( 4 ,     2,        "Zapatilla"       ,"NikeAirMax" ,"talle 40"           ,35899    , 5,    "nike-airmax-correlate.jpg")
            zapatilla   = Producto( 5 ,     2,        "Zapatilla"       ,"NikeAirMax" ,"talle 39"           ,35899    , 2,    "nike-airmax-correlate.jpg")
            kitfitness  = Producto( 6 ,     1,        "KitFitnessHome"  ,"Everlast"   ,"kit 3 piezas"       ,9215     ,15,    "Kit-fitness.jpg")
            gorrotenis  = Producto( 7 ,     2,        "GorroTenisBlade" ,"Wilson"     ,"Gorro tenis"        ,4799     ,10,    "gorra-tenis-wilson.jpg")
            shortadidas = Producto( 8 ,     2,        "ShortAdidasAero" ,"Adidas"     ,"Short Aero Ready S" ,10599    , 5,    "short-adidas.jpg")
            shortadidas = Producto( 9 ,     2,        "ShortAdidasAero" ,"Adidas"     ,"Short Aero Ready M" ,10599    , 5,    "short-adidas.jpg")
            shortadidas = Producto(10 ,     2,        "ShortAdidasAero" ,"Adidas"     ,"Short Aero Ready L" ,10599    , 5,    "short-adidas.jpg")
            shortadidas = Producto(11 ,     2,        "ShortAdidasAero" ,"Adidas"     ,"Short Aero Ready XL",10599    , 5,    "short-adidas.jpg")
            raquetatenis= Producto(12 ,     1,        "RaquetaTenis"    ,"Wilson"     ,"Raqueta Wilson"     ,69999    ,10,    "raqueta-de-tenis-wilson.jpg")
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
            
    
    
    

    
    
