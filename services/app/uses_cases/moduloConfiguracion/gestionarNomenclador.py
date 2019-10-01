from flask import jsonify
from app.model import hlmodel
from app.repositorio.hlDb import saveEntidad, selectAll, selectByCod, updateEntidad, selectByisActiv
from app.api.helperApi.hlResponse import ResponseException, ResponseOk
from app.shared.toLowerCase import toLowerCaseSingle, obtainDict
import json
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
        dataLower = toLowerCaseSingle(data)
        objeto = modelos[entidad].from_json(dataLower)
        saveEntidad(objeto)
        return ResponseOk()
    except Exception as e:
        return ResponseException(e)


def getNomencladoCod(entidad,cod):
        objeto = selectByCod(modelos[entidad],cod)
        if not objeto:
            raise Exception('N','No existe el codigo ingresado') #lanzo la exepcion de nuevo porque algunos casos de usos las necesitan y no llega por la cantidad de llamadas
        return objeto


def putNomenclador(data,entidad,cod):
    try:
        dataLower = toLowerCaseSingle(data)
        updateEntidad(modelos[entidad],cod,dataLower)
        return ResponseOk()
    except Exception as e:
        return ResponseException(e)

def getNomencladorFilter(data,entidad):
    try:
        filtros= data.get('filtros')
        if not filtros:
            raise Exception('N','No posee filtros, por favor declare los filtros de esta manera: {"filtros:{"isActiv":true}}')
        valor = filtros.get('isActiv')
        
        if valor == None: 
             raise Exception('N','el campo is Activ no posee valor, coloque true o false')
             
        objetos = selectByisActiv(modelos[entidad],valor)
        return  jsonify([obj.to_json() for obj in objetos])
    except Exception as e:
        return ResponseException(e)
    

