from flask import jsonify, request
from flask_restplus import Resource
from app.api.helperApi.hlUrl import urlNomenclador
from app.uses_cases.moduloConfiguracion.gestionarNomenclador import getNomenclador, getNomencladoCod, postNomenclador, putNomenclador, getNomencladorFilter
from app.api.shared.tokenHandler import token_required
from app.api.helperApi.hlResponse import ResponseException, notCheck
from app.uses_cases.moduloSeguridad.checkUrl import checkUrl

nomenclador = urlNomenclador

@nomenclador.route('')
class NomencladorsHandler(Resource):
    @token_required
    def post(data,currentUser):
        isCheck = checkUrl(request.method,request.path,currentUser.rol.nombre)
        if isCheck:
            return postNomenclador(data)
        else:
            return notCheck()

@nomenclador.route('/<string:tipoNomenclador>')
class NomencladorsHandler(Resource):
    @token_required
    def get(data,currentUser,tipoNomenclador):
        isCheck = checkUrl(request.method,request.path,currentUser.rol.nombre)
        if isCheck:
            return getNomenclador(tipoNomenclador)
        else:
            return notCheck()

    @token_required
    def post(data,currentUser,tipoNomenclador):
        isCheck = checkUrl(request.method,request.path,currentUser.rol.nombre)
        if isCheck:
            return getNomencladorFilter(data,tipoNomenclador)
        else:
            return notCheck()

@nomenclador.route('/<string:tipoNomenclador>/<int:cod>')
class  NomencladorHandler(Resource):
    @token_required    
    def get(data,currentUser,tipoNomenclador,cod):
        isCheck = checkUrl(request.method,request.path,currentUser.rol.nombre)
        if isCheck:
        ##tengo que agregar una exceptión ya que el .to_json es parte del objeto, y no puedo econtrar la exceptión primaraia si no encuentro la que to_json no es una funcion de un objeto vacio
            try:    
                obj = getNomencladoCod(tipoNomenclador,cod)
                return (obj.to_json())
            except Exception as e:
                return ResponseException(e)
        else:
            return notCheck()
    @token_required 
    def put(data,currentUser,tipoNomenclador,cod):
        isCheck = checkUrl(request.method,request.path,currentUser.rol.nombre)
        if isCheck:
            return putNomenclador(data,tipoNomenclador,cod)
        else:
            return notCheck()
    