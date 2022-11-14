from sys import path
#PARA IMPORTAR DESDE MODELO
path.append('C:/Users/nanit/Desktop/proyecto/Proyecto-FullStack')
#DATABASE
from Backend.modelo.database.conexionDb import Conexion
#MODELOS
from Backend.modelo.modelUser import ModelUser
from Backend.modelo.modelProducto import ModelProducto
from Backend.modelo.modelInstalacion import ModelInstalacion
from Backend.modelo.modelProveedor import ModelProveedor
#CLASES

from Backend.modelo.clases.producto import Producto
from Backend.modelo.clases.users import Empleado

def registrarEmpleado():
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
        empleado= ModelUser.selectOneUser(conn,dni)
        if (empleado == None):

            nombre=input('ingrese nombre:\n')
            apellido=input('ingrese apellido:\n')
            telefono=input('ingrese numero de telefono:\n')
            direccion=input('ingrese direccion:\n')
            instalacion=int(input('ingrese id instalacion\n'))
            horario= input('ingrese horario(8-14 o 14-22\n')

            i=True
            while i:
                contrasena=input('íngrese contraseña:\n')
                if len(contrasena)>=6 and len(contrasena)<=16 :
                    i=False
                else:
                    print("debe ingresar una contraseña valida(de 6 a 16 caracteres)")

            #usuario rellena campos requeridos y pulsa enviar
            #VARIABLES ESTATICAS
        
            #idEmpleado =1   idEmpleado (se asigna automatico en bd)
            
            #                                                       DATOS CAPTURADOS                     
            #                   dni   |  nombre   | apellido  | telefono   | direccion     |contraseña   | idEmpleado| ideinstalacion |horario
            empleado =Empleado(   dni,   nombre  ,   apellido,   telefono ,  direccion,       contrasena,   1,         instalacion,    horario)
            
            #AGREGO CLIENTE A LA BASE DE DATOS
            ModelUser.addEmpleado(conn,empleado)
            conn.close()
            
            return True
        else:
            print("el usuario ya existe")
            return False
def updateEmpleado(empleado):
    
    db=Conexion()
    conn= db.connection
    if  conn.is_connected():
        print("Si no desea modificar el campo presione [ENTER]")
        nombre=input('ingrese nombre:\n')
        apellido=input('ingrese apellido:\n')
        telefono=input('ingrese numero de telefono:\n')
        direccion=input('ingrese direccion:\n')
        contrasena=input('íngrese contraseña:\n')
        instalacion=input('ingrese id instalacion\n')
        horario= input('ingrese horario(8:00-14:00 o 14:00-22:00\n')
        
        #usuario modifica los campos deseados y pulsa enviar
        if nombre!=empleado.getNombre()and nombre!="":
            empleado.setNombre(nombre)
        
        if apellido!=empleado.getApellido()and apellido != "":
            empleado.setApellido(apellido)
        
        if telefono!=empleado.getTel()and telefono != "":
            empleado.setTel(telefono)
        
        if direccion!=empleado.getDireccion()and direccion != "":
            empleado.setDireccion(direccion)
        
        if contrasena!=empleado.getContraseña()and contrasena != "":
            empleado.setContraseña(contrasena)
        
        if instalacion!=empleado.getIdInstalacion()and instalacion != "":
            empleado.setIdInstalacion(int(instalacion))
        
        if horario!=empleado.getHorario()and horario != "":
            empleado.setHorario(horario)

        ModelUser.updateUser(conn,empleado)
        ModelUser.updateEmpleado(conn,empleado)
        conn.close()
        return True
    else:
        return False

def deleteEmpleado(id):
    db=Conexion()
    conn= db.connection
    if  conn.is_connected():
        ModelUser.deleteEmpleado(conn,id)
        conn.close()
        return True
    else:
        return False
def loginAdmin():
    dni=int(input("Ingrese DNI:\n"))
    contrasena=input("Ingrese contraseña:\n")
    db=Conexion()
    conn= db.connection
    if  conn.is_connected():
        cliente= ModelUser.loginAdmin(conn,dni,contrasena)
        return cliente
        
    else:
        return None

def mostrarProductos():
    db=Conexion()
    conn= db.connection
    data=ModelProducto.selectAllProducto(conn)
    for i in data:
        print(i)

def mostrarInstalaciones():
    db=Conexion()
    conn= db.connection
    data=ModelInstalacion.selectAllInstalacion(conn)
    for i in data:
        print(i)
def mostrarProveedores():
    db=Conexion()
    conn= db.connection
    data=ModelProveedor.selectAllProveedores(conn)
    for i in data:
        print(i)

def registrarProd():
    proveedor=int(input("ingrese id proveedor"))
    nombre=input('ingrese nombre:\n')
    marca=input('ingrese marca:\n')
    description=input('ingrese description:\n')
    precio=input('ingrese precio:\n')
    stock=input('ingrese stock:\n')
    foto=input('ingrese foto:\n')
    db=Conexion()
    conn= db.connection  
    producto=Producto(1,proveedor,nombre,marca,description,precio,stock,foto)
    ModelProducto.addProducto(conn,producto)
def updateProducto(producto):
    
    db=Conexion()
    conn= db.connection
    if  conn.is_connected():
        print("Si no desea modificar el campo presione [ENTER]")
        proveedor=(input("ingrese id proveedor"))
        nombre=input('ingrese nombre:\n')
        marca=input('ingrese marca:\n')
        description=input('ingrese description:\n')
        precio=input('ingrese precio:\n')
        stock=input('ingrese stock:\n')
        foto=input('ingrese foto:\n')
        
        #usuario modifica los campos deseados y pulsa enviar
        if proveedor!=producto.getIdProveedor() and proveedor!="":
            producto.setIdProveedor(int(proveedor))
        
        if nombre!=producto.getNombre() and nombre!="":
            producto.setINombre(nombre)
        
        if marca!=producto.getMarca() and marca!="":
            producto.setMarca(marca)
        
        if description!=producto.getDescripcion() and description!="":
            producto.setDescripcion(description)
        
        if precio!=producto.getPrecio() and precio!="":
            producto.setPrecio(precio)
        
        if stock!=producto.getStock() and stock!="":
            producto.setStock(stock)
        
        if foto!=producto.getFoto() and foto!="":
            producto.setFoto(foto)
        


        ModelProducto.updateProducto(conn, producto)
        conn.close()
        return True
    else:
        return False
def deleteProducto():
    db=Conexion()
    conn= db.connection
    id=input('ingrese id producto:\n')
    producto=ModelProducto.selectOneProducto(conn,id)
    if  conn.is_connected():
        ModelProducto.deleteProducto(conn,producto)
        conn.close()
        return True
    else:
        return False

if __name__=="__main__":
   #a=loginAdmin()
    db=Conexion()
    conn= db.connection

    producto=ModelProducto.selectOneProducto(conn,15)
    updateProducto(producto)