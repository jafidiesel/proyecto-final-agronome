from flask import jsonify
from flask_restplus import Resource
from app.api.helperApi.hlUrl import urlParametro
from app.uses_cases.moduloConfiguracion.gestionarParametro import postParametro,getParametroEstructura, getParametroById, updateParametro,getAllParametros
#from app.uses_cases.moduloConfiguracion.gestionarNomenclador import getNomenclador, getNomencladoCod, postNomenclador, putNomenclador
from app.uses_cases.moduloSeguridad.gestionarUsuarios import postUser
from app.api.shared.tokenHandler import token_required
from app.api.helperApi.hlResponse import notCheck
from app.uses_cases.moduloSeguridad.checkUrl import checkUrl
from flask import request

parametro = urlParametro

@parametro.route('')
class ParametroHandler(Resource):
    @token_required
    def post(data,currentUser):
        isCheck = checkUrl(request.method,request.path,currentUser.rol.nombre)
        if isCheck:
            return postParametro(data)
        else:
            return notCheck()
    @token_required
    def get(data,currentUser):
        isCheck = checkUrl(request.method,request.path,currentUser.rol.nombre)
        if isCheck:
            return getAllParametros() 
        else:
            return notCheck()
        
    @token_required
    def put(data,currentUser):
        #Tira un 404 a pesar de que las url coinciden.
        """ isCheck = checkUrl(request.method,request.path,currentUser.rol.nombre)
        if isCheck:
            return updateParametro(data)
        else:
            return notCheck() """

        #Esto SI funciona
        if (currentUser.rol.nombre =='administrador'):            
            return updateParametro(data)
        else:
            return make_response(jsonify({'message:':'No posee permisos para realizar esta acción'}),404)


@parametro.route('/<string:tipoNomenclador>')
class ParametroHandler(Resource):
    @token_required
    def get(data,currentUser,tipoNomenclador):
        isCheck = checkUrl(request.method,request.path,currentUser.rol.nombre)
        if isCheck:
            return getParametroEstructura(tipoNomenclador)
        else:
            return notCheck()

@parametro.route('/<int:cod>')
class  ParametroHandler(Resource):
    @token_required
    def get(data,currentUser, cod):
        isCheck = checkUrl(request.method,request.path,currentUser.rol.nombre)
        if isCheck:
            return getParametroById(cod)
        else:
            return notCheck()

