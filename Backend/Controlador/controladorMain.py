from controladorCliente import *
from os import system


if __name__=="__main__":
           
    i=1
    while i!=0:
        #CRUD CLIENTE
        system("cls")
        print ("""&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&""")
        print ("""&&&&&&&&&&&&& CLIENTES &&&&&&&&&&&&&""")
        print ("""&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&""")
        print("presione [1] para registrarse\npresione [2] para loguearse\n ")
        print ("""&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&""")
        aux=int(input("ingrese accion:  "))
        
        if aux==1 :
            var=regitroCliente()
            if var:
                print("Registro existoso")
            else:
                print("error de registro")    
        elif aux==2:
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