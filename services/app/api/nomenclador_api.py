from flask import jsonify,make_response
from flask_restplus import Resource
from app.api.helperApi.hlUrl import urlNomenclador
from app.uses_cases.moduloConfiguracion.gestionarNomenclador import getNomenclador, getNomencladoCod, postNomenclador, putNomenclador, getNomencladorFilter
from app.api.helperApi.hlResponse import ResponseException
from app.api.shared.tokenHandler import token_required
from app.api.helperApi.hlResponse import notCheck
from app.uses_cases.moduloSeguridad.checkUrl import checkUrl
from flask import request

nomenclador = urlNomenclador

@nomenclador.route('')
@nomenclador.doc(params={
    "tipoNomenclador": "nombre del nomenclador",
    "nombre": "string",
    "isActiv": "boolean"
},responses={202: 'Flag s', 404: 'Flag:n'})

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
        if (currentUser.rol.nombre =='administrador'):                         
            return getNomenclador(tipoNomenclador)
        else:
            return make_response(jsonify({'message:':'No posee permisos para realizar esta acción'}),404)

    @token_required
    def post(data,currentUser,tipoNomenclador):
        if (currentUser.rol.nombre =='administrador'):                         
            return getNomencladorFilter(data,tipoNomenclador)
        else:
            return make_response(jsonify({'message:':'No posee permisos para realizar esta acción'}),404)

@nomenclador.route('/<string:tipoNomenclador>/<int:cod>')
class  NomencladorHandler(Resource):
    @token_required
    def get(data,currentUser,tipoNomenclador,cod):
        if (currentUser.rol.nombre =='administrador'):                         
        ##tengo que agregar una exceptión ya que el .to_json es parte del objeto, y no puedo econtrar la exceptión primaraia si no encuentro la que to_json no es una funcion de un objeto vacio
            try:    
                obj = getNomencladoCod(tipoNomenclador,cod)
                return (obj.to_json())
            except Exception as e:
                return ResponseException(e)
        else:
            return make_response(jsonify({'message:':'No posee permisos para realizar esta acción'}),404)

    @token_required    
    def put(data,currentUser,tipoNomenclador,cod):
        if (currentUser.rol.nombre =='administrador'):                         
            return putNomenclador(data,tipoNomenclador,cod)
        else:
            return make_response(jsonify({'message:':'No posee permisos para realizar esta acción'}),404)    