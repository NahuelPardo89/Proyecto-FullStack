#from conexionDb import Conexion
from .clases.users import User, Cliente,Empleado


###
#conn = Conexion()
#conn1 = conn.getConn()
####
class ModelUser:
    @classmethod
    def login(self, conn, user):
        try:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT * FROM users WHERE idUser=%s", (user.getId(),))
            row = cursor.fetchone()
            if row != None:
                if user.getContraseña() == row[5]:
                    user = User(row[0], row[1], row[2],
                                   row[3], row[4], True)
                    return user
            else:
                return None
        except Exception as ex:
            raise Exception(ex)

    def addUser(conn, user):
        cursor = conn.cursor()
        cursor.execute("INSERT INTO `users` (`idUser`, `Nombre`, `apellido`, `Telefono`, `direccion`, `contraseña`) VALUES (%s,%s,%s,%s,%s,%s)", (
        user.getId(), user.getNombre(), user.getApellido(), user.getTel(),user.getDireccion(),user.getContraseña()))
        conn.commit()
        

    def updateUser(conn, user):
        cursor = conn.cursor()
        cursor.execute("""
                UPDATE users
                SET  Nombre=%s,
                    apellido=%s,
                    Telefono=%s,
                    direccion=%s,
                    contraseña=%s
                WHERE idUser=%s
            """, (user.getNombre(), user.getApellido(), user.getTel(),user.getDireccion(),user.getContraseña(),user.getId()))
        conn.commit()
        

    def deleteUser(conn, user):

        cursor = conn.cursor()
        cursor.execute("DELETE FROM users WHERE idUser=%s",
                       (user.getId(),))
        conn.commit()
        

    def selectOneUser(conn, id):
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM users WHERE idUser=%s", (id,))
        fila = cursor.fetchall()
        user=User(fila[0],fila[1],fila[2],fila[3],fila[4],fila[5])
        
        return user

    def selectAllUsers(conn):
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users")
        data = cursor.fetchall()
        
        return data
    ##methods####

    ######################### CLIENTES###############################


    def addCliente(conn, cliente):
        cursor = conn.cursor()
        cursor.execute("INSERT INTO `clientes` (`idCliente`, `idUser`, `socio`) VALUES (%s,%s,%s)", (
            cliente.getIdCliente(), cliente.getId(), cliente.getSocio()))
        conn.commit()
        

    def updateCliente(conn, cliente):
        cursor = conn.cursor()
        cursor.execute("""
                UPDATE clientes
                SET  socio=%s
                WHERE idCliente=%s
            """, (cliente.getSocio(), cliente.getIdCliente()))
        conn.commit()
        

    def deleteCliente(conn, cliente):

        cursor = conn.cursor()
        cursor.execute("DELETE FROM clientes WHERE idCliente=%s",
                       (cliente.getIdCliente(),))
        conn.commit()
        

    def selectOneCliente(conn, id):
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM clientes WHERE idCliente=%s",
                       (id,))
        clienteData = cursor.fetchall()
        cursor.execute("SELECT * FROM users WHERE idUser=%s",
                       (clienteData[1],))
        userData= cursor.fetchall()
        cliente=Cliente(userData[0],userData[1],userData[2],userData[3],userData[4],userData[5],clienteData[0],clienteData[2])
        return cliente

    def selectAllCliente(conn):
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM clientes")
        data = cursor.fetchall()
        
        return data

    ######################### EMPLEADOS###############################

    def addEmpleado(conn, empleado):
        cursor = conn.cursor()
        cursor.execute("INSERT INTO `empleados` (`idEmpleado`, `idUser`, `idInstalacion`, `Horario`) VALUES (%s,%s,%s,%s)", (
        empleado.getIdEmpleado(), empleado.getId(),empleado.getIdInstalacion(), empleado.getHorario()))

        conn.commit()
       

    def updateEmpleado(conn, empleado):
        cursor = conn.cursor()
        cursor.execute("""
                UPDATE empleados
                SET  idDepartamento=%s,
                    idInstalacion=%s,
                    Horario=%s
                WHERE idEmpleado=%s
            """, (empleado.getIdDepartamento(), empleado.getIdInstalacion(), empleado.getHorario(),empleado.getIdEmpleado()))
        conn.commit()
        

    def deleteEmpleado(conn, empleado):

        cursor = conn.cursor()
        cursor.execute("DELETE FROM empleados WHERE idEmpleado=%s",
                       (empleado.getIdEmpleado(),))
        conn.commit()
        

    def selectOneEmpleado(conn, empleado):
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM empleados WHERE idEmpleado=%s",
                       (empleado.getIdEmpleado(),))

        empleadoData = cursor.fetchall()
        cursor.execute("SELECT * FROM users WHERE idUser=%s",
                       (empleadoData[1],))
        userData= cursor.fetchall()
        empleado=Empleado(userData[0],userData[1],userData[2],userData[3],userData[4],userData[5],empleadoData[0],empleadoData[2],empleadoData[3])
        
        return empleado

    def selectAllEmpleado(conn):
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM empleados")
        data = cursor.fetchall()
        
        return data

    # producto = Producto(5,1,"zpa","adidas","chica",23,2,"fototruca.jpg")
    # addProducto(conn1,producto)
    # updateProducto(conn1,producto)
    # deleteProducto(conn1,producto)
    # prod=selectProducto(conn1,producto)
    # print(prod)
    # data=selectAll(conn1)
    # print(data)
#persona = Persona(33222333, "Oscar", "sierra","3584372604","roma 111","admin")
    # addPersona(conn1,persona)
    # updatePersona(conn1,persona)
    # a=selectAllPersona(conn1)
    # print(a)
    # deletePersona(conn1,persona)
    # cliente= Cliente(persona.getId(),persona.getNombre(),persona.getApellido(),persona.getTel(),persona.getDireccion(),persona.getContraseña(),5,25)
    # print(persona.getId())
    # addCliente(conn1,cliente)
    # updateCliente(conn1,cliente)
    # print(cliente.getId())
    # deleteCliente(conn1,cliente)
    # fila=selectOneCliente(conn1,cliente)
    # print(fila)

    # empleado= Empleado(persona.getId(),persona.getNombre(),persona.getApellido(),persona.getTel(),persona.getDireccion(),persona.getContraseña(),7,1,2,"updated")

    # print(empleado.getId(),empleado.getNombre(),empleado.getApellido(),empleado.getTel(),empleado.getDireccion(),empleado.getContraseña(),empleado.getIdDepartamento(),empleado.getIdInstalacion(),empleado.getHorario())

    # addEmpleado(conn1,empleado)
    # updateEmpleado(conn1,empleado)
    # deleteEmpleado(conn1,empleado)

    # a=selectAllEmpleado(conn1)

    # print(a)
#a=(modelPersona.login(conn1,persona))

#print(a)
