from app.api.helperApi.hlDb import saveEntidad
from app.model.hlmodel import Parametro, ParametroOpcion, TipoParametro, TipoDato, Opcion
import json
from app.uses_cases.moduloConfiguracion.gestionarNomenclador import getNomencladoCod2
from app.extensions import db

def postParametro(data): 
    try:
        #Manejo de Json
        parametroJson = data.get('parametro')
        print(parametroJson)
        tipoParametroJson = data.get('tipoParametro')
        tipoDatoJson = data.get('tipoDato')
        opcionJson = data.get('opcion')

        
        #Buscar instancias a asociar
        tipoParametroRst = getNomencladoCod2(tipoParametroJson, tipoParametroJson.get('id'))
        tipoDatoRst = getNomencladoCod2(tipoDatoJson, tipoDatoJson.get('id'))
        opcionRst = getNomencladoCod2(opcionJson,opcionJson.get('id'))
        #Verificar que las clases esten activas
        
        #Creacion  y persistencia de Parametro 

        parametroRst = Parametro.from_json(parametroJson)     
        tipoDatoRst.parametroRef.append(parametroRst)
        tipoParametroRst.parametroRef.append(parametroRst)
        parametroOpcion = ParametroOpcion(True,parametroRst,opcionRst) 

        rst2 =saveEntidad(parametroRst)

        #Creacion  y persistencia de ParametroOpcion 
        
        print(parametroOpcion.parametro)
        
        #opcionRst.parametroOpcion.append(parametroOpcion)
        #parametroRst.parametroOpcion.append(parametroOpcion)

        saveEntidad(parametroOpcion)
       # rst3 = getNomencladoCod2(rst2,rst2.get('id'))
        print("Despues de append")
        
        return rst2 
    except:
        return ("mala sintaxis")
    #Asociar Parametro a TipoParametro
    #Asociar Parametro a TipoDato
    #Buscar opciones agregadas
        #Crear ParametroOpcion
        #Asociar ParametroOpcion a Opcion y Parametro
    