from controladorCliente import *
from controladorAdmin import *
from os import system


if __name__=="__main__":
           
    i=1
    while i!=0:
        #CRUD CLIENTE
        system("cls")
        print("para ingresar al menu empleado puse [1] para ingresar al menu clientes pulse[2]")
        aux=int(input("ingrese accion:  "))
        if aux==1:
            print ("""&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&""")
            print ("""&&&&&&&&&&&&& ADMIN &&&&&&&&&&&&&""")
            print ("""&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&""")
            print("presione [1] para registrar empleado\npresione [2] para loguearse\n ")
            print ("""&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&""")
            aux1=int(input("ingrese accion:  "))
            if aux1==1:
                var=registrarEmpleado()
                if var:
                    print("Registro existoso")
                else:
                    print("error de registro") 
            elif aux1==2:
                system("cls")
                print ("""&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&""")
                print ("""&&&&&&&&&&&& LOGIN ADMIN &&&&&&&&&&""")
                print ("""&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&""")
                loggedUser=loginAdmin()
                if loggedUser!=None:
                    system("cls")
                    print("Bienvenido "+ loggedUser.getNombre().upper()+", "+loggedUser.getApellido().upper()) 
                    print ("""&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&""")
                    print("presione [1] para munu usuario\npresione [2] para menu gestion")
                    print ("""&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&""")
                    aux2=int(input("ingrese accion: "))
                    if aux2==1:
                        print("presione [1] para modificar datos de usuario\npresione [2] para eliminar usuario")
                        aux3=int(input("ingrese accion: "))
                        if aux3==1:
                            system("cls")
                            print ("""&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&""")
                            print ("""&&&&&&&& MODIFICAR DATOS &&&&&&&&&&&""")
                            print ("""&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&""")
                            id=str(loggedUser.getId())
                            loggedUser=updateEmpleado(loggedUser)
                            if loggedUser:
                                print("cliente DNI N°: ["+id+"] actualizado")

                            else:
                                print("error de actualizacion")
                        elif aux3==2:
                            id=str(loggedUser.getId())
                            loggedUser=deleteEmpleado(loggedUser)
                            if loggedUser:
                                print("cliente DNI N° "+id+" removido")
                            else:
                                print("error de eliminacion")  
                    elif aux2==2:
                        system("cls")
                        print ("""&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&""")
                        print ("""&&&&&&&& MENU GESTION &&&&&&&&&&&""")
                        print ("""&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&""")
                        i=1
                        while i!=0:
                            print ("para listar productos presione [1], para agregar productos presione [2], para eliminar productos presione [3]")
                            aux4=int(input("ingrese accion: "))
                            if aux4==1:
                                mostrarProductos()
                            elif aux4==2:
                                registrarProd()
                            elif aux4==3:
                                deleteProducto()
                            i=int(input("si desea volver al menu presion [1], si desea salir presione [0]"))



                else:
                    print("usuario o contraseña incorrecta")

        if aux==2:
            print ("""&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&""")
            print ("""&&&&&&&&&&&&& CLIENTES &&&&&&&&&&&&&""")
            print ("""&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&""")
            print("presione [1] para registrarse\npresione [2] para loguearse\n ")
            print ("""&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&""")
            aux1=int(input("ingrese accion:  "))
            
            if aux1==1 :
                var=regitroCliente()
                if var:
                    print("Registro existoso")
                else:
                    print("error de registro")    
            elif aux1==2:
                system("cls")
                print ("""&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&""")
                print ("""&&&&&&&&&&&&&& LOGIN &&&&&&&&&&&&&&&""")
                print ("""&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&""")
                loggedUser=login()
                if loggedUser!=None:
                    system("cls")
                    print("Bienvenido "+ loggedUser.getNombre().upper()+", "+loggedUser.getApellido().upper()) 
                    print ("""&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&""")
                    print("presione [1] para modificar datos\npresione [2] para eliminar usuario")
                    print ("""&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&""")
                    aux=int(input("ingrese accion: "))
                    if aux==1:
                        system("cls")
                        print ("""&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&""")
                        print ("""&&&&&&&& MODIFICAR DATOS &&&&&&&&&&&""")
                        print ("""&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&""")
                        id=str(loggedUser.getId())
                        
                        loggedUser=updateCliente(loggedUser)
                        if loggedUser:
                            print("cliente DNI N°: ["+id+"] actualizado")

                        else:
                            print("error de actualizacion")
                    elif aux==2:
                        id=str(loggedUser.getId())
                        loggedUser=deleteCliente(loggedUser.getId())
                        if loggedUser:
                            print("cliente DNI N° "+id+" removido")
                        else:
                            print("error de eliminacion")  
                else:
                    print("usuario o contraseña incorrecta")
    
        i=int(input("Si desea salir pulse [0]\nSi desea continuar pulse cualquier numero:\n"))