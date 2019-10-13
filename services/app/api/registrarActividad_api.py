from flask_restplus import Resource
from app.api.helperApi.hlUrl import urlResgistrarActiv
from app.uses_cases.moduloActividad.registrarActividad import postRegistrarActiv, getRegistrarActiv, putRegistrarActiv, deleteRegistrarActiv, getRegistrarActivCod ,getParametrosFull
from app.api.helperApi.hlResponse import ResponseException

registrarActiv = urlResgistrarActiv

@registrarActiv.route('')
class RegistrarActivHandler(Resource):
    def post(self):
        data = self.api.payload
        return postRegistrarActiv(data)

    def get(self):
        #data = self.api.payload
        return getRegistrarActiv()


@registrarActiv.route('/<int:codActivDetalle>')
class RegistrarActivHandler(Resource):
    def get(self,codActivDetalle):
        return getRegistrarActivCod(codActivDetalle)
    
    
    def put(self,codActivDetalle):
        data = self.api.payload
        return putRegistrarActiv(data,codActivDetalle)
    
    def delete(self,codActivDetalle):
        data = self.api.payload
        return deleteRegistrarActiv(data,codActivDetalle)

@registrarActiv.route('/parametros/<int:codActividad>')
class RegistrarActivHandler(Resource):
     def get(self,codActividad):
        return getParametrosFull(codActividad)