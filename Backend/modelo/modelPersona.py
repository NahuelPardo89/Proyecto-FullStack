#from conexionDb import Conexion
from .clases.persona import Persona


###
#conn = Conexion()
#conn1 = conn.getConn()
####
class modelPersona:
    @classmethod
    def login(self, conn, persona):
        try:
            cursor = conn.connection.cursor()
            cursor.execute(
                "SELECT * FROM personas WHERE idPersona=%s", (persona.getId(),))
            row = cursor.fetchone()
            if row != None:
                if persona.getContraseña() == row[5]:
                    user = Persona(row[0], row[1], row[2],
                                   row[3], row[4], True)
                    return user
            else:
                return None
        except Exception as ex:
            raise Exception(ex)

    def addPersona(conn, persona):
        cursor = conn.connection.cursor()
        cursor.execute("INSERT INTO `personas` (`idPersona`, `Nombre`, `apellido`, `Telefono`, `direccion`, `contraseña`) VALUES (%s,%s,%s,%s,%s,%s)", (
        persona.getId(), persona.getNombre(), persona.getApellido(), persona.getTel(),persona.getDireccion(),persona.getContraseña()))
        conn.commit()
        conn.close()

    def updatePersona(conn, persona):
        cursor = conn.cursor()
        cursor.execute("""
                UPDATE personas
                SET  Nombre=%s,
                    apellido=%s,
                    Telefono=%s,
                    direccion=%s,
                    contraseña=%s
                WHERE idPersona=%s
            """, (persona.getNombre(), persona.getApellido(), persona.getTel(),persona.getDireccion(),persona.getContraseña(),persona.getId()))
        conn.commit()
        conn.close()

    def deletePersona(conn, persona):

        cursor = conn.cursor()
        cursor.execute("DELETE FROM personas WHERE idPersona=%s",
                       (persona.getId(),))
        conn.commit()
        conn.close()

    def selectOnePersona(conn, persona):
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM personas WHERE idPersona=%s", (persona.getId(),))
        fila = cursor.fetchall()
        conn.close()
        return fila

    def selectAllPersona(conn):
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM personas")
        data = cursor.fetchall()
        conn.close()
        return data
    ##methods####

    ######################### CLIENTES###############################


    def addCliente(conn, cliente):
        cursor = conn.cursor()
        cursor.execute("INSERT INTO `clientes` (`idCliente`, `idPersona`, `socio`) VALUES (%s,%s,%s)", (
            cliente.getIdCliente(), cliente.getId(), cliente.getSocio()))
        conn.commit()
        conn.close()

    def updateCliente(conn, cliente):
        cursor = conn.cursor()
        cursor.execute("""
                UPDATE clientes
                SET  socio=%s
                WHERE idCliente=%s
            """, (cliente.getSocio(), cliente.getIdCliente()))
        conn.commit()
        conn.close()

    def deleteCliente(conn, cliente):

        cursor = conn.cursor()
        cursor.execute("DELETE FROM clientes WHERE idCliente=%s",
                       (cliente.getIdCliente(),))
        conn.commit()
        conn.close()

    def selectOneCliente(conn, cliente):
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM clientes WHERE idCliente=%s",
                       (cliente.getIdCliente(),))
        fila = cursor.fetchall()
        conn.close()
        return fila

    def selectAllCliente(conn):
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM clientes")
        data = cursor.fetchall()
        conn.close()
        return data

    ######################### EMPLEADOS###############################

    def addEmpleado(conn, empleado):
        cursor = conn.cursor()
        cursor.execute("INSERT INTO `empleados` ( `idPersona`, `idDepartamento`, `idInstalacion`, `Horario`) VALUES (%s,%s,%s,%s)", (
        empleado.getId(), empleado.getIdDepartamento(), empleado.getIdInstalacion(), empleado.getHorario()))

        conn.commit()
        conn.close()

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
        conn.close()

    def deleteEmpleado(conn, empleado):

        cursor = conn.cursor()
        cursor.execute("DELETE FROM empleados WHERE idEmpleado=%s",
                       (empleado.getIdEmpleado(),))
        conn.commit()
        conn.close()

    def selectOneEmpleado(conn, empleado):
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM empleados WHERE idEmpleado=%s",
                       (empleado.getIdEmpleado(),))
        fila = cursor.fetchall()
        conn.close()
        return fila

    def selectAllEmpleado(conn):
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM empleados")
        data = cursor.fetchall()
        conn.close()
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
