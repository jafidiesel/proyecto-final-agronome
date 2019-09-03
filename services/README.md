# AgronoMe
## back-end
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

- [Configuracion](#configuracion)
	- [Crear Nomenclador](#crear-nomenclador)
    - [Consultar Nomenclador](#get-nomenclador)
    - [Consultar Nomencladores tipoRecurso](#get-nomencladores-tipoRecurso)
    - [Consultar Nomencladores tipoCultivo](#get-nomencladores-tipoCultivo)
    - [Consultar Nomencladores tipoPlanificacion](#get-nomencladores-tipoPlanificacion)
    - [Consultar Nomencladores estadoPlanificacion](#get-nomencladores-estadoPlanificacion)
    - [Consultar Nomencladores tipoAnalisis](#get-nomencladores-tipoAnalisis)
    - [Consultar Nomencladores tipoPlan](#get-nomencladores-tipoPlan)
    - [Consultar Nomencladores actividad](#get-nomencladores-actividad)
    - [Consultar Nomencladores rol](#get-nomencladores-rol)
    - [Consultar Nomencladores tipoParametro](#get-nomencladores-tipoParametro)
    - [Consultar Nomencladores opcion](#get-nomencladores-opcion)
    - [Consultar Nomencladores tipoDato](#get-nomencladores-tipoDato)
    - [Consultar Nomencladores recomendacion](#get-nomencladores-recomendacion)
    
- [Reporte](#)
	- [Crear Reporte](#read)
    - [Consultar Reporte](#read)
    - [Consultar Reportes](#read)

- [Recomendacion](#)
	- [Crear Recomendacion](#read)
    - [Consultar Recomendacion](#read)
    - [Consultar Recomendaciones](#read)

# <a name='configuracion'></a> Configuracion

## <a name='crear-nomenclador'></a> Crear Nomenclador
[Back to top](#top)

<p>Crea un nomenclador</p>

	POST /api/configuracion/nomenclador/


### Body
```
{
    "tipoNomenclador": "string",
    "nombre": "string",
    "isActive": boolean
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
       "path" : "{Nombre del modulo}",
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

## <a name='get-nomenclador'></a> Get Nomenclador
[Back to top](#top)

<p>Obtiene un nomenclador</p>

	GET /api/configuracion/nomenclador/:id


### Header param
```
{
    "id": "number"
}
```


### Success Response

Success-Response:

```
HTTP/1.1 200 Ok
{
    "id": "number",
    "tipoNomenclador": "string",
    "nombre": "string",
    "isActive": boolean
}

```


### Error Response

400 Bad Request

```
HTTP/1.1 400 Bad Request
{
   "messages" : [
     {
       "path" : "{Nombre del modulo}",
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
 
## <a name='get-nomencladores-tipoRecurso'></a> Get Nomencladores tipoRecurso
[Back to top](#top)

<p>Obtiene todos los registros de nomencladores tipoRecurso</p>

	GET /api/configuracion/nomenclador/tipoRecurso/


### Header param
```
{
}
```


### Success Response

Success-Response:

```
HTTP/1.1 200 Ok
{
    {
        "id": "number",
        "tipoNomenclador": "tipoRecurso",
        "nombre": "string",
        "isActive": boolean
        
    },
    ...,
    {
        "id": "number",
        "tipoNomenclador": "tipoRecurso",
        "nombre": "string",
        "isActive": boolean
        
    },
}

```

## <a name='get-nomencladores-tipoCultivo'></a> Get Nomencladores tipoCultivo
[Back to top](#top)

<p>Obtiene todos los registros de nomencladores tipoCultivo</p>

	GET /api/configuracion/nomenclador/tipoCultivo/


### Header param
```
{
}
```


### Success Response

Success-Response:

```
HTTP/1.1 200 Ok
{
    {
        "id": "number",
        "tipoNomenclador": "tipoCultivo",
        "nombre": "string",
        "isActive": boolean
        
    },
    ...,
    {
        "id": "number",
        "tipoNomenclador": "tipoCultivo",
        "nombre": "string",
        "isActive": boolean
        
    },
}

```

## <a name='get-nomencladores-tipoPlanificacion'></a> Get Nomencladores tipoPlanificacion
[Back to top](#top)

<p>Obtiene todos los registros de nomencladores tipoPlanificacion</p>

	GET /api/configuracion/nomenclador/tipoPlanificacion/


### Header param
```
{
}
```


### Success Response

Success-Response:

```
HTTP/1.1 200 Ok
{
    {
        "id": "number",
        "tipoNomenclador": "tipoPlanificacion",
        "nombre": "string",
        "isActive": boolean
        
    },
    ...,
    {
        "id": "number",
        "tipoNomenclador": "tipoPlanificacion",
        "nombre": "string",
        "isActive": boolean
        
    },
}

```

## <a name='get-nomencladores-estadoPlanificacion'></a> Get Nomencladores estadoPlanificacion
[Back to top](#top)

<p>Obtiene todos los registros de nomencladores estadoPlanificacion</p>

	GET /api/configuracion/nomenclador/estadoPlanificacion/


### Header param
```
{
}
```


### Success Response

Success-Response:

```
HTTP/1.1 200 Ok
{
    {
        "id": "number",
        "tipoNomenclador": "estadoPlanificacion",
        "nombre": "string",
        "isActive": boolean
        
    },
    ...,
    {
        "id": "number",
        "tipoNomenclador": "estadoPlanificacion",
        "nombre": "string",
        "isActive": boolean
        
    },
}

```

## <a name='get-nomencladores-tipoAnalisis'></a> Get Nomencladores tipoAnalisis
[Back to top](#top)

<p>Obtiene todos los registros de nomencladores tipoAnalisis</p>

	GET /api/configuracion/nomenclador/tipoAnalisis/


### Header param
```
{
}
```


### Success Response

Success-Response:

```
HTTP/1.1 200 Ok
{
    {
        "id": "number",
        "tipoNomenclador": "tipoAnalisis",
        "nombre": "string",
        "isActive": boolean
        
    },
    ...,
    {
        "id": "number",
        "tipoNomenclador": "tipoAnalisis",
        "nombre": "string",
        "isActive": boolean
        
    },
}

```
## <a name='get-nomencladores-tipoPlan'></a> Get Nomencladores tipoPlan
[Back to top](#top)

<p>Obtiene todos los registros de nomencladores tipoPlan</p>

	GET /api/configuracion/nomenclador/tipoPlan/


### Header param
```
{
}
```


### Success Response

Success-Response:

```
HTTP/1.1 200 Ok
{
    {
        "id": "number",
        "tipoNomenclador": "tipoPlan",
        "nombre": "string",
        "isActive": boolean
        
    },
    ...,
    {
        "id": "number",
        "tipoNomenclador": "tipoPlan",
        "nombre": "string",
        "isActive": boolean
        
    },
}

```

## <a name='get-nomencladores-actividad'></a> Get Nomencladores actividad
[Back to top](#top)

<p>Obtiene todos los registros de nomencladores actividad</p>

	GET /api/configuracion/nomenclador/actividad/


### Header param
```
{
}
```


### Success Response

Success-Response:

```
HTTP/1.1 200 Ok
{
    {
        "id": "number",
        "tipoNomenclador": "actividad",
        "nombre": "string",
        "isActive": boolean
        
    },
    ...,
    {
        "id": "number",
        "tipoNomenclador": "actividad",
        "nombre": "string",
        "isActive": boolean
        
    },
}

```

## <a name='get-nomencladores-rol'></a> Get Nomencladores rol
[Back to top](#top)

<p>Obtiene todos los registros de nomencladores rol</p>

	GET /api/configuracion/nomenclador/rol/


### Header param
```
{
}
```


### Success Response

Success-Response:

```
HTTP/1.1 200 Ok
{
    {
        "id": "number",
        "tipoNomenclador": "rol",
        "nombre": "string",
        "isActive": boolean
        
    },
    ...,
    {
        "id": "number",
        "tipoNomenclador": "rol",
        "nombre": "string",
        "isActive": boolean
        
    },
}

```

## <a name='get-nomencladores-tipoParametro'></a> Get Nomencladores tipoParametro
[Back to top](#top)

<p>Obtiene todos los registros de nomencladores tipoParametro</p>

	GET /api/configuracion/nomenclador/tipoParametro/


### Header param
```
{
}
```


### Success Response

Success-Response:

```
HTTP/1.1 200 Ok
{
    {
        "id": "number",
        "tipoNomenclador": "tipoParametro",
        "nombre": "string",
        "isActive": boolean
        
    },
    ...,
    {
        "id": "number",
        "tipoNomenclador": "tipoParametro",
        "nombre": "string",
        "isActive": boolean
        
    },
}

```

## <a name='get-nomencladores-opcion'></a> Get Nomencladores opcion
[Back to top](#top)

<p>Obtiene todos los registros de nomencladores opcion</p>

	GET /api/configuracion/nomenclador/opcion/


### Header param
```
{
}
```


### Success Response

Success-Response:

```
HTTP/1.1 200 Ok
{
    {
        "id": "number",
        "tipoNomenclador": "opcion",
        "nombre": "string",
        "isActive": boolean
        
    },
    ...,
    {
        "id": "number",
        "tipoNomenclador": "opcion",
        "nombre": "string",
        "isActive": boolean
        
    },
}

```

## <a name='get-nomencladores-tipoDato'></a> Get Nomencladores tipoDato
[Back to top](#top)

<p>Obtiene todos los registros de nomencladores tipoDato</p>

	GET /api/configuracion/nomenclador/tipoDato/


### Header param
```
{
}
```


### Success Response

Success-Response:

```
HTTP/1.1 200 Ok
{
    {
        "id": "number",
        "tipoNomenclador": "tipoDato",
        "nombre": "string",
        "isActive": boolean
        
    },
    ...,
    {
        "id": "number",
        "tipoNomenclador": "tipoDato",
        "nombre": "string",
        "isActive": boolean
        
    },
}

```

## <a name='get-nomencladores-recomendacion'></a> Get Nomencladores recomendacion
[Back to top](#top)

<p>Obtiene todos los registros de nomencladores recomendacion</p>

	GET /api/configuracion/nomenclador/recomendacion/


### Header param
```
{
}
```


### Success Response

Success-Response:

```
HTTP/1.1 200 Ok
{
    {
        "id": "number",
        "tipoNomenclador": "recomendacion",
        "nombre": "string",
        "isActive": boolean
        
    },
    ...,
    {
        "id": "number",
        "tipoNomenclador": "recomendacion",
        "nombre": "string",
        "isActive": boolean
        
    },
}

```

