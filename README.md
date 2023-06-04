
# Proyecto-FullStack 2022
Pagina web sobre complejo deportivo AMPA (ficticio) desarrollada para el Proyecto integrador del módulo programador FullStack. Instituto Superior Politécnico de Córdoba


Github Pages: https://nahuelpardo89.github.io/Proyecto-FullStack/Maqueta2022/Frontend/vista/index.html

Wordpress DevCord: https://devcord.g4merstore.com.ar/

Presentación final Proyecto  : https://www.youtube.com/watch?v=B_L0aNS21BM&ab_channel=cartup90


# Proyecto-FullStack  E-commerce 2023

Para ejecutar el servidor posicionarse en la carpeta FrontEnd/ampa, hacer npm install en la terminal y luego ng serve -o

## Django

Para ejecutarlo deben hacer lo siguiente, primero creen un entorno virtual dentro de la carpeta backend
- Posicionar la consola en la carpeta backend y  escribir lo siguente: virtualenv -p python3 env
- Se les deberia crear una carpeta llamada env si todo esta correcto. 
- Luego  escriben lo siguiente: .\env\Scripts\activate
- Si todo salio bien les deveria figurar env en la consola, por ejemplo     
 (env) PS C:\Users\nanit\Desktop\tsdw2023\proyecto2023\Proyecto-FullStack\BackEnd>
 Eso significa que ya estan dentro del entorno virtual.
 
Ahora posicionan la consola en la carpeta ampaApiRest y ejecutan el siguiente comando :    
pip install -r requirements.txt     
 Se deberia instalarles django y las dependencias
- Luego ejecutan los siguientes comandos:       
 python manage.py makemigrations    
 python manage.py migrate      
 python manage.py createsuperuser     
Ahi les pide los datos para crear un super usuario, lo crean y luego ejecutan el comando:            
python manage.py runserver

Para entrar en el navegador escriben : http://127.0.0.1:8000/       
Para entrar al panel de administracion escriben http://127.0.0.1:8000/admin
