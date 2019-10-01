from flask import jsonify
from flask_restplus import Resource
from app.api.helperApi.hlUrl import urlEntidadInterm
from app.uses_cases.moduloConfiguracion.gestionarEntidadIntermedia import postEntidadInterm, getEntidadIntermCod, getEntidadInterm, putEntidadInterm
from app.uses_cases.moduloConfiguracion.gestionarAsociacion import postAsociacion, getAsociacionCod
#from app.uses_cases.moduloConfiguracion.gestionarNomenclador import getNomenclador, getNomencladoCod, postNomenclador, putNomenclador


entidadInterm = urlEntidadInterm


@entidadInterm.route('')
class EntidadIntermHandler(Resource):
    def post(self):
        data = self.api.payload
        #print(data)
        return postAsociacion(data)


@entidadInterm.route('/<string:entidadIntermedia>')
class EntidadIntermHandler(Resource):
    def get(self, entidadIntermedia):
        return getEntidadInterm(entidadIntermedia)


@entidadInterm.route('/<string:entidadIntermedia>/<int:id>')
class EntidadIntermHandler(Resource):
    def get(self, entidadIntermedia,id):
        return getAsociacionCod(entidadIntermedia,id)        


    def put(self, entidadIntermedia,id):
        data = self.api.payload
        return putEntidadInterm(data,entidadIntermedia,id) 