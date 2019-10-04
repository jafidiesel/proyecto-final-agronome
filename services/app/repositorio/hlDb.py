from flask import jsonify
from app.extensions import db

def saveEntidad(entidad):
    db.session.add(entidad)
    db.session.commit()
    return entidad


def selectAll(entidad):
    objList=entidad.query.order_by(entidad.cod).all()
    return objList

def selectAllisActiv(entidad):
    objList=entidad.query.filter(entidad.isActiv==True).order_by(entidad.cod).all()
    return objList

def selectByCod(entidad,cod): ##si el codigo se llama cod
    obj = entidad.query.filter(entidad.cod==cod).first()
    if not obj:
        #print('no hay objeto')
        raise Exception('N','No existe el codigo ingresado')

    return (obj)

def updateEntidad(entidad,cod,data): ##solo update nomencladores
    obj = entidad.query.filter(entidad.cod==cod).first() 
    if not obj: ## si el objeto no existe lanzo la exception
        raise Exception('N','No existe el codigo ingresado')
    
    obj.nombre = data.get('nombre')
    obj.isActiv = data.get('isActiv')
    db.session.commit()
    return (obj)
    
def selectByisActiv(entidad,valor):
    objetos = entidad.query.filter(entidad.isActiv==valor).all()
    if not objetos:
        raise Exception('N','No existen objetos con isActiv ingresado')
    return objetos


def saveEntidadSinCommit(entidad):
   db.session.add(entidad)
   return entidad

def Commit():
    db.session.commit()
    print('commit de la base de datos')
    return 'commit sucess'

def Rollback():
    print('rollback de la base de datos')
    db.session.rollback()
    return 'rollback sucess'

def addObject(entidad):
    db.session.add(entidad)
    print("In ADD")
    print("Funciones")
    print(dir(entidad))
    return 'add success'

def deleteObject(entidad):
    db.session.delete(entidad)
    return