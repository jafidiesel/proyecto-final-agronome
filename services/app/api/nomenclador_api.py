from flask import jsonify
from flask_restplus import Resource
from app.api.helperApi.hlUrl import urlNomenclador
from app.uses_cases.moduloConfiguracion.gestionarNomenclador import getNomenclador, getNomencladoCod, postNomenclador, putNomenclador


nomenclador = urlNomenclador

@nomenclador.route('/<string:tipoNomenclador>')
class NomencladorsHandler(Resource):
    def get(self,tipoNomenclador):
        return getNomenclador(tipoNomenclador)


@nomenclador.route('')
class NomencladorsHandler(Resource):
    def post(self):
        data = self.api.payload
        return postNomenclador(data)

@nomenclador.route('/<string:tipoNomenclador>/<int:id>')
class  NomencladorHandler(Resource):
    def get(self,tipoNomenclador,id):
        obj = getNomencladoCod(tipoNomenclador,id)
        return jsonify(obj.to_json())

    def put(self,tipoNomenclador,id):
        data = self.api.payload
        return putNomenclador(data,tipoNomenclador,id)
    