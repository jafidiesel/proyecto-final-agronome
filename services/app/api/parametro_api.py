from flask import jsonify
from flask_restplus import Resource
from app.api.helperApi.hlUrl import urlParametro
from app.uses_cases.moduloConfiguracion.gestionarParametro import postParametro
#from app.uses_cases.moduloConfiguracion.gestionarNomenclador import getNomenclador, getNomencladoCod, postNomenclador, putNomenclador


parametro = urlParametro

@parametro.route('')
class ParametroHandler(Resource):
    def post(self):
        data = self.api.payload
        return postParametro(data)
    def get(self):
        return getParametros()

""" @parametro.route('/<int:id>')
class  ParametroHandler(Resource):
    def get(self, id):
        data = self.api.payload
        return getNomencladoCod(data,id)

    def put(self,id):
        data = self.api.payload
        return putNomenclador(data,id) """
    