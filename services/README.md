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

_📌 Para poder verificar los cambios en el modelo de la aplicación se escribir el comando db migrate, este proceso genera un archivo dentro de la carpeta migrations del proyecto, que posee todas las sentencias para actualizar las tablas_
```
 app.py db migrate 
```

_📌 Para impactar todos los cambios se debe realizar un upgrade_
```
 app.py db upgrade 
```
 
## Backup de la base de datos ⚙️
_Para poder realizar un backup completo de las tablas y datos se deben realizar los siguientes pasos_

⚙️Abrir el cmd como administrador e ir al path bin donde esta instalado postgres
```
cd C:\Program Files\PostgreSQL\9.6\bin
```
⚙️Correr el comando y completar los literales que se encuentran entre comillas simples:

pg_dump -U 'usuario' -W -h 'host' 'database' > 'backup.sql' 
```
pg_dump -U postgres -W -h localhost agronome > agronomeBackup.sql
```

* Se crear el archivo agronomeBackup.sql en la carpeta C:\Program Files\PostgreSQL\9.6\bin , en donde se visualiza el script sql 

⚙️Para restaurar lanzamos el comando:

psql -U 'usuario' -W -h 'host' 'database' < 'backup.sql'
```
psql -U postgres -W -h localhost agronome < agronomeBackup.sql
```


⚙️Para realizar el backup de solo una TABLA en particular:

pg_dump -U 'usuario' -W -h 'host' 'database' -t 'tablename' > 'backup.sql' 
```
pg_dump -U postgres -W -h localhost -t actividad agronome > actividadbackup.sql
```
## Link de interes para backup con postgres ✒️

✒️ [Postgres - pgdump documentación oficial ](https://www.postgresql.org/docs/9.1/app-pgdump.html)

✒️ [Tutorial para crear un backup](https://platzi.com/tutoriales/1480-postgresql/2252-como-generar-una-backup-de-postgresql-y-como-restaurarla/)

✒️ [Especificaciones del comando pgdump](http://es.tldp.org/Postgresql-es/web/navegable/user/app-pgdump.html)

## Crear un nuevo end point  📄

_📄 Para poder definir un nuevo end point se deben realizar los siguientes pasos:_

- Crear el archivo base del end point con la siguente nomenclatura: [nombre]_api ejemplo: finca_api
- Agregar la url en app.api.helperApi.hlUrl 
- Agregar el namespace en app.api.helperApi.hlNamespaceBackend
- Correr el servidor http://127.0.0.1:9001/ y verificar si reconoce la url definida 

#

## API REST Documents 📖 

- [Actividad](#actividad)
	- [Registrar Actividad](#registrar-actividad)
    - [Consultar Actividades](#consultar-actividad)
    - [Consultar Actividad](#consultar-actividad)
    - [Modificar Actividad](#modificar-actividad)
    - [Eliminar Actividad](#eliminar-actividad)
    - [Consultar Parametros Full de Actividad](#parametroFull-actividad)

- [Finca](#)
	- [Crear Finca](#crear-finca)
    - [Consultar Fincas](#consultar-fincas)
    - [Consultar Finca](#consultar-finca)


- [Planificacion](#)
	- [Crear Planificacion](#read)
    - [Consultar Planificacion](#read)
    - [Consultar Planificaciones](#read)
    


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





# <a name='actividad'></a> Actividad

## <a name='registrar-actividad'></a> Registrar Actividad
[Back to top](#top)

<p>Registrar una actividad</p>

	POST /api/actividad/registrar

### Body
```
{
	"codActividad": int,
	"fchActivDetalle": dateString, // "2019-10-30 22:12:54"
	"observacion": string,
	"imagenes": [
		{
		"dscImg":String,
		"base64": String de img en base 64
		}, ..... 
	],

	"parametros":[
      {
      "codParam":int,
      "valor": "String"
      }, .....	
	]
}
```

#

## <a name='consultar-actividades'></a> Consultar Actividades
[Back to top](#top)

<p>Consultar actividades</p>

	GET /api/actividad/registrar



### Success Response 
200 Ok
```
{
    "codActivDetalle": int,
    "fchActivDetalle": dateString,//   "28-09-2019 16:01:34"
    "observacion": String,
    "Actividad": {
        "codActividad": int,
        "nombreActividad": String
    },
    "Parametros": [
        {
            "codParamtro": int,
            "nombreParametro": String,
            "valor": String
        },....
    ],

    "Imagenes": [
        {
            "dscImg": String,
            "base64": String img base 64
        },...
        
      ]
},

{
    "codActivDetalle": int,
    "fchActivDetalle": dateString,//   "28-09-2019 16:01:34"
    "observacion": String,
    "Actividad": {
        "codActividad": int,
        "nombreActividad": String
    },
    "Parametros": [
        {
            "codParamtro": int,
            "nombreParametro": String,
            "valor": String
        },....
    ],

    "Imagenes": [
        {
            "dscImg": String,
            "base64": String img base 64
        },...
        
      ]
}.....
    
```

#
## <a name='consultar-actividad'></a> Consultar Actividad
[Back to top](#top)

<p>Consultar una actividad en particular</p>

	GET /api/actividad/registrar/:codDetalleActividad


### Success Response 
200 Ok
```
{
    "codActivDetalle": int,
    "fchActivDetalle": dateString,//   "28-09-2019 16:01:34"
    "observacion": String,
    "Actividad": {
        "codActividad": int,
        "nombreActividad": String
    },
    "Parametros": [
        {
            "codParamtro": int,
            "nombreParametro": String,
            "valor": String
        },....
    ],

    "Imagenes": [
        {
            "dscImg": String,
            "base64": String img base 64
        },...
        
```
#
## <a name='modificar-actividad'></a> Modificar Actividad
[Back to top](#top)

<p>Modificar una actividad en particular, hay que tener en cuenta que no se puede eliminar un parametro ni agregar uno nuevo, ya que esta planteado que se modifiquen las instancias que ya estan creadas </p>

	PUT /api/actividad/registrar/:codDetalleActividad

```  
{
    "codActivDetalle": int,
    "fchActivDetalle": dateString,//   "28-09-2019 16:01:34"
    "observacion": String,
    "Actividad": {
        "codActividad": int,
        "nombreActividad": String
    },
    "parametros": [
        {
            "codParam": int,
            "valor": String
        },....
    ],

    "imagenes": [
        {
            "dscImg": String,
            "base64": String img base 64
        },...
        
```
#
## <a name='eliminar-actividad'></a> Eliminar Actividad
[Back to top](#top)

<p>Eliminar una actividad en particular, coloca "isEliminada" en True, es una eliminación logica </p>

	DELETE /api/actividad/registrar/:codDetalleActividad

#

## <a name='parametroFull-actividad'></a> Consultar Parametros Full de Actividad
[Back to top](#top)

<p>Consultar los parametros para poder armar el formulario de una actividad en particular, ojo en los parametros se debe ingresar el codigo de la actividad y no el codigo del detalle </p>

	GET /api/actividad/registrar/parametros/:codActividad

### Success Response 
200 Ok
```
{      //por cada parametro  
    {
    "parametro": {
        "cod": int
        "nombre": String,
        "isActiv": boolean
    },
    "tipoParametro": {
        "cod": int,
        "nombre": String,
        "isActiv": boolean
    },
    "tipoDato": {
        "nombre": String,
        "cod": int,
        "isActiv": boolean
    },
    "opcion": [
        {
            "cod": int,
            "nombre": String,
            "isActiv": boolean
        },
        {
            "cod": int,
            "nombre": String,
            "isActiv": boolean
        }
        ]
    }
 ]
}
```

#


# <a name='finca'></a> Finca

## <a name='crear-finca'></a> Crear Finca
[Back to top](#top)

<p>Crear una finca</p>

	POST /api/finca

### Body
```
{
    "nombre": String,
    "superficie": float,
    "calle": String,
    "nro": int,
    "localidad": String,
    "provincia": String,
    "parcelas": [
        {
            "nombre": String,
            "superficie": float,
            "filas": int,
            "columnas": int
        },
        {
            "nombre": String,
            "superficie": float,
            "filas": int,
            "columnas": int
        }
    ]
}
```
#
## <a name='consultar-fincas'></a> Consultar Fincas
[Back to top](#top)

<p>Cnsultar todas las fincas</p>

	GET /api/finca



### Success Response 
200 Ok
```
{
    "fincas": [
        //por cada finca
        { 
            "codFinca": 2,
            "nombre": "3 Huertas",
            "superficie": 12341.23,
            "isActiv": true,
            "calle": "Doctor Moreno",
            "nro": 1805,
            "localidad": "Las Heras",
            "provincia": "Mendoza",
            "urlMaps": "https://www.google.com.ar/maps/place/Doctor+Moreno+1805+Las+Heras+Mendoza"
        }....
    ]
} 

```
#

## <a name='consulta-finca'></a> Consultar Finca
[Back to top](#top)

<p>Consultar una finca en particular</p>

	GET /api/finca/:codFinca

```
    {
    "finca": {
        "codFinca": int,
        "nombre": String,
        "superficie": float,
        "isActiv": boolean,
        "calle": String,
        "nro": int,
        "localidad": String,
        "provincia": String,
        "urlMaps": Url String,
        "parcelas": [
            //por cada parcela
            {  "codParcela": int,
                "nombre": String,
                "superficie": String, //123.4 m
                "filas": int,
                "columnas": int,
                "cantCuadros": int,
                "cuadros": [
                    //por cada cuadro
                    {
                        "codCuadro": int,
                        "nombreCuadro": String"
                    },..
                ]
            }
        ]

```






#

## <a name='consultar-actividades'></a> Consultar Actividades




#
# <a name='configuracion'></a> Configuracion

## <a name='crear-nomenclador'></a>  Nomenclador
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

<p>Consultar Parametros de una actividad, recomendación, tipo analisis o tipo plan que estan activos</p>

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


