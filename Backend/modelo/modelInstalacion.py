from Backend.modelo.clases.instalaciones import Instalacion


class ModelInstalacion:
    @classmethod 
    def addInstalacion(self,conn, instalacion):
            try:
                cursor=conn.cursor()
                cursor.execute("INSERT INTO `instalaciones` ( `idInstalacion`, `nombre`, `precio`)  VALUES (%s,%s,%s)",(
                instalacion.getidInstalacion(),instalacion.getnombre(),instalacion.getprecio()))
                conn.commit()
            except Exception as ex:
                raise Exception(ex)

    def updateInstalacion(self,conn,instalacion):
        try:
            cursor=conn.cursor()
            cursor.execute("""
                    UPDATE instalaciones
                    SET idInstalacion=%s,
                        nombre=%s,
                        precio=%s,
                        
                WHERE idInstalacion=%s
                """,(instalacion.getIdInstalacion(),instalacion.getnombre(),instalacion.getPrecio()))
            conn.commit()
        except Exception as ex:
            raise Exception(ex)
    def deleteInstalacion(self,conn,instalacion):
        try:
            cursor=conn.cursor()
            cursor.execute("DELETE FROM instalaciones WHERE idInstalacion=%s",(instalacion.getId()))
            conn.commit()
        except Exception as ex:
            raise Exception(ex)
    def selectOneIntalacion(self,conn,instalacion):
        try:
            cursor=conn.cursor()
            cursor.execute("SELECT * FROM instalaciones WHERE idInstalacion=%s",(instalacion.getId()))
            filainstalacion=cursor.fetchone()
        
            return filainstalacion
        except Exception as ex:
            raise Exception(ex)

    def selectAllInstalacion(conn):
        try:
            cursor=conn.cursor()
            cursor.execute("SELECT * FROM instalaciones")
            dataInstalacion = cursor.fetchall()
            
            return dataInstalacion
        except Exception as ex:
            raise Exception(ex)