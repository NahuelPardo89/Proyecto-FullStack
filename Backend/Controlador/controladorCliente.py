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
        
        #validacion de dni
        i=True
        while i:
            dni= int(input('Ingrese numero de DNI:\n'))
            if dni>=1000000 and dni<100000000:
                i=False
            else:
                print("debe ingresar un documento valido")
        
        #VERIFICO SI YA EXISTE EL USUARIO
        cliente= ModelUser.selectOneUser(conn,dni)
        if (cliente == None):

            nombre=input('ingrese nombre:\n')
            apellido=input('ingrese apellido:\n')
            telefono=input('ingrese numero de telefono:\n')
            direccion=input('ingrese direccion:\n')

            i=True
            while i:
                contrasena=input('íngrese contraseña:\n')
                if len(contrasena)>=6 and len(contrasena)<=16 :
                    i=False
                else:
                    print("debe ingresar una contraseña valida(de 6 a 16 caracteres)")

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
            print("el usuario ya existe")
            return False

    
    ########################################################################################

def updateCliente(cliente):
    
    db=Conexion()
    conn= db.connection
    if  conn.is_connected():
        print("Si no desea modificar el campo presione [ENTER]")
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
            cliente.setDireccion(direccion)
        
        if contrasena!=cliente.getContraseña()and contrasena != "":
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

    
        











