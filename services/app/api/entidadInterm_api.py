from flask import jsonify
from flask_restplus import Resource
from app.api.helperApi.hlUrl import urlEntidadInterm
from app.uses_cases.moduloConfiguracion.gestionarEntidadIntermedia import postEntidadInterm, getEntidadIntermCod, getEntidadInterm, putEntidadInterm
#from app.uses_cases.moduloConfiguracion.gestionarNomenclador import getNomenclador, getNomencladoCod, postNomenclador, putNomenclador


entidadInterm = urlEntidadInterm


@entidadInterm.route('')
class EntidadIntermHandler(Resource):
    def post(self):
        data = self.api.payload
        print(data)
        return postEntidadInterm(data)


@entidadInterm.route('/<string:entidadIntermedia>')
class EntidadIntermHandler(Resource):
    def get(self, entidadIntermedia):
        return getEntidadInterm(entidadIntermedia)


@entidadInterm.route('/<string:entidadIntermedia>/<int:cod>')
class EntidadIntermHandler(Resource):
    def get(self, entidadIntermedia,cod):
        return getEntidadIntermCod(entidadIntermedia,cod)        


    def put(self, entidadIntermedia,cod):
        data = self.api.payload
        return putEntidadInterm(data,entidadIntermedia,cod) 