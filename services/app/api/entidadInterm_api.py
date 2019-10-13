from flask import jsonify
from flask_restplus import Resource
from app.api.helperApi.hlUrl import urlEntidadInterm
from app.uses_cases.moduloConfiguracion.gestionarAsociacion import postAsociacion, getAsociacionCod, getAsociaciones, putAsociacion



entidadInterm = urlEntidadInterm


@entidadInterm.route('')
class EntidadIntermHandler(Resource):
    def post(self):
        data = self.api.payload
        return postAsociacion(data)


@entidadInterm.route('/<string:entidadIntermedia>')
class EntidadIntermHandler(Resource):
    def get(self, entidadIntermedia):
        return getAsociaciones(entidadIntermedia)


@entidadInterm.route('/<string:entidadIntermedia>/<int:cod>')
class EntidadIntermHandler(Resource):
    def get(self, entidadIntermedia,cod):
        return getAsociacionCod(entidadIntermedia,cod)        


    def put(self, entidadIntermedia,cod):
        data = self.api.payload
        return putAsociacion(data,entidadIntermedia,cod) 