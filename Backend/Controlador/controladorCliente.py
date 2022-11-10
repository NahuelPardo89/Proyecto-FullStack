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
        if nombre!=cliente.getNombre()and nombre!="":
            cliente.setNombre(nombre)
        
        if apellido!=cliente.getApellido()and apellido != "":
            cliente.setApellido(apellido)
        
        if telefono!=cliente.getTel()and telefono != "":
            cliente.setTel(telefono)
        
        if direccion!=cliente.getDireccion()and direccion != "":
            print("direccion=",direccion)
            cliente.setDireccion(direccion)
        
        if contrasena!=cliente.getContraseña()and contrasena != "":
            print("contraseña=",contrasena)
            cliente.setContraseña(contrasena)

        ModelUser.updateUser(conn,cliente)
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
        return cliente
        
    else:
        return None
#uso solo de pruebas
if __name__=="__main__":
           
    i=1
    while i!=0:
        
        print("presione 1 para registrar cliente\n presione 2 para loguearse\n ")
        aux=int(input("ingrese accion:  "))
        if aux==1 :
            var=regitroCliente()
            if var:
                print("Registro existoso")
            else:
                print("error de registro")    
        elif aux==2:
            loggedUser=login()
            if loggedUser!=None:
                print("login existoso")
                print("presione 1 para modificar datos\n presione 2 para eliminar usuario")
                aux=int(input("ingrese accion: "))
                if aux==1:
                    loggedUser=updateCliente(loggedUser)
                    if loggedUser:
                        print("cliente actualizado")

                    else:
                        print("error de actualizacion")
                elif aux==2:
                    loggedUser=deleteCliente(loggedUser.getId())
                    if loggedUser:
                        print("cliente removido")
                    else:
                     print("error de eliminacion")  
            else:
                print("usuario o contraseña incorrecta")
    
        i=int(input("si desea salir pulse 0"))    
        











