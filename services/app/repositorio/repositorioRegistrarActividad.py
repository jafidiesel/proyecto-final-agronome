from app.extensions import db
from app.model.hlmodel import ActividadDetalle

def selectActivDetalle(): 
    objetos = ActividadDetalle.query.filter(ActividadDetalle.isEliminado==False)
    return  objetos 