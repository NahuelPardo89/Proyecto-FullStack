# Especificación de requisitos de software Proyecto:  A.M.P.A. COMPLEJO DEPORTIVO

## Ficha del documento


| FECHA | REVISIÓN | AUTOR | VERIFICADO DEP. CALIDAD |   
|-------|----------|-------|------------------------|
| 03/10/2022  |    ALPHA 1.0      | DevCord Inspiradores Digitales      |                        |   





# Contenido
## FICHA DEL DOCUMENTO	
CONTENIDO	
1. INTRODUCCIÓN	
    1. Propósito	
    2. Alcance	
    3. Personal involucrado	
    4. Definiciones, acrónimos y abreviaturas	
    5. Referencias	
    6. Resumen
    	
2. DESCRIPCIÓN GENERAL
    1. Perspectiva del producto	
    2. Características de los usuarios	
    3. Restricciones		
   
3. REQUISITOS ESPECÍFICOS	
    1. Product Backlog	
    2. Sprints	
        1. Sprint 0	
        2. Sprint 1
        3. Sprint 2	

## Introducción

Por medio de este documento especificamos los requerimientos que cumplirá el sistema de administración de clientes/afiliados a A.M.P.A  (Asociación Mutual de Programadores Argentinos) para poder hacer uso del Complejo Deportivo y poder disfrutar de todas sus instalaciones.


### Propósito

El presente documento tiene como propósito definir las especificaciones funcionales, no funcionales para el desarrollo de una página web que permitirá gestionar un complejo deportivo.   Éste   será   utilizado  por el personal y los afiliados de A.M.P.A (Asociación Mutual de Programadores Argentinos) 

### Alcance

Esta especificación de requisitos está dirigida a los usuarios de la web "Complejo Deportivo A.M.P.A , para  la administración de las distintas actividades recreativas que ofrece  la   institución   y   para   profundizar   en   la automatización de ésta, la cual tiene por objetivo principal el gestionar los distintos procesos administrativos (Alquileres de las instalaciones deportivas, Eventos, Mapa del sitio, Información, etc).

### Personal involucrado:

| Nombre              | Rol         | Categoría Profesional | Responsabilidad             | Información de contacto       |
|---------------------|-------------|-----------------------|-----------------------------|-------------------------------|
| Maria Eugenia Godoy | Colaborador | Estudiante de TSDWAD  | Desarrollador de página web | mariaeugeniagodoy8@gmail.com  |

| Nombre               | Rol         | Categoría Profesional | Responsabilidad             | Información de contacto         |
|----------------------|-------------|-----------------------|-----------------------------|---------------------------------|
| Sofia Gimena Ledesma | Colaborador | Estudiante de TSDWAD  | Desarrollador de página web | ledesmasofiagimena49@gmail.com  |

| Nombre               | Rol         | Categoría Profesional | Responsabilidad             | Información de contacto    |
|----------------------|-------------|-----------------------|-----------------------------|----------------------------|
| Lautaro Brian Torres | Colaborador | Estudiante de TSDWAD  | Desarrollador de página web | lautioptimus123@gmail.com  |

| Nombre           | Rol         | Categoría Profesional | Responsabilidad             | Información de contacto     |
|------------------|-------------|-----------------------|-----------------------------|-----------------------------|
| Mateo Joel Lopez | Colaborador | Estudiante de TSDWAD  | Desarrollador de página web | thefilesystem1024@gmail.com |

| Nombre                 | Rol           | Categoría Profesional | Responsabilidad             | Información de contacto |
|------------------------|---------------|-----------------------|-----------------------------|-------------------------|
| Nahuel Cruz Pardo Lesa | Scrum Master  | Estudiante de TSDWAD  | Desarrollador de página web | nahue.pardo74@gmail.com |

| Nombre                     | Rol         | Categoría Profesional | Responsabilidad             | Información de contacto |
|----------------------------|-------------|-----------------------|-----------------------------|-------------------------|
|  Catriel Ignacio Pardo Lesa | Colaborador | Estudiante de TSDWAD  | Desarrollador de página web | cartup90@gmail.com      |

| Nombre             | Rol         | Categoría Profesional | Responsabilidad             | Información de contacto  |
|--------------------|-------------|-----------------------|-----------------------------|--------------------------|
| Farias Rita Pamela | Colaborador | Estudiante de TSDWAD  | Desarrollador de página web | ritafarias.mrc@gmail.com |

| Nombre               | Rol         | Categoría Profesional | Responsabilidad             | Información de contacto  |
|----------------------|-------------|-----------------------|-----------------------------|--------------------------|
| Michael David Farias | Colaborador | Estudiante de TSDWAD  | Desarrollador de página web | Makl_2112@hotmail.com.ar |

| Nombre                 | Rol         | Categoría Profesional | Responsabilidad             | Información de contacto   |
|------------------------|-------------|-----------------------|-----------------------------|---------------------------|
| Nadia Soledad Brizuela | Colaborador | Estudiante de TSDWAD  | Desarrollador de página web | solebrizuela.17@gmail.com |

### Definiciones, acrónimos y abreviaturas

|  **Nombre** |                                     Descripción                                     |
|:-----------|:-----------------------------------------------------------------------------------|
| **Usuario** | Persona que usará el sistema                                |
|   **Usuario Administrador**   | Persona que administrará el sistema                               |
|    **RF**   | Requerimiento Funcional                                                             |
|   **RNF**   | Requerimiento No Funcional                                                          |

### Referencias
|   Título del Documento   | Referencia |
|:------------------------:|:----------:|
| Standard IEEE 830 - 1998 | IEEE       |


### Resumen
Este   documento   consta   de   tres   secciones.   En   la   primera   sección   se   realiza   una introducción al mismo y se proporciona una visión general del próposito y alcance del proyecto. También el personal involucrado. En la segunda sección del documento se realiza una descripción general del producto, con el fin de conocer las principales funciones que este debe o no realizar, como así también las caraterísticas de los usuarios. Por   último,   la   tercera   sección   del   documento   es   aquella   en   la   que   se   definen detalladamente los requisitos que debe satisfacer el sistema


## Descripción General:
### Perspectiva del producto
El sitio web A.M.P.A será diseñado para gestionar de una forma eficaz y rápida a los proveedores para el ámbito comercial, y también a clientes, como para alquilar las instalaciones del complejo deportivo, o adquirir algún producto desde la compra y venta de accesorios, sin tener la necesidad de un interacción física, operando desde su computadora y/o celular.
### Características de los usuarios:
| **Tipo de usuario** | Administrador                             |
|---------------------|-------------------------------------------|
| **Formación**       | Manejo de herramientas informáticas       |
| **Actividades**     | 1.Control y manejo del sistema en general |

| **Tipo de usuario** | Registrado                                                                                                                                                                                                                  |
|:---------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Formación**       | Manejo de entornos web                                                                                                                                                                                                      |
| **Actividades**     | 1. Observar servicios y productos del complejo. 2. Reservar el uso de alguna de las instalaciones del complejo. 3. Poder cancelar mis reservas. 4. Poder efectuar compra de accesorios. 5. Poder contactarme con la empresa |

| **Tipo de usuario** | No Registrado                                                                                              |
|---------------------|------------------------------------------------------------------------------------------------------------|
| **Formación**       | Manejo de entornos web                                                                                     |
| **Actividades**     | 1. Observar servicios y productos del complejo. 2. Poder registrarse y ponerse en contacto con la empresa. |

### Restricciones
1. Interfaz para ser usada con internet (solamente o puede ser de escritorio).
2. Lenguajes y tecnologías en uso: HTML, CSS, Bootstrap, JavaScript, Python, MySQL.

## Requisitos específicos
### Product Backlog:
- #US01: Como **cliente** quiero tener una una pagina de inicio en la cual pueda loguear o registrarme
- #US02: Como **cliente** quiero tener una una pagina de registro en la cual el usuario pueda ingresar los siguientes datos: Apellido/s, Nombre/s, Teléfono, Email, DNI y Contraseña
- #US03: Como **cliente** quiero tener una página que hable sobre nuestra empresa para que los usuarios conozcan mas detalles
- #US04: Como **cliente** quiero que el usuario tenga un formulario de contacto para plasmar sus dudas o problematicas y que esta información se envíe a un mail empresarial
- #US05: Como **Cliente** quiero que todos los datos de registro se almacenen en una base de datos para su posterior acceso 
- #US06: Como **Cliente** quiero que mi página de inicio cuente con una seccion de navegación la cual permita acceder de manera sencilla a las otras páginas
- #US07: Como **Cliente** quiero tener acceso de usuario administrador a la pagina para su futuro gestionamiento
- #US08: Como **Cliente** quiero que los usuarios de la página puedan acceder a esta desde cualquier dispositivo manteniéndose el diseño y la legibilidad del sitio.
- #US09: Como **Cliente** deseo tener todos los medios de pagos como débito, crédito, transferencia, mercado pago y otras,  desde la página.
- #US10: Como **Cliente** deseo que cada instalación cuente con estrellas y comentarios para que los usuarios brinden su opinión y poder mejorar los servicios brindados.
- #US11: Como **usuario administrador** quiero poder agregar, eliminar y modificar servicios y productos para mantener la página al día con la empresa.
- #US12: Como **usuario administrador** quiero poder acceder a la base de datos para ver el listado de usuarios registrados
- #US13: Como **usuario administrador** quiero poder ver las instalaciones reservadas y quien las reservo
- #US14: Como **usuario administrador** deseo poder ver si se efectuó el pago de la reserva realizadas por los usuarios registrados
- #US15: Como **usuario no regisrado** quiero ver las instalaciones que posee A.M.P.A  para elegir o para ver si ofrecen el servicio que necesito.
- #US16: Como **usuario no registrado** quiero registrarme en el sitio para poder realizar la reserva de instalaciones
- #US17: Como **usuario registrado** quiero poder reservar una instalación y conocer el costo de dicha reserva.
- #US18: Como **usuario registrado** quiero poder pagar la reserva de las instalaciones o cualquier otro servicio que ofrezcan desde la misma página web para no tener que hacer el pago en el momento de utilizar los servicios.
- #US19: Como **usuario registrado** quiero poder cancelar mis reservas.
- #US20: Como **usuario registrado** debo contar con descuentos si utilizo las instalaciones con frecuencia.
- #US21: Como **usuario registrado** quiero ver las fechas y horarios disponibles de las instalaciones ofrecidas en la web para saber cuando están libres para hacer uso de las mismas


### Sprint Backlog
- TK#01: Crear documento IEEE830
- TK#02: diagramación mapa del sitio
- TK#03: Diseñar página de inicio
- TK#04: Codificar el HTML de la página de inicio
- TK#05: Realizar el diseño CCS de la página de inicio
- TK#06: Crear sección de navegación con los enlaces a : Instalaciones, contacto, acerca de y loguearse/registrarse 
- TK#07: Codificar el HTML de la página instalaciones 
- TK#08: Realizar el diseño CCS de la página Servicios
- TK#09: Diseñar página contacto
- TK#10: Codificar el HTML de la página de contacto
- TK#11: Realizar el diseño CCS de la página de contacto
- TK#12: Diseñar página ACERCA DE
- TK#13: Codificar el HTML de la página ACERCA DE
- TK#14: Realizar el diseño CCS de la página ACERCA DE
- TK#15: Incluir Bootstrap
- TK#16: Diseñar base de datos (Diseño Relacional) 
- TK#17: Codificar base de datos
- TK#18: Codificar HTML formulario de registro 
- TK#19: Codificar css de formulario de registro 
- TK#20: Realizar diseño de la página SERVICIOS
- TK#21: MVC -Modulación y Abstracción
- TK#22: Navegabilidad
- TK#23: Modelado de BB DER, modelo relacional
- TK#24: Script de la BD en MySQL
- TK#25: Links funcionales
- TK#26: Responsive
- TK#27: Formularios con funcionalidad en JavaScript
- TK#28: Modelo de Caso de Uso de cada modularización
- TK#29: Definir clases con sus métodos de Carrito de Productos
- TK#30: Definir clase con sus métodos de Detalle de Carrito de Productos
- TK#31: Definir clase con sus métodos de Instalaciones
- TK#32: Definir clase con sus métodos de Carrito de Reservas
- TK#33: Definir clase con sus métodos de Detalle Carrito de Reservas
- TK#34: Registro de meetings y toda la info necesaria dentro de la Wiki de GitHub
- TK#35: Sitio funcional en hosting remoto de Sitio Institucional en WordPress
- TK#36: Presentación Final de Proyecto


#### Sprint
| **N° de sprint**                         | 00                                                                                                                                                                                                                                                                                                                                                                                                                               |
|------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Sprint Backlog**                       | TK#01: Crear documento IEEE830 TK#02: Diagramación del sitio                                                                                                                                                                                                                                                                                                                                                                     |
| **Responsabilidades**                    | ● Registrar la Especificación de Requerimientos mediante la documentación IEEE830 (subirlo en una carpeta de GitHub en la rama main). ● Git/GitHub : Instalación y registración ● Crear Project estilo Kanban con incorporación de Historias de Usuarios, tareas, e incidencias. ● Idea de mapa del Sitio ● Llevar registro de meetings y toda la info necesaria dentro de la Wiki de GitHub. (Ver consideraciones generales)    |
| **Calendario**                           | Fecha Inicio = 17/09/2022 -  Fecha de Fin = 03/10/2022                                                                                                                                                                                                                                                                                                                                                                           |
| **Inconvenientes:** |  **Sprint Review**: No hubo mayores inconvenientes, salvo dudas lógicas sobre el confeccionamiento del documenteo IEEE830, pero se cumplió con los requisitos del sprint                                                                                                                                                                                                                                                                                                                                                                                                                                |





| N° de sprint                         | 01                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|--------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Sprint Backlog                       | TK#03: Diseñar página de inicio TK#04: Codificar el HTML de la página de inicio TK#05: Realizar el diseño CCS de la página de inicio TK#06: Crear sección de navegación con los enlaces a : Instalaciones, contacto, acerca de y loguearse/registrarse  TK#07: Diseñar página instalaciones TK#08: Codificar el HTML de la página instalaciones TK#09: Realizar el diseño CCS de la página instalaciones TK#10: Crear página contacto TK#11: Codificar el HTML de la página de contacto TK#12: Realizar el diseño CCS de la página de contacto TK#13: Diseñar página acerca de TK#14: Codificar el HTML de la página acerca de TK#15: Realizar el diseño CCS de la página acerca de       |
| Responsabilidades                    | ●    FrontEnd: Estructura HTML, semántica y estilos CSS ●     Navegabilidad - Links funcionales. Responsive ●     BOOTSTRAP y funcionalidad con JavaScript                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Calendario                           | Fecha Inicio = 03/10/2022 -  Fecha de Fin = 17/10/2022                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Inconvenientes:                     	 |   **Sprint Review**: Olvidarnos de designar algunas issues, lo que generó que 2 personas hicieran el mismo trabajo. El formulario de contacto no quedaba como queríamos y luego se logró acomodar. Se nos desacomodó el navbar cuando se implementó Bootstrap.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |


| N° de sprint                         | 02                                                                                                                                                                                                                                                                           |
|--------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Sprint Backlog                       |  TK#16: Diseñar base de datos (Diseño Relacional)  TK#17: Codificar base de datos TK#18: Crear formulario de registro TK#19: Realizar la codificación para validar datos del formulario de registro y crear la lógica necesaria para agregarlos a la base de datos           |
| Responsabilidades                    | ● Sitio funcional en hosting remoto de Sitio Institucional en WordPress y Frontend en subcarpeta (subdominio) y opcional linkeado al repositorio de GitHub/ GitHub Pages.   ●     Backend ○     Script de la BD en MySQL ○     Consultas : Insert - Select - Update - JOIN   |
| Calendario                           | Fecha Inicio = 17/10/2022 -  Fecha de Fin = 14/11/2022                                                                                                                                                                                                                       |
| Inconvenientes:                     	 |                                                                                                                                                                                                                                                                              |

