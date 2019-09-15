from app.extensions import db
from app.repositorio.hlDb import Commit

def selectByCodEspec(entidad,codEspecial,cod,isFilterParametro,codParametro): 
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
        
    if isFilterParametro:
        objetos = entidad.query.filter(entidad.codParametro==codParametro).filter(filtro==cod).first()
    else:
        objetos = entidad.query.filter(filtro==cod).all()
    
    if not objetos:
        if isFilterParametro:
            raise Exception('N','No existe el codigo ' + codEspecial + ' ingresado, o el codParametro ingresado')
        else:    
            raise Exception('N','No existe el codigo ' + codEspecial + ' ingresado')

    return (objetos)


def updateEntidadInterm(isActiv,entidad,codEspecial,cod,isFilterParametro,codParametro):
    objeto = selectByCodEspec(entidad,codEspecial,cod,isFilterParametro,codParametro)
    objeto.isActiv = isActiv
    Commit()
    return (objeto)