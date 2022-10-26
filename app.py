from flask import Flask, render_template, request, redirect, url_for,flash


from Backend.modelo.clases.persona import Persona
from Backend.modelo.clases.producto import Producto
from Backend.modelo.modelPersona import modelPersona
from flask_mysqldb import MySQL
from datetime import datetime#usado para nombre foto
import os #usado para interactuar con archivos
from flask import send_from_directory #para traer foto del directorio
app=Flask(__name__,template_folder="view")

#mysql connection
app.config["MYSQL_HOST"]= "localhost"
app.config["MYSQL_USER"]= "root"
app.config["MYSQL_PASSWORD"]= "copado34414604"
app.config["MYSQL_DB"]= "ampav3"
mysql=MySQL(app)


CARPETA=os.path.join("uploads")#configuracion de carpeta archivos

app.config["CARPETA"]=CARPETA

@app.route('/uploads/<nombrefoto>')
def uploads(nombrefoto):
    return send_from_directory(app.config["CARPETA"],nombrefoto)

#settings

app.secret_key="mysecretkey"

#@app.route("/uploads/<nombrefoto>")
#def upload(nombrefoto):
 #   return send_from_directory(app.config)

@app.route("/")
def index():
    cursor= mysql.connection.cursor()
    cursor.execute("SELECT * FROM productos")
    data = cursor.fetchall()
    return render_template("index.html", productos=data)

@app.route("/login", methods=["GET","POST"])
def login():
    if request.method== "POST":
        #print (request.form["user"])
        #print (request.form["password"])
        user=Persona(request.form["user"],"","","","",request.form["password"])
        logged_user=modelPersona.login(mysql,user)
        if logged_user != None:
            return render_template("servicios.html")
        else:
            flash("usuario no encontrado")    
            return render_template("/login.html")
        
    else:    
        return render_template("/login.html")

@app.route("/registroProducto", methods=["POST"]) #ruta que se encarga de registrar producto
def registroProducto():
    if request.method== "POST":
        _nombre=request.form["nombre"]
        _marca=request.form["marca"]
        _descripcion=request.form["descripcion"]
        _precio=request.form["precio"]
        _stock=request.form["cantidad"]
        _foto=request.files["foto"]
        _proveedor=request.form["proveedor"]
       
        now= datetime.now()
        tiempo= now.strftime("%Y%H%M%S")
       
        if _foto.filename != "":
            nuevoNombreFoto=tiempo+_foto.filename
            _foto.save("uploads/"+nuevoNombreFoto)
       
        producto= Producto(None,_proveedor,_nombre,_marca,_descripcion,_precio,_stock,nuevoNombreFoto)
        
        
        cursor=mysql.connection.cursor()
        cursor.execute("INSERT INTO `productos` ( `idProveedor`, `Nombre`, `marca`, `descripcion`, `precio`, `stock`, `foto`)  VALUES (%s,%s,%s,%s,%s,%s,%s)",(
        producto.getIdProveedor(),producto.getNombre(),producto.getMarca(),producto.getDescripcion(),producto.getPrecio(), producto.getStock(),producto.getFoto()))
        mysql.connection.commit()
        flash("producto agregado") #muestra mensaje despues del commit

        return redirect(url_for("index")) #redireciona a index


@app.route("/edit-product/<int:id>")
def editProduct(id):
    cursor= mysql.connection.cursor()
    cursor.execute("SELECT * FROM productos WHERE idProd={0}".format(id))
    data = cursor.fetchall()

     
    return render_template("edit-product.html", productos=data)

@app.route("/update/<id>",methods=["POST"])
def upadateProd(id):
    if request.method== "POST":
        
        _nombre=request.form["nombre"]
        _marca=request.form["marca"]
        _descripcion=request.form["descripcion"]
        _precio=request.form["precio"]
        _cantidad=request.form["cantidad"]
        _foto=request.files["foto"]
        _proveedor=request.form["proveedor"]
        cursor=mysql.connection.cursor()

        now= datetime.now()
        tiempo= now.strftime("%Y%H%M%S")
        if _foto.filename != "":
            nuevoNombreFoto=tiempo+_foto.filename
            _foto.save("uploads/"+nuevoNombreFoto)
            
            cursor.execute("SELECT foto FROM productos WHERE idProd={0}".format(id))
            fila=cursor.fetchall()

            os.remove(os.path.join(app.config["CARPETA"],fila[0][0]))
            cursor.execute("UPDATE productos SET foto=%s WHERE idProd=%s",(nuevoNombreFoto,id))
            mysql.connection.commit()

        cursor.execute("""
            UPDATE productos
            SET nombre=%s,
                marca=%s,
                descripcion=%s,
                precio=%s,
                cantidad=%s,
                `Proveedores_id del producto`=%s
           WHERE idProd=%s
        """,(_nombre,_marca,_descripcion,_precio,_cantidad,_proveedor,id))
        mysql.connection.commit()
        flash("usuario actualizado")
        return redirect(url_for("/admin"))
           


@app.route("/deleteProducto/<id>")
def delete_product(id):
    cursor=mysql.connection.cursor()
    cursor.execute("SELECT foto FROM productos WHERE idProd={0}".format(id))
    fila=cursor.fetchall()
    os.remove(os.path.join(app.config["CARPETA"],fila[0][0]))
    
    cursor.execute("DELETE FROM productos WHERE idProd={0}".format(id))
    mysql.connection.commit()
    flash("usuario eliminado")
    return redirect(url_for("/admin"))

    

@app.route("/admin")
def adminPanel():
    cursor= mysql.connection.cursor()
    cursor.execute("SELECT * FROM productos")
    data = cursor.fetchall()
    return render_template("admin.html", productos=data)
@app.route("/contacto")
def enviarConsulta():
    return "enviando consulta"

if __name__=="__main__":
    app.run(port=3000, debug=True)