from flask import jsonify
from flask_restplus import Resource
from app.api.helperApi.hlUrl import urlEntidadInterm
from app.uses_cases.moduloConfiguracion.gestionarAsociacion import postAsociacion, getAsociacionCod, getAsociaciones, putAsociacion
from app.api.shared.tokenHandler import token_required
from app.api.helperApi.hlResponse import notCheck


entidadInterm = urlEntidadInterm


@entidadInterm.route('')
class EntidadIntermHandler(Resource):
    @token_required
    def post(data,currentUser):
        return postAsociacion(data) 
     
        
@entidadInterm.route('/<string:entidadIntermedia>')
class EntidadIntermHandler(Resource):
    @token_required
    def get(data,currentUser, entidadIntermedia):
        return getAsociaciones(entidadIntermedia)
        
            


@entidadInterm.route('/<string:entidadIntermedia>/<int:cod>')
class EntidadIntermHandler(Resource):
    @token_required
    def get(data,currentUser,entidadIntermedia,cod):
        return getAsociacionCod(entidadIntermedia,cod)        
        
            

    @token_required
    def put(data,currentUser, entidadIntermedia,cod):
        return putAsociacion(data,entidadIntermedia,cod) 
        
            