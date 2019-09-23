from flask import jsonify
from flask_restplus import Resource
from app.api.helperApi.hlUrl import urlParametro
from app.uses_cases.moduloConfiguracion.gestionarParametro import postParametro,getParametroEstructura, getParametroById, updateParametro,getAllParametros
#from app.uses_cases.moduloConfiguracion.gestionarNomenclador import getNomenclador, getNomencladoCod, postNomenclador, putNomenclador


parametro = urlParametro

@parametro.route('')
class ParametroHandler(Resource):
    def post(self):
        data = self.api.payload
        return postParametro(data)
    def get(self):
        return getAllParametros() 
    def put(self):
        data = self.api.payload
        return updateParametro(data)


@parametro.route('/<string:tipoNomenclador>')
class ParametroHandler(Resource):
    def get(self,tipoNomenclador):
        return getParametroEstructura(tipoNomenclador)

@parametro.route('/<int:id>')
class  ParametroHandler(Resource):
    def get(self, id):
        return getParametroById(id)

