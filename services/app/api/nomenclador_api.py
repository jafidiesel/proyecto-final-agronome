from flask import jsonify
from flask_restplus import Resource
from app.api.helperApi.hlUrl import urlNomenclador
from app.uses_cases.moduloConfiguracion.gestionarNomenclador import getNomenclador, getNomencladoCod, postNomenclador, putNomenclador


nomenclador = urlNomenclador

@nomenclador.route('')
class NomencladorsHandler(Resource):
    def get(self):
        data = self.api.payload
        return getNomenclador(data)

    def post(self):
        data = self.api.payload
        return postNomenclador(data)

@nomenclador.route('/<int:id>')
class  NomencladorHandler(Resource):
    def get(self, id):
        data = self.api.payload
        return getNomencladoCod(data,id)

    def put(self,id):
        data = self.api.payload
        return putNomenclador(data,id)
    