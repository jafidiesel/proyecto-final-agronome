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
        return postNomenclador(data) 
       

@nomenclador.route('/<string:tipoNomenclador>')
class NomencladorsHandler(Resource):
    @token_required
    def get(data,currentUser,tipoNomenclador): 
        return getNomenclador(tipoNomenclador)


    @token_required
    def post(data,currentUser,tipoNomenclador):      
        return getNomencladorFilter(data,tipoNomenclador)

@nomenclador.route('/<string:tipoNomenclador>/<int:cod>')
class  NomencladorHandler(Resource):
    @token_required    
    def get(data,currentUser,tipoNomenclador,cod):
        try:    
            obj = getNomencladoCod(tipoNomenclador,cod)
            return (obj.to_json())
        except Exception as e:
            return ResponseException(e)
       
    @token_required 
    def put(data,currentUser,tipoNomenclador,cod):            
        return putNomenclador(data,tipoNomenclador,cod)
    
