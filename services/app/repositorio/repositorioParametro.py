from app.extensions import db
from app.repositorio.hlDb import Commit, saveEntidadSinCommit, Rollback
from app.model.hlmodel import ParametroOpcion, Parametro, Opcion
from app.uses_cases.moduloConfiguracion.gestionarNomenclador import getNomencladoCod
from app.api.helperApi.hlResponse import ResponseException, ResponseOk

def selectAllByParamCod(codParam):
    objectList = ParametroOpcion.query.filter(ParametroOpcion.codParametro == codParam).all()
    return objectList

def selectActiveByName(entidad,valor):
    obj = entidad.query.filter(entidad.nombre == valor).filter(entidad.isActiv == True).first()
    return obj

def selectByValue(entidad, valor):
    objList = entidad.query.filter(entidad.codTipoParametro == valor).filter(entidad.isActiv == True).all()
    return objList

def selectAllActiveByParamCod(valor):
    objectList = ParametroOpcion.query.filter(ParametroOpcion.codParametro == valor).filter(ParametroOpcion.isActiv == True).all()
    return objectList

def updateParam(parametroJson,tipoParametroRst, tipoDatoRst,opcionJsonList):    
    try:
        #Se busca Parametro por id, en caso de existir se actualiza
        parametroRst = Parametro.query.filter(Parametro.cod == parametroJson.get('id')).first()
        parametro = Parametro.from_json(parametroJson)
        codOpcionList=[]
            
        #Actualizacion datos propios de Parametro        
        parametroRst.nombre = parametro.nombre
        parametroRst.isActiv = parametro.isActiv
                
        # Actualizacion de asociaciones
        tipoParametroRst.parametroTipo.append(parametroRst)
        tipoDatoRst.parametroDato.append(parametroRst)

        paramOpList = ParametroOpcion.query.filter(ParametroOpcion.codParametro==parametroRst.cod).all()
        #Busqueda por ID de entidades Opcion relacionadas a parametroOpcion
        for parametroOp in paramOpList:
            opcion= Opcion.query.filter(Opcion.cod == parametroOp.codOpcion).one()
            opcionTmp = opcion.to_json()
            opcionTmp.pop('tipoNomenclador', None)
            opcionTmp.pop('nombre', None)
            
            if (opcionTmp not in opcionJsonList):
                #Si ParametroOpcion tiene asociado un codOpcion que NO esta en opcionJsonList, actualizar iSActiv a False
                parametroOp.isActiv = False
            elif (opcionTmp in opcionJsonList):
                parametroOp.isActiv = True
    

        for opcionJson in opcionJsonList:
            i = 0
            for parametroOp in paramOpList:
                if(opcionJson.get('id') == parametroOp.codOpcion):      
                    i += 1
                    
            if(i ==0 ):
                opcion = Opcion.query.filter(Opcion.cod == opcionJson.get('id'))
                saveEntidadSinCommit(ParametroOpcion(True,parametroRst.cod, opcion.cod))       

        Commit()      
        return ResponseOk()   
    except Exception as e:
        Rollback()
        return ResponseException(e)
