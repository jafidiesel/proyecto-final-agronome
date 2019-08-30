from app.model.opcion import Opcion
from app.model.estadoPlanificacion import EstadoPlanificacion
from app.api.helperApi.hlDb import saveEntidad, selectAll, selectByCod, updateEntidad


modelos = {"opcion":Opcion,"estadoPlanificacion":EstadoPlanificacion}

def getNomenclador(data):
    try:
        entidad = data.get('entidad')
        objetos = selectAll(modelos[entidad])
        return objetos 
    except:
        return ("mala sintaxis")


def postNomenclador(data):
    try:
        entidad = data.get('entidad')
        objeto = modelos[entidad].from_json(data)
        result =saveEntidad(objeto)
        return result 
    except:
        return ("mala sintaxis")


def getNomencladoCod(data,id):
    try:
        entidad = data.get('entidad')
        objeto = selectByCod(modelos[entidad],id)
        return objeto 
    except:
        return ("mala sintaxis")

def putNomenclador(data,id):
    try:
        entidad = data.get('entidad')
        objeto = updateEntidad(modelos[entidad],id,data)
        return objeto 
    except:
        return ("mala sintaxis")