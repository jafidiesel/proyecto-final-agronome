from app.extensions import db
from app.repositorio.hlDb import Commit, saveEntidadSinCommit, Rollback
from app.model.hlmodel import Usuario, Rol, FincaUsuario,Finca
from app.uses_cases.moduloConfiguracion.gestionarNomenclador import getNomencladoCod
from app.api.helperApi.hlResponse import ResponseException, ResponseOk
from sqlalchemy.orm import exc


def updateUser(usuarioJson, rolRst, codUsuario, listFincaJson):
    try:
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
        for fincaJson in listFincaJson:
            #Limpiar Json, solo queda el Id
            claves = list(fincaJson.keys())
            for clave in claves:
                if clave!="codFinca":
                    fincaJson.pop(clave,None)
        #Verificar si las Fincas asociadas al usuario de la BD, son iguales o no, a las Fincas del Json
        #Si la Finca traida de la Bd no se encuentra en el Json, setear isActiv = False
        fincaUsuarioListRst = usuarioRst.fincaUsuarioList
        for fincaUsuarioRst in fincaUsuarioListRst:
            finca = fincaUsuarioRst.finca
            fincaTmp = dict(codFinca=finca.codFinca)
            if (fincaTmp not in listFincaJson)or(listFincaJson[0].get("")):
            #Si FincaUsuario tiene asociado un codFinca que NO esta en listFincaJson, actualizar iSActiv a False
            # y fchFin con fecha actual
                fincaUsuarioRst.isActiv = False
                fincaUsuarioRst.fchFin = 
            elif (fincaTmp in listFincaJson):
                #SE ACTUALIZAN LAS FECHAS??? COMO???
                fincaUsuarioRst.isActiv = True
        #En caso de NO 
        for opcionJson in opcionJsonList:
        i = 0
        for parametroOp in paramOpList:
            
            if(opcionJson.get('cod') == parametroOp.codOpcion):      
                i += 1
        from app.model import hlmodel
        if(i ==0 ):
            opcionRst = Opcion.query.filter(hlmodel.Opcion.cod == opcionJson.get('cod')).one()
            parametroOpcion = ParametroOpcion(True)
            parametroOpcion.opcion = opcionRst
            parametroRst.paramOpcion.append(parametroOpcion) 
            saveEntidadSinCommit(parametroOpcion)     
        Commit()
        return ResponseOk()   
    except Exception as e:
        Rollback()
        return ResponseException(e)

def getUsuarioByName(nombre):
    try:
        usuario = Usuario.query.filter(Usuario.usuario == nombre).one()
        return usuario
    except exc.NoResultFound:
        raise Exception('N', 'Usuario no encontrado')
    except Exception as e:
        return ResponseException(e)