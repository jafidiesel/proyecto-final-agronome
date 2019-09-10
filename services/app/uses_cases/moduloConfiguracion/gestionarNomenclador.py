from flask import jsonify
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


def getNomenclador(entidad):
    try:
        objetos = selectAll(modelos[entidad])
        return jsonify([obj.to_json() for obj in objetos])
    except Exception as e:
        return ResponseException(e)

def postNomenclador(data):
    try:
        entidad = data.get('tipoNomenclador')
        objeto = modelos[entidad].from_json(data)
        result =saveEntidad(objeto)
        return jsonify(result.to_json()) 
    except Exception as e:
        return ResponseException(e)


def getNomencladoCod(entidad,id):
    try:
        objeto = selectByCod(modelos[entidad],id)
        #return jsonify(objeto.to_json())
        return objeto 
    except Exception as e:
        return ResponseException(e)

def putNomenclador(data,entidad,id):
    try:
        objeto = updateEntidad(modelos[entidad],id,data)
        return jsonify(objeto.to_json()) 
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