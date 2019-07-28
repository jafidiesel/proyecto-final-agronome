<a name="top"></a>
# AgronoMe Services

API REST endopints

- [Actividad](#actividad)
	- [Registrar Actividad](#crear-actividad)
    - [Consultar Actividad](#consultar-actividad)
    - [Modificar Actividad](#crear-actividad)
    - [Eliminar Actividad](#crear-actividad)
    - [Consultar Actividades](#consultar-actividades)

- [Planificacion](#)
	- [Crear Planificacion](#read)
    - [Consultar Planificacion](#read)
    - [Crear Analisis](#read)
    - [Consultar Analisis](#read)
    - [Modificar Analisis](#read)
    - [Eliminar Analisis](#read)
    - [Crear Plan](#read)
    - [Consultar Plan](#read)
    - [Modificar Plan](#read)
    - [Eliminar Plan](#read)
    - [Consultar Planificaciones](#read)
    
- [Finca](#)
	- [Crear Finca](#read)
	- [Modificar Finca](#read)
    - [Consultar Finca](#read)
    - [Consultar Fincas](#read)
    - [Crear Supervisor](#read)
    - [Modificar Supervisor](#read)
    - [Eliminar Supervisor](#read)

- [Recurso](#)
	- [Crear Recurso](#read)
    - [Consultar Recurso](#read)
    - [Modificar Recurso](#read)
    - [Eliminar Recurso](#read)
    - [Consultar Recursos](#read)

- [Seguridad](#)
	- [Crear Usuario](#read)
	- [Modificar Usuario](#read)
	- [Eliminar Usuario](#read)
	- [Crear Rol](#read)
	- [Modificar Rol](#read)
	- [Eliminar Rol](#read)
    - [Consultar Usuarios](#read)
    - [Consultar Roles](#read)
    - [Consultar Usuarios Activos](#read)

- [Sesion](#)
	- [Log In](#read)
	- [Blanquear Contraseña](#read)

- [Configuracion](#)
	- [Crear Parametro](#read)
    - [Consultar Parametro](#read)
    - [Consultar Parametro](#read)

- [Reporte](#)
	- [Generar Reporte](#read)
    - [Consultar Reporte](#read)
    - [Consultar Reportes](#read)

- [Recomendacion](#)
	- [Registrar Recomendacion](#read)
    - [Consultar Recomendacion](#read)
    - [Consultar Actividades a Recomendar](#read)
    - [Consultar Recomendaciones](#read)

# <a name='actividad'></a> Actividad

## <a name='crear-actividad'></a> Crear Actividad
[Back to top](#top)

<p>Crea una actividad</p>

	POST /api/v1/actividad/


### Body
```
{

}
```


### Success Response

Success-Response:

```
HTTP/1.1 200 Ok

```


### Error Response

400 Bad Request

```
HTTP/1.1 400 Bad Request
{
   "messages" : [
     {
       "path" : "{Nombre de la propiedad}",
       "message" : "{Motivo del error}"
     },
     ...
  ]
}
```
500 Server Error

```
HTTP/1.1 500 Internal Server Error
{
   "error" : "Not Found"
}
```
