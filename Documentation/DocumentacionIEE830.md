# Especificación de requisitos de software Proyecto:  A.M.P.A. COMPLEJO DEPORTIVO

## Ficha del documento


| Fecha | Revisión | Autor | Verificado dep. Calidad. |   |
|:-----:|:--------:|:-----:|:------------------------:|---|
| 2022  |          |       |                          |   |


1. Elemento de la lista 1
2. Elemento de la lista 2
3. Elemento de la lista 3


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
| Pardo Lesa Nahuel Cruz | Scrum Master  | Estudiante de TSDWAD  | Desarrollador de página web | nahue.pardo74@gmail.com |

| Nombre                     | Rol         | Categoría Profesional | Responsabilidad             | Información de contacto |
|----------------------------|-------------|-----------------------|-----------------------------|-------------------------|
| Pardo Lesa Catriel Ignacio | Colaborador | Estudiante de TSDWAD  | Desarrollador de página web | cartup90@gmail.com      |

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
| **Usuario** | Persona que usará el sistema para gestionar procesos                                |
|  **SIS-I**  | Sistema de Información Web para la Gestión de Procesos Administrativos y Académicos |
|   **ERS**   | Especificación de Requisitos Software                                               |
|    **RF**   | Requerimiento Funcional                                                             |
|   **RNF**   | Requerimiento No Funcional                                                          |
|   **FTP**   | Protocolo de Transferencia de Archivos                                              |

### Referencias
|   Título del Documento   | Referencia |
|:------------------------:|:----------:|
| Standard IEEE 830 - 1998 | IEEE       |
|                          |            |

### Resumen


## Descripción General:
### Perspectiva del producto
El sitio web A.M.P.A será diseñado para gestionar de una forma eficaz y rápida a los proveedores para el ámbito comercial, y también a clientes, como para alquilar las instalaciones del complejo deportivo, o adquirir algún producto desde la compra y venta de accesorios, sin tener la necesidad de un interacción física, operando desde su computadora y/o celular.
### Características de los usuarios:
| **Tipo de usuario** | Administrador                             |
|---------------------|-------------------------------------------|
| **Formación**       | Manejo de herramientas informáticas       |
| **Actividades**     | 1.Control y manejo del sistema en general |

| **Tipo de usuario** |  Registrado                                                                                                                                                                                                                  |
|---------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Formación**       | Manejo de entornos web                                                                                                                                                                                                       |
| **Actividades**     | 1. Observar servicios y productos del complejo. 2. Reservar el uso de alguna de las instalaciones del complejo. 3. Poder cancelar  mis reservas. 4. Poder efectuar compra de accesorios. 5. Poder contactarme con la empresa |

| **Tipo de usuario** | No Registrado                                                                                              |
|---------------------|------------------------------------------------------------------------------------------------------------|
| **Formación**       | Manejo de entornos web                                                                                     |
| **Actividades**     | 1. Observar servicios y productos del complejo. 2. Poder registrarse y ponerse en contacto con la empresa. |

### Restricciones
1. Interfaz para ser usada con internet (solamente o puede ser de escritorio).
2. Lenguajes y tecnologías en uso: HTML, CSS, Bootstrap, JavaScript, Python, MySQL.

## Requisitos específicos
### Product Backlog:
- #US01: Como administrador quiero poder agregar, eliminar y modificar servicios y productos para mantener la página al día con la empresa.
- #US02: Como administrador quiero que los usuarios de la página puedan acceder a esta desde cualquier dispositivo manteniéndose el diseño y la legibilidad del sitio.
- #US03: Como administrador quiero ver el listado de usuarios registrados
- #US04: Como administrador quiero poder ver las instalaciones reservadas
- #US05: Como usuario quiero ver las instalaciones que posee A.M.P.A  para elegir o para ver si ofrecen el servicio que necesito
- #US06: Como usuario registrado quiero poder reservar una instalación y conocer el costo de dicha reserva.
- #US07: Como usuario no registrado quiero registrarme en el sitio para poder realizar la reserva de instalaciones
- #US08: Como proveedor de servicios y productos quiero poder administrar mi sección de la tienda
- #US09: Como usuario registrado quiero poder pagar la reserva de las instalaciones o cualquier otro servicio que ofrezcan desde la misma página web para no tener que hacer el pago en el momento de utilizar los servicios.
- #US10: Como usuario quiero poder cancelar mis reservas.
- #US11: Como Proveedor deseo tener todos los medios de pagos como débito, crédito, transferencia, mercado pago y otras,  desde la página.
- #US12: Como Proveedor deseo que cada instalación cuente con estrellas y comentarios para que los usuarios brinden su opinión y poder mejorar los servicios brindados.
- #US13: Como Proveedor deseo que cuando el Usuario ingrese aparezca una foto del carnet de socio en la pantalla.
- #US14: Como Usuario debo contar con descuentos si utilizo las instalaciones con frecuencia.
- #US15: Como empleado del complejo deseo poder chequear si el usuario ya hizo el pago cuando ingresa al complejo a utilizar las instalaciones para que este no tenga necesidad de mostrar ningún comprobante 
- #US16: Como usuario registrado quiero ver las fechas y horarios disponibles de las instalaciones ofrecidas en la web para saber cuando están libres para hacer uso de las mismas

### Sprint Backlog
- TK#01: Crear documento IEEE830
- TK#02: diagramación mapa del sitio
- TK#03: Diseñar página de inicio
- TK#04: Codificar el HTML de la página de inicio
- TK#05: Realizar el diseño CCS de la página de inicio
- TK#06: Crear sección de navegación con los enlaces a : Instalaciones, contacto, acerca de y loguearse/registrarse 
- TK#07: Diseñar página instalaciones
- TK#08: Codificar el HTML de la página instalaciones
- TK#09: Realizar el diseño CCS de la página instalaciones
- TK#10: Crear página contacto
- TK#11: Codificar el HTML de la página de contacto
- TK#12: Realizar el diseño CCS de la página de contacto
- TK#13: Diseñar página acerca de
- TK#14: Codificar el HTML de la página acerca de
- TK#15: Realizar el diseño CCS de la página acerca de
- TK#16: Diseñar base de datos (Diseño Relacional) 
- TK#17: Codificar base de datos
- TK#18: Crear formulario de registro
#### Sprint
| **N° de sprint**                         | 00                                                                                                                                                                                                                                                                                                                                                                                                                               |
|------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Sprint Backlog**                       | TK#01: Crear documento IEEE830 TK#02: Diagramación del sitio                                                                                                                                                                                                                                                                                                                                                                     |
| **Responsabilidades**                    | ● Registrar la Especificación de Requerimientos mediante la documentación IEEE830 (subirlo en una carpeta de GitHub en la rama main). ● Git/GitHub : Instalación y registración ● Crear Project estilo Kanban con incorporación de Historias de Usuarios, tareas, e incidencias. ● Idea de mapa del Sitio ● Llevar registro de meetings y toda la info necesaria dentro de la Wiki de GitHub. (Ver consideraciones generales)    |
| **Calendario**                           | Fecha Inicio = 17/09/2022 -  Fecha de Fin = 03/10/2022                                                                                                                                                                                                                                                                                                                                                                           |
| **Inconvenientes:** |                                                                                                                                                                                                                                                                                                                                                                                                                                  |





| N° de sprint                         | 01                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|--------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Sprint Backlog                       | TK#03: Diseñar página de inicio TK#04: Codificar el HTML de la página de inicio TK#05: Realizar el diseño CCS de la página de inicio TK#06: Crear sección de navegación con los enlaces a : Instalaciones, contacto, acerca de y loguearse/registrarse  TK#07: Diseñar página instalaciones TK#08: Codificar el HTML de la página instalaciones TK#09: Realizar el diseño CCS de la página instalaciones TK#10: Crear página contacto TK#11: Codificar el HTML de la página de contacto TK#12: Realizar el diseño CCS de la página de contacto TK#13: Diseñar página acerca de TK#14: Codificar el HTML de la página acerca de TK#15: Realizar el diseño CCS de la página acerca de       |
| Responsabilidades                    | ●    FrontEnd: Estructura HTML, semántica y estilos CSS ●     Navegabilidad - Links funcionales. Responsive ●     BOOTSTRAP y funcionalidad con JavaScript                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Calendario                           | Fecha Inicio = 03/10/2022 -  Fecha de Fin = 17/10/2022                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Inconvenientes:                     	 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |


| N° de sprint                         | 02                                                                                                                                                                                                                                                                           |
|--------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Sprint Backlog                       |  TK#16: Diseñar base de datos (Diseño Relacional)  TK#17: Codificar base de datos TK#18: Crear formulario de registro TK#19: Realizar la codificación para validar datos del formulario de registro y crear la lógica necesaria para agregarlos a la base de datos           |
| Responsabilidades                    | ● Sitio funcional en hosting remoto de Sitio Institucional en WordPress y Frontend en subcarpeta (subdominio) y opcional linkeado al repositorio de GitHub/ GitHub Pages.   ●     Backend ○     Script de la BD en MySQL ○     Consultas : Insert - Select - Update - JOIN   |
| Calendario                           | Fecha Inicio = 17/10/2022 -  Fecha de Fin = 14/11/2022                                                                                                                                                                                                                       |
| Inconvenientes:                     	 |                                                                                                                                                                                                                                                                              |

