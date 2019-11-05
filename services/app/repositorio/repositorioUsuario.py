from app.extensions import db
from app.repositorio.hlDb import Commit, saveEntidadSinCommit, Rollback
from app.model.hlmodel import Usuario, Rol, FincaUsuario,Finca
from app.uses_cases.moduloConfiguracion.gestionarNomenclador import getNomencladoCod
from app.api.helperApi.hlResponse import ResponseException, ResponseOk
from sqlalchemy.orm import exc


import datetime

def updateUser(usuarioJson, rolRst, codUsuario, listFincaJson):
    try:
        from app.model import hlmodel
        #Se busca el usuario, en caso de existir se actualiza el mismo
        usuarioRst = Usuario.query.filter(Usuario.cod == codUsuario).one()
        #user = Usuario.from_json(usuarioJson)
        #Actualizar datos propios de Usuario
        usuarioRst.nombre = usuarioJson.get('nombre')
        usuarioRst.apellido = usuarioJson.get('apellido')
        usuarioRst.contraseniaUsuario =usuarioJson.get('contraseniaUsuario')
        usuarioRst.email = usuarioJson.get('email')
        usuarioRst.usuario = usuarioJson.get('usuario')
        usuarioRst.isActiv = usuarioJson.get('isActiv')
        #Actualizar Rol
        usuarioRst.rol = rolRst
        #Actualizar Fincas
        #Limpiar Json de Fincas, solo queda el id de Finca
        if listFincaJson:
            for fincaJson in listFincaJson:
                #Limpiar Json, solo queda el Id
                claves = list(fincaJson.keys())
                for clave in claves:
                    if clave!="codFinca":
                        fincaJson.pop(clave,None)
            
        fincaUsuarioListRst = usuarioRst.fincaUsuarioList
        if fincaUsuarioListRst:
            #Por cada FincaUsuario buscar Finca
            for fincaUsuarioRst in fincaUsuarioListRst:
                finca = fincaUsuarioRst.finca
                fincaTmp = dict(codFinca=finca.codFinca)
                if (fincaTmp not in listFincaJson)or(listFincaJson[0].get("")):
                #Si FincaUsuario tiene asociado un codFinca que NO esta en listFincaJson, actualizar iSActiv a False
                # y fchFin con fecha actual
                    fincaUsuarioRst.isActiv = False
                    fincaUsuarioRst.fchFin = datetime.datetime.now
                elif (fincaTmp in listFincaJson)and(fincaUsuarioRst.isActiv==False):
                    fincaRst = Finca.query.filter(hlmodel.Finca.codFinca == fincaJson.get('codFinca')).one()
                    #Crear FincaUsario
                    fincaUsuario = hlmodel.FincaUsuario()
                    fincaUsuario.isActiv = True
                    #Asociar Finca a ficnaUsuario
                    fincaUsuario.finca = fincaRst
                    #Asociar usuario a fincaUsuario
                    usuarioRst.fincaUsuarioList.append(fincaUsuario)                
                    
            #En caso de ser una asociacion nueva
            for fincaJson in listFincaJson:
                i = 0
                for fincaUsr in fincaUsuarioListRst:
                    if(fincaJson.get('codFinca') == fincaUsr.codFinca):      
                        i += 1
                if(i ==0 ):
                    fincaRst = Finca.query.filter(hlmodel.Finca.codFinca == fincaJson.get('codFinca')).one()
                    fincaUsuario = hlmodel.FincaUsuario()
                    fincaUsuario.isActiv = True
                    fincaUsuario.finca = fincaRst
                    usuarioRst.fincaUsuarioList.append(fincaUsuario)
                    saveEntidadSinCommit(fincaUsuario)    

        elif (not fincaUsuarioListRst) and (listFincaJson):
            for fincaJson in listFincaJson:
                fincaRst = Finca.query.filter(hlmodel.Finca.codFinca == fincaJson.get('codFinca')).one()
                fincaUsuario = hlmodel.FincaUsuario()
                fincaUsuario.isActiv = True
                fincaUsuario.finca = fincaRst
                usuarioRst.fincaUsuarioList.append(fincaUsuario)
                saveEntidadSinCommit(fincaUsuario)              
        Commit()      
        return ResponseOk()   
    except Exception as e:
        Rollback()
        return ResponseException(e)

def getUsuarioByName(nombre):
    try:
        print(nombre)
        #usuario = Usuario.query.filter(Usuario.usuario == nombre).first()
        usuario = Usuario.query.filter(Usuario.usuario == nombre).one()
        print(usuario)
        return usuario
    except exc.NoResultFound:
        raise Exception('N', 'Usuario no encontrado')
    except Exception as e:
        return ResponseException(e)


def selectAllUser():
    objList=Usuario.query.order_by(Usuario.usuario).all()
    return objList
