<a name="top"></a>
# AgronoMe Services

API REST endopints

- [Actividad](#actividad)
	- [Crear Actividad](#crear-actividad)
    - [Consultar Actividad](#consultar-actividad)
    - [Consultar Actividades](#consultar-actividades)

- [Planificacion](#)
	- [Crear Planificacion](#read)
    - [Consultar Planificacion](#read)
    - [Consultar Planificaciones](#read)
    
- [Finca](#)
	- [Crear Finca](#read)
    - [Consultar Finca](#read)
    - [Consultar Finca](#read)

- [Recurso](#)
	- [Crear Recurso](#read)
    - [Consultar Recurso](#read)
    - [Consultar Recursos](#read)

- [Seguridad](#)
	- [Crear Recurso](#read)
    - [Consultar Recurso](#read)
    - [Consultar Recursos](#read)

- [Configuracion](#)
	- [Crear Parametro](#read)
    - [Consultar Parametro](#read)
    - [Consultar Parametro](#read)

- [Reporte](#)
	- [Crear Reporte](#read)
    - [Consultar Reporte](#read)
    - [Consultar Reportes](#read)

- [Recomendacion](#)
	- [Crear Recomendacion](#read)
    - [Consultar Recomendacion](#read)
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
