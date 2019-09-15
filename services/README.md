# AgronoMe
## back-end
<a name="top"></a>
# AgronoMe Services

### Levantar entorno
workon // Lista los entornos creados que tenemos
workon "nombre_entorno"

#### Dentro de la carpeta services:

python app.py


#### Para probar que este corriendo ejecutar en el navegador:

http://localhost:9001/api/ 


-------------------------------------------

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
    - [Consultar Nomenclador ID](#get-nomencladorid)
    - [Modficar Nomenclador ID](#put-nomenclador)
    - [Asociar Parametros](#post-asociarParametro)
    - [Consultar Parametros](#get-consultarParametro)
    - [Modificar Parametro Asociado](#put-modificarParametro)

    


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

	POST /api/configuracion/nomenclador


### Body
```
{
    "tipoNomenclador": "string",
    "nombre": "string",
    "isActive": boolean
}
```


### Success Response 
200 Ok
```
{
  "flag": "S"
}
```

### Error Response
400 Bad Request

```
{
  "flag": "N",
  "message": "cause"
}
```

#


## <a name='get-nomenclador'></a> Consultar Nomenclador
[Back to top](#top)

<p>Obtiene todas las instancias de un nomenclador</p>

	GET /api/configuracion/nomenclador/:tipoNomenclador


### Success Response 
200 Ok

```
[
  {
    "id": int,
    "isActiv": boolean,
    "nombre": "string",
    "tipoNomenclador": "tipoNomenclador"
  },
    .
    .
    ....
]
```

### Error Response
400 Bad Request

```
{
  "flag": "N",
  "message": "cause"
}
```
 

 
#


## <a name='get-nomencladorid'></a> Consultar  Nomenclador Id
[Back to top](#top)

<p>Obtiene la intancia de un nomenclador</p>

	GET /api/configuracion/nomenclador/:tipoNomenclador/:id


### Success Response 
200 Ok

```
{
  "id": int,
  "isActiv": boolean,
  "nombre": "string",
  "tipoNomenclador": "tipoNomenclador"
}
```

### Error Response
400 Bad Request

```
{
  "flag": "N",
  "message": "cause"
}
```


#

## <a name='put-nomenclador'></a> Modificar Nomenclador Id
[Back to top](#top)

<p>Modifica la intancia de un nomenclador</p>

	PUT /api/configuracion/nomenclador/:tipoNomenclador/:id

### Body
```
{
    "nombre": "string",
    "isActive": boolean
}
```

### Success Response 
200 Ok
```
{
  "flag": "S"
}
```

### Error Response
400 Bad Request

```
{
  "flag": "N",
  "message": "cause"
}
```

#

## <a name='post-asociarParametro'></a> Asociar Parametros
[Back to top](#top)

<p>Asociar Parametros a actividad o recomendación o tipo analisis o tipo plan</p>

	POST api/configuracion/asociar


### Body
```
{
    "entidadIntermedia": "actividadParametro",
    "id": int, //CODIGO DE ENTIDAD A ASOCIAR
    "parametros": {
        "id": "[int]" //lista de parametros
    }
}
```


### Success Response 
200 Ok
```
{
  "flag": "S"
}
```

### Error Response
400 Bad Request

```
{
  "flag": "N",
  "message": "cause"
}
```

#


## <a name='get-consultarParametro'></a> Consultar Parametros
[Back to top](#top)

<p>Consultar Parametros de una actividad o recomendación o tipo analisis o tipo plan</p>

	GET /api/configuracion/asociar/:entidadIntermedia/:id


### Success Response 
200 Ok

```
{
    "parametros": [
        {
            "codParametro": int,
            "nombreParametro": string,
            "isActiv": boolean
        },
        ......
    ]
}
```

### Error Response
400 Bad Request

```
{
  "flag": "N",
  "message": "cause"
}
```

#


## <a name='put-modificarParametro'></a> Modificar Parametro Asociado
[Back to top](#top)

<p>Activar o desactivar un determinado parametro de una entidad</p>

	PUT /api/configuracion/asociar/:entidadIntermedia/:id

### Body
```
{
  "idParametro": int,
  "isActiv": boolean
}
```

### Success Response 
200 Ok
```
{
  "flag": "S"
}
```

### Error Response
400 Bad Request

```
{
  "flag": "N",
  "message": "cause"
}
```


