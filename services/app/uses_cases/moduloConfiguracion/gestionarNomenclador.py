from flask import jsonify
from app.model import hlmodel
from app.repositorio.hlDb import saveEntidad, selectAll, selectByCod, updateEntidad, selectByCod2
from app.api.helperApi.hlResponse import ResponseException, ResponseOk

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
"tipoRecurso": hlmodel.TipoRecurso,
"parametro": hlmodel.Parametro #agregue esto para usarlo en gestionar entidad intermedia, darle una vuelta de rosca mas con la chechi, basicamente el parametro no es un nomenclador comun, pero lo necesito aca para reutilizar la funcion getNomencladorCod
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
        saveEntidad(objeto)
        return ResponseOk()
    except Exception as e:
        return ResponseException(e)


def getNomencladoCod(entidad,id):
        objeto = selectByCod(modelos[entidad],id)
        if not objeto:
            raise Exception('N','No existe el codigo ingresado') #lanzo la exepcion de nuevo porque algunos casos de usos las necesitan y no llega por la cantidad de llamadas
        return objeto


def putNomenclador(data,entidad,id):
    try:
        updateEntidad(modelos[entidad],id,data)
        return ResponseOk()
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