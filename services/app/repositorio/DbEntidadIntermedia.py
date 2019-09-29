from app.extensions import db
from app.repositorio.hlDb import Commit, addObject, saveEntidadSinCommit
#from app.model.hlmodel import 
from app.model import hlmodel

def selectByCodEspec(entidad,codEspecial,cod): 
    if codEspecial=='actividadParametro':
        filtro = entidad.codActividad
    else:
        if codEspecial == 'recomendacionParametro': 
            filtro = entidad.codRecomendacion
        else:
            if codEspecial == 'tipoAnalisisParam':
                filtro = entidad.codTipoAnalisis  
            else:
                if codEspecial == 'tipoAnalisisParam':
                    filtro = entidad.codTipoPlan  
                else:
                     raise Exception('N','No existe el codigo especial ingresado')
        

    objetos = entidad.query.filter(filtro==cod).filter(entidad.isActiv==True).all()
    
    if not objetos:
        obj = entidad.query.filter(filtro==cod).all()
        if obj:
            raise Exception('N','Posee asociaciones pero estan desactivdadas')
        else:  
            raise Exception('N','No existe el codigo ' + codEspecial + ' ingresado')

    return (objetos)


def updateEntidadInterm(data,entidadInterm,entidad,cod):
    dtoActualizadoList=[] #lista de actualizados y creados
    dtoIntermList= [] #lista de todas la entidadIntermedia correspondiente
    modelos = { 
    "actividadParametro":hlmodel.ActividadParametro,
    "recomendacionParametro": hlmodel.RecomendacionParametro,
    "tipoAnalisisParam":hlmodel.TipoAnalisisParam,
    "tipoPlanParam": hlmodel.TipoPlanParam
    }

    if entidad=='actividadParametro':
        filtro = entidadInterm.codActividad
    else:
        if entidad == 'recomendacionParametro': 
            filtro = entidadInterm.codRecomendacion
        else:
            if entidad == 'tipoAnalisisParam':
                filtro = entidadInterm.codTipoAnalisis  
            else:
                if entidad == 'tipoAnalisisParam':
                    filtro = entidadInterm.codTipoPlan  
                else:
                     raise Exception('N','No existe el codigo especial ingresado')

    parametros = data.get('parametros')  

    for param in parametros:
        #isActiv = param.get('isActiv')
        codParam = param.get('codParametro')
        objeto = entidadInterm.query.filter(entidadInterm.codParametro==codParam).filter(filtro==cod).first() 
        if objeto: #si existe, actualizo
            dtoAux=dict(codParam = codParam, codNomen = cod)
            objeto.isActiv = True
            dtoActualizadoList.append(dtoAux)
        else: # si no creo
            dtoAux=dict(codParam = codParam, codNomen = cod)
            objeto = modelos[entidad](True,codParam,cod)
            dtoActualizadoList.append(dtoAux)
            saveEntidadSinCommit(objeto)


    intermediaList = entidadInterm.query.filter(filtro==cod).all() 

    #creo diccionarios de los elementos que existen
    for interm in intermediaList:
        dtoInterm=dict(codParam = interm.codParametro)
        if entidad=='actividadParametro':
            dtoInterm['codNomen'] = interm.codActividad
        else:
            if entidad == 'recomendacionParametro': 
                dtoInterm['codNomen'] = interm.codRecomendacion
            else:
                if entidad == 'tipoAnalisisParam':
                    dtoInterm['codNomen'] = interm.codTipoAnalisis 
                else:
                    if entidad == 'tipoAnalisisParam':
                        dtoInterm['codNomen'] = interm.codTipoPlan
        dtoIntermList.append(dtoInterm)
 

    for item in dtoIntermList:
        if not item in dtoActualizadoList: #si no fue actualizado ni creado, se coloca el false
            objeto = entidadInterm.query.filter(entidadInterm.codParametro==item['codParam']).filter(filtro==item['codNomen']).first() 
            objeto.isActiv =False 


    Commit()
    return ()