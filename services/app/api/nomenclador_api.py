from flask import jsonify
from flask_restplus import Resource
from app.api.helperApi.hlUrl import urlNomenclador
from app.uses_cases.moduloConfiguracion.gestionarNomenclador import getNomenclador, getNomencladoCod, postNomenclador, putNomenclador, getNomencladorFilter
from app.api.helperApi.hlResponse import ResponseException

nomenclador = urlNomenclador

@nomenclador.route('')
@nomenclador.doc(params={
    "tipoNomenclador": "nombre del nomenclador",
    "nombre": "string",
    "isActiv": "boolean"
},responses={202: 'Flag s', 404: 'Flag:n'})

class NomencladorsHandler(Resource):
    def post(self):
        data = self.api.payload
        return postNomenclador(data)


@nomenclador.route('/<string:tipoNomenclador>')
class NomencladorsHandler(Resource):
    def get(self,tipoNomenclador):
        return getNomenclador(tipoNomenclador)

    def post(self,tipoNomenclador):
        data = self.api.payload
        return getNomencladorFilter(data,tipoNomenclador)

@nomenclador.route('/<string:tipoNomenclador>/<int:cod>')
class  NomencladorHandler(Resource):
    def get(self,tipoNomenclador,cod):
        ##tengo que agregar una exceptión ya que el .to_json es parte del objeto, y no puedo econtrar la exceptión primaraia si no encuentro la que to_json no es una funcion de un objeto vacio
        try:    
            obj = getNomencladoCod(tipoNomenclador,cod)
            return (obj.to_json())
        except Exception as e:
            return ResponseException(e)
         
    def put(self,tipoNomenclador,cod):
        data = self.api.payload
        return putNomenclador(data,tipoNomenclador,cod)
    