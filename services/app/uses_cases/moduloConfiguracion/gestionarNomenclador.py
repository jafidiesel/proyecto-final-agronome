from app.model import hlmodel
from app.api.helperApi.hlDb import saveEntidad, selectAll, selectByCod, updateEntidad, selectByCod2
from app.api.helperApi.hlResponse import ResponseException
modelos = {
"actividad":hlmodel.Actividad,
"estadoPlanificacion":hlmodel.EstadoPlanificacion,
"opcion":hlmodel.Opcion,
"permiso": hlmodel.Permiso,
"recomendacion": hlmodel.Recomendacion,
"recurso": hlmodel.Recurso,
"rol": hlmodel.Rol,
"tipoAnalisis": hlmodel.TipoAnalisis,
"tipoCultivo": hlmodel.TipoCultivo,
"tipoDato": hlmodel.TipoDato,
"tipoParametro": hlmodel.TipoParametro,
"tipoPlan": hlmodel.TipoPlan,
"tipoPlanificacion": hlmodel.TipoPlanificacion,
"tipoRecurso": hlmodel.TipoRecurso
}

def getNomenclador(data):
    try:
        entidad = data.get('tipoNomenclador')
        objetos = selectAll(modelos[entidad])
        return objetos 
    except Exception as e:
        return ResponseException(e)

def postNomenclador(data):
    try:
        entidad = data.get('tipoNomenclador')
        objeto = modelos[entidad].from_json(data)
        result =saveEntidad(objeto)
        return result
    except Exception as e:
        return ResponseException(e)


def getNomencladoCod(data,id):
    try:
        entidad = data.get('tipoNomenclador')
        objeto = selectByCod(modelos[entidad],id)
        return objeto 
    except Exception as e:
        return ResponseException(e)

def putNomenclador(data,id):
    try:
        entidad = data.get('tipoNomenclador')
        objeto = updateEntidad(modelos[entidad],id,data)
        return objeto 
    except Exception as e:
        return ResponseException(e)

def getNomencladoCod2(data,id):
    try:
        print(data)
        entidad = data.get('tipoNomenclador')
        objeto = selectByCod2(modelos[entidad],id)
        return objeto 
    except Exception as e:
        return ResponseException(e)