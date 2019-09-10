from flask import jsonify
from app.api.helperApi.hlDb import saveEntidad
from app.model.hlmodel import Parametro, Actividad, ActividadParametro
from app.uses_cases.moduloConfiguracion.gestionarNomenclador import getNomencladoCod
import json




def postActivParam(data):
    actividadJson = data.get('actividad')
    parametroJson = data.get ('parametros')

    codActividad = actividadJson.get('id')
    codParametro = parametroJson.get('id')


    actividadParametro = ActividadParametro(True,codParametro,codActividad)
    saveEntidad(actividadParametro)

    #implementacion de muchos parametros
    #lista = json.loads(codParametro)

    #for  cod in lista:
    #    print(cod)
    #    actividadParametro = ActividadParametro(True,cod,codActividad)
    #    saveEntidad(actividadParametro)

    return ('ok')