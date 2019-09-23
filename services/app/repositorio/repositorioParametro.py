from app.extensions import db
from app.repositorio.hlDb import Commit, saveEntidadSinCommit, Rollback
from app.model.hlmodel import ParametroOpcion, Parametro, Opcion
from app.uses_cases.moduloConfiguracion.gestionarNomenclador import getNomencladoCod
from app.api.helperApi.hlResponse import ResponseException, ResponseOk

def selectAllByParamCod(codParam):
    objectList = ParametroOpcion.query.filter(ParametroOpcion.codParametro == codParam).filter(ParametroOpcion.isActiv==True ).all()
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
        for opcionJson in opcionJsonList:
            #Limpiar Json, solo queda el Id
            claves = list(opcionJson.keys())
            for clave in claves:
                if clave!="id":
                    print("Json inicio")
                    print(opcionJson)
                    opcionJson.pop(clave,None)
                    print("Json final")
                    print(opcionJson)

        print(opcionJsonList)

        #Se busca Parametro por id, en caso de existir se actualiza
        parametroRst = Parametro.query.filter(Parametro.cod == parametroJson.get('id')).first()
        parametro = Parametro.from_json(parametroJson)
            
        #Actualizacion datos propios de Parametro        
        parametroRst.nombre = parametro.nombre
        parametroRst.isActiv = parametro.isActiv
                
        # Actualizacion de asociaciones
        tipoParametroRst.parametroTipo.append(parametroRst)
        tipoDatoRst.parametroDato.append(parametroRst)

        paramOpList = ParametroOpcion.query.filter(ParametroOpcion.codParametro==parametroRst.cod).all()
        print("Lista de clases intermedias")
        print(paramOpList)
        #Busqueda por ID de entidades Opcion relacionadas a parametroOpcion
        for parametroOp in paramOpList:
            opcion= Opcion.query.filter(Opcion.cod == parametroOp.codOpcion).one()
            
            opcionTmp = opcion.to_json()
            
            opcionTmp.pop('tipoNomenclador', None)
            opcionTmp.pop('nombre', None)
            opcionTmp.pop('isActiv', None)
            print("OPcion")
            print(opcionTmp)

            if (opcionTmp not in opcionJsonList)or(opcionJsonList[0].get("")):
                print("No incluido")
                #Si ParametroOpcion tiene asociado un codOpcion que NO esta en opcionJsonList, actualizar iSActiv a False
                parametroOp.isActiv = False
            elif (opcionTmp in opcionJsonList):
                print("Incluido")
                parametroOp.isActiv = True
    

        for opcionJson in opcionJsonList:
            print("OpcionJson")
            print(opcionJson)
            i = 0
            for parametroOp in paramOpList:
                print("Parametro Opcion")
                print(parametroOp)
                if(opcionJson.get('id') == parametroOp.codOpcion):      
                    print("VAlor i")
                    print(i)
                    i += 1
            from app.model import hlmodel
            if(i ==0 ):
                print("ParametroOPcion nuevo")
                print(opcionJson.get('id'))

                opcion = Opcion.query.filter(hlmodel.Opcion.cod == opcionJson.get('id')).one()
                saveEntidadSinCommit(ParametroOpcion(True,parametroRst.cod, opcion.cod))       

        #Lista Opcion vacia
        Commit()      
        return ResponseOk()   
    except Exception as e:
        Rollback()
        return ResponseException(e)
