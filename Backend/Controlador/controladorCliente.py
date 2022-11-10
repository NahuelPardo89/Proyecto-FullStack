from sys import path
#PARA IMPORTAR DESDE MODELO
path.append('C:/Users/nanit/Desktop/proyecto/Proyecto-FullStack')

#DATABASE
from Backend.modelo.database.conexionDb import Conexion
#MODELOS
from Backend.modelo.modelUser import ModelUser
#CLASES
from Backend.modelo.clases.users import Cliente


########################################################################################
#SIMULACION DE OBTENCION DE DATOS DEL FORMULARIO REGISTRO
def regitroCliente():
    #CONEXION CON BASE DE DATOS ampaDB
    db=Conexion()
    conn= db.connection
    if  conn.is_connected():
        #simulacion de formulario de Registro
        dni= int(input('Ingrese numero de DNI:\n'))
        #VERIFICO SI YA EXISTE EL USUARIO
        cliente= ModelUser.selectOneCliente(conn,dni)
        if (cliente != None):

            nombre=input('ingrese nombre:\n')
            apellido=input('ingrese apellido:\n')
            telefono=input('ingrese numero de telefono:\n')
            direccion=input('ingrese direccion:\n')
            contrasena=input('íngrese contraseña:\n')
            #usuario rellena campos requeridos y pulsa enviar
            #VARIABLES ESTATICAS
        
            #idCliente =1   idCliente (se asigna automatico en bd)
            #socio     =1   =true socio (funcionalidad futura)
            #                                                       DATOS CAPTURADOS                     |necesarias para contructor de la clase Cliente
            #                   dni   |  nombre   | apellido  | telefono   | direccion     |contraseña   |
            cliente =Cliente(   dni,   nombre  ,   apellido,   telefono ,  direccion,       contrasena,   1 , 1)
            
            #AGREGO CLIENTE A LA BASE DE DATOS
            ModelUser.addCliente(conn,cliente)
            conn.close()
            
            return True
        else:
            
            return False

    
    ########################################################################################

def updateCliente(cliente):
    
    db=Conexion()
    conn= db.connection
    if  conn.is_connected():
        
        nombre=input('ingrese nombre:\n')
        apellido=input('ingrese apellido:\n')
        telefono=input('ingrese numero de telefono:\n')
        direccion=input('ingrese direccion:\n')
        contrasena=input('íngrese contraseña:\n')
        #usuario modifica los campos deseados y pulsa enviar
        if nombre!=cliente.getNombre():
            cliente.setNombre(nombre)
        
        if apellido!=cliente.getApellido():
            cliente.setApellido(apellido)
        
        if telefono!=cliente.getTel():
            cliente.setTel(telefono)
        
        if direccion!=cliente.getDireccion():
            cliente.setDireccion(direccion)
        
        if contrasena!=cliente.getContraseña():
            cliente.setContraseña(contrasena)

        ModelUser.updateCliente(conn,cliente)
        conn.close()
        return True
    else:
        return False
        
    
def deleteCliente(id):
    db=Conexion()
    conn= db.connection
    if  conn.is_connected():
        ModelUser.deleteCliente(conn,id)
        conn.close()
        return True
    else:
        return False

        
def login():
    dni=int(input("Ingrese DNI:\n"))
    contrasena=input("Ingrese contraseña:\n")
    db=Conexion()
    conn= db.connection
    if  conn.is_connected():
    
    
        cliente= ModelUser.login(conn,dni,contrasena)
        if cliente!=None:
            return True
        else:
            return False
    else:
        return None

if __name__=="__main__":
           
    i=1
    while i!=0:
        print("1 registro-2 updateCliente -3 deleteCliente -4 login")
        #aux=int(input("ingrese accion\n"))
        aux=deleteCliente(34414604)
        if aux:
            print("eliminado existoso") 
        i=int(input("si desea salir pulse 0"))    
        











