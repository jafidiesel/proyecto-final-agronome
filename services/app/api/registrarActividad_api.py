from flask import jsonify
from flask_restplus import Resource
from app.api.helperApi.hlUrl import urlResgistrarActiv
#from app.uses_cases.moduloConfiguracion.gestionarNomenclador import getNomenclador, getNomencladoCod, postNomenclador, putNomenclador, getNomencladorFilter
from app.uses_cases.moduloActividad.registrarActividad import postRegistrarActiv, getRegistrarActiv
from app.api.helperApi.hlResponse import ResponseException

registrarActiv = urlResgistrarActiv

@registrarActiv.route('')
class RegistrarActivHandler(Resource):
    def post(self):
        data = self.api.payload
        return postRegistrarActiv(data)



    def get(self):
        data = self.api.payload
        return getRegistrarActiv(data)