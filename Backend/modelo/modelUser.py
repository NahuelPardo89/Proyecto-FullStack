#CLASES
from Backend.modelo.clases.users import User,Cliente,Empleado



class ModelUser:
   
    
    def addUser(conn, user):
        try:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO `users` (`idUser`, `Nombre`, `apellido`, `Telefono`, `direccion`, `contraseña`) VALUES (%s,%s,%s,%s,%s,%s)", (
            user.getId(), user.getNombre(), user.getApellido(), user.getTel(),user.getDireccion(),user.getContraseña()))
            conn.commit()
            print(user.getNombre()," agregado"  )
        except Exception as ex:
            raise Exception(ex)

    def updateUser(conn, user):
        try:
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
        except Exception as ex:
            raise Exception(ex)

    def deleteUser(conn, user):
        try:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM users WHERE idUser=%s",
                        (user.getId(),))
            conn.commit()
        except Exception as ex:
            raise Exception(ex)

    def selectOneUser(conn, id):
        user=None
        try:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT * FROM users WHERE idUser=%s", (id,))
            fila = cursor.fetchone()
            user=User(fila[0],fila[1],fila[2],fila[3],fila[4],fila[5])
        
            return user
        except Exception as ex:
            raise Exception(ex)
            
            
    def selectAllUsers(conn):
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users")
            data = cursor.fetchall()
            
            return data
        except Exception as ex:
            raise Exception(ex)

    

    ######################### CLIENTES###############################


    def addCliente(conn, cliente):
        
        try:
            cursor = conn.cursor()
            #Cargo user para poder cargar cliente, idUser es fk de cliente
            cursor.execute("INSERT INTO `users` (`idUser`, `Nombre`, `apellido`, `Telefono`, `direccion`, `contraseña`) VALUES (%s,%s,%s,%s,%s,%s)", (
            cliente.getId(), cliente.getNombre(), cliente.getApellido(), cliente.getTel(),cliente.getDireccion(),cliente.getContraseña()))
            #cargo cliente
            cursor.execute("INSERT INTO `clientes` (`idCliente`, `idUser`, `socio`) VALUES (%s,%s,%s)", (
                cliente.getIdCliente(), cliente.getId(), cliente.getSocio()))
            conn.commit()
            print (cliente.getNombre()+" agregado")
        except Exception as ex:
            raise Exception(ex)

    def updateCliente(conn, cliente):
        try:
            cursor = conn.cursor()
            cursor.execute("""
                    UPDATE clientes
                    SET  socio=%s
                    WHERE idCliente=%s
                """, (cliente.getSocio(), cliente.getIdCliente()))
            conn.commit()
        except Exception as ex:
            raise Exception(ex)

    def deleteCliente(conn, cliente):
        try:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM clientes WHERE idCliente=%s",
                        (cliente.getIdCliente(),))
            conn.commit()
        except Exception as ex:
            raise Exception(ex)

    def selectOneCliente(conn, id):
        
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM clientes WHERE idCliente=%s",(id,))
            clienteData = cursor.fetchall()
            print (clienteData)
            #cliente=Cliente(clienteData[0],clienteData[1],clienteData[2],clienteData[3],clienteData[4],clienteData[5],clienteData[6],clienteData[7])
            return clienteData
        except Exception as ex:
            raise Exception(ex)

    def selectAllCliente(conn):
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM clientes")
            data = cursor.fetchall()
            
            return data
        except Exception as ex:
            raise Exception(ex)
    
    
    ######################### EMPLEADOS###############################

    def addEmpleado(conn, empleado):
        try:
            cursor = conn.cursor()

            cursor.execute("INSERT INTO `users` (`idUser`, `Nombre`, `apellido`, `Telefono`, `direccion`, `contraseña`) VALUES (%s,%s,%s,%s,%s,%s)", (
            empleado.getId(), empleado.getNombre(), empleado.getApellido(), empleado.getTel(),empleado.getDireccion(),empleado.getContraseña()))

            cursor.execute("INSERT INTO `empleados` (`idUser`, `idInstalacion`, `Horario`) VALUES (%s,%s,%s)", (
            empleado.getId(),empleado.getIdInstalacion(), empleado.getHorario()))

            conn.commit()
        except Exception as ex:
            raise Exception(ex)

    def updateEmpleado(conn, empleado):
        try:
            cursor = conn.cursor()
            cursor.execute("""
                    UPDATE empleados
                    SET  idDepartamento=%s,
                        idInstalacion=%s,
                        Horario=%s
                    WHERE idEmpleado=%s
                """, (empleado.getIdDepartamento(), empleado.getIdInstalacion(), empleado.getHorario(),empleado.getIdEmpleado()))
            conn.commit()
        except Exception as ex:
            raise Exception(ex)

    def deleteEmpleado(conn, empleado):
        try:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM empleados WHERE idEmpleado=%s",
                        (empleado.getIdEmpleado(),))
            conn.commit()
        except Exception as ex:
            raise Exception(ex)

    def selectOneEmpleado(conn, empleado):
        
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM empleados WHERE idEmpleado=%s",
                        (empleado.getIdEmpleado(),))

            empleadoData = cursor.fetchone()
            cursor.execute("SELECT * FROM users WHERE idUser=%s",
                        (empleadoData[1],))
            userData= cursor.fetchone()
            empleado=Empleado(userData[0],userData[1],userData[2],userData[3],userData[4],userData[5],empleadoData[0],empleadoData[2],empleadoData[3])
            
            return empleado
        except Exception as ex:
            raise Exception(ex)

    def selectAllEmpleado(conn):
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM empleados")
            data = cursor.fetchall()
            
            return data
        except Exception as ex:
            raise Exception(ex)
    


    
    def login(self, conn, usuario,contraseña):
        try:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT * FROM users WHERE idUser=%s", (usuario,))
            row = cursor.fetchone()
            if row != None:
                if contraseña == row[5]:
                    user = User(row[0], row[1], row[2],
                                   row[3], row[4], True)
                    return user
            else:
                return None
        except Exception as ex:
            raise Exception(ex)