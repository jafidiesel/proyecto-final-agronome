# AgronoMe - back end
_El backend de agronome esta desarrollado en python con Flask, para renspoder peticiones hhtps_
 
# AgronoMe Services

## Instalación 🔧 

 _🔧 Instalar [Python 3.7.4](https://www.python.org/downloads/)_ 
 * check instalación: python --version


_🔧 Instalar [Postgres 9.6](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads)_

_🔧 Instalar [PGAdmin 3](https://www.pgadmin.org/download/pgadmin-3-windows/) o [PGAdmin 4](https://www.pgadmin.org/download/pgadmin-4-windows/)_

_🔧 Instalar las siguientes librerias desde la consola para poder trabajar con ambientes:_
```
pip install virtualenv
```
```
pip install virtualenvwrapper-win
```

## Configuración 🛠️

_🛠️ Crear un ambiente virtual y acceder al mismo para poder dentro de este instalar los paquetes asociados a nuestro proyecto_ 
```
mkvirtualenv agronomedev
```
_🛠️ Listar todos los ambientes virtuales_ 

```
workon
```

_🛠️ Entrar al ambiente creado (agronomedev)_ 

```
workon agronomedev 
```

_🛠️ Instalar todas las librerias en el ambiente (agronomedev), para esto vamos a la carpeta raiz del proyecto (services) y instalamos lo que esta en requirements.txt_ 

```
\agronome\services pip install -r requirements.txt 
```

## Inicialización de la base de datos  🔩

_🔩 Crear desde PGAdmin una base de datos con el nombre agronome_

_🔩 En caso que el proyecto contenga una migración se debe borrar la carpeta migrations, buscar en agronome\services\migrations_

_🔩 Inicializar la base de dato desde consola, en la carpeta agronome\services>_

```
 app.py db init    // crea el repositorio migrations
```

```
 app.py db migrate  //detecta las tablas a crear
```

```
 app.py db upgrade //actualiza la tabla
```

## Run services  🚀

_🚀 Run a la aplicación dentro de  agronome\services>_

```
 python app.py 
```


* Para probar que este corriendo ejecutar en el navegador: http://localhost:9001

## Impactar cambios en la base de datos  📌

_📌 Para poder verificar los cambios en el modelo de la aplicación se escribir el comando db migrate, este proceso genera un archivo dentro de la carpeta migrations del proyecto, que posee todas las sentias para actualizar las tablas_
```
 app.py db migrate 
```

_📌 Para impactar todos los cambios se debe realizar un upgrade_
```
 app.py db upgrade 
```

#


## API REST endopints 📄

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
    - [Consultar Nomenclador Filter](#post-nomencladorFilter)
    - [Consultar Nomenclador ID](#get-nomencladorid)
    - [Modoficar Nomenclador ID](#put-nomenclador)
    - [Asociar Parametros](#post-asociarParametro)
    - [Consultar Asociaciones](#get-consultarAsociaciones)
    - [Consultar Parametros Asociados](#get-consultarParametroAsociados)
    - [Modificar Parametros Asociados](#put-modificarParametro)

    


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
## <a name='post-nomencladorFilter'></a> Consultar Nomenclador Filter (isActiv)
[Back to top](#top)

<p>Obtiene la intancia de un nomenclador segun el filtro isActiv</p>

	POST /api/configuracion/nomenclador/:tipoNomenclador
### Body
```
{
  "filtros":
    {
    "isActiv":boolean
    }  
}

```
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


## <a name='get-consultarAsociaciones'></a> Consultar Asociaciones
[Back to top](#top)

<p>Consultar actividades, recomendaciones, tipo plan y tipo paramatro que tienen asociaciones</p>

	GET /api/configuracion/asociar/:entidadIntermedia


### Success Response 
200 Ok

```
{
    "asociaciones": [
        {
            "cod": int,
            "nombre": "String"
        },
        {
            "cod": int,
            "nombre": "String"
        }
    ],

    "sinAsociaciones": [
        {
            "cod": int,
            "nombre": "String"
        }
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


## <a name='get-consultarParametroAsociados'></a> Consultar Parametros asociados
[Back to top](#top)

<p>Consultar Parametros de actividad, recomendación, tipo analisis o tipo plan que estan activos</p>

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


## <a name='put-modificarParametro'></a> Modificar Parametros Asociados
[Back to top](#top)

<p>Activar o desactivar un determinado parametro de una entidad, los parametros que no son enviados se desactivan</p>

	PUT /api/configuracion/asociar/:entidadIntermedia/:id

### Body
```
{
    "parametros": [
        {
            "codParametro": int
        },
        {
            "codParametro": int,
        }
      ]
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


