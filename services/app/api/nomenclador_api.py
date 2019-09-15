from flask import jsonify
from flask_restplus import Resource
from app.api.helperApi.hlUrl import urlNomenclador
from app.uses_cases.moduloConfiguracion.gestionarNomenclador import getNomenclador, getNomencladoCod, postNomenclador, putNomenclador
from app.api.helperApi.hlResponse import ResponseException


nomenclador = urlNomenclador

@nomenclador.route('')
class NomencladorsHandler(Resource):
    def post(self):
        data = self.api.payload
        return postNomenclador(data)


@nomenclador.route('/<string:tipoNomenclador>')
class NomencladorsHandler(Resource):
    def get(self,tipoNomenclador):
        return getNomenclador(tipoNomenclador)

@nomenclador.route('/<string:tipoNomenclador>/<int:id>')
class  NomencladorHandler(Resource):
    def get(self,tipoNomenclador,id):
        ##tengo que agregar una exceptión ya que el .to_json es parte del objeto, y no puedo econtrar la exceptión primaraia si no encuentro la que to_json no es una funcion de un objeto vacio
        try:    
            obj = getNomencladoCod(tipoNomenclador,id)
            return (obj.to_json())
        except Exception as e:
            return ResponseException(e)
         
    def put(self,tipoNomenclador,id):
        data = self.api.payload
        return putNomenclador(data,tipoNomenclador,id)
    