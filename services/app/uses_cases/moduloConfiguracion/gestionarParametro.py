from app.api.helperApi.hlDb import saveEntidad, selectAll, selectByCod, updateEntidad
from app.model.hlmodel import Parametro, ParametroOpcion, TipoParametro, TipoDato, Opcion
import json

def postParametro(data): 
    try:
        #dataDic = json.load(data)
        #Manejo de Json
        parametroJson = data.get('parametro')
        tipoParametroJson = data.get('tipoParametro')
        tipoDatoJson = data.get('tipoDato')
        opcionJson = data.get('opcion')
        #parametroOpcionJson = data.get('parametroOpcion')

        #Buscar instancias a asociar
        tipoParametro = selectByCod(TipoParametro,tipoParametroJson.get('id'))
        tipoDato = selectByCod(TipoDato,tipoDatoJson.get('id'))
        op = selectByCod(Opcion,opcionJson.get('id'))

        #Creacion Parametro y ParametroOpcion
        #Como se setean las FK?
        param = Parametro.from_json(parametroJson)
        parametroOpcion = ParametroOpcion(True)
        parametroOpcion.opcion.append(op)
        parametroOpcion.parametro.append(param)
        #Seteo de ParametroOpcion 
        

        result =saveEntidad(parametroOpcion)
        return result 
    except:
        return ("mala sintaxis")
    #Asociar Parametro a TipoParametro
    #Asociar Parametro a TipoDato
    #Buscar opciones agregadas
        #Crear ParametroOpcion
        #Asociar ParametroOpcion a Opcion y Parametro
    