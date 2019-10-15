from flask_restplus import Resource
from app.api.helperApi.hlUrl import urlResgistrarActiv
from app.uses_cases.moduloActividad.registrarActividad import postRegistrarActiv, getRegistrarActiv, putRegistrarActiv, deleteRegistrarActiv, getRegistrarActivCod ,getParametrosFull
from app.api.helperApi.hlResponse import ResponseException, notCheck
from app.api.shared.tokenHandler import token_required

registrarActiv = urlResgistrarActiv

@registrarActiv.route('')
class RegistrarActivHandler(Resource):
    @token_required
    def post(data,currentUser):
        if (currentUser.rol.nombre =='administrador' or currentUser.rol.nombre =='encargadofinca' ): 
            return postRegistrarActiv(data)
        else:
            return notCheck()

    @token_required
    def get(data,currentUser):
        if (currentUser.rol.nombre =='administrador' or currentUser.rol.nombre =='encargadofinca' ): 
            return getRegistrarActiv()
        else:
            return notCheck()


@registrarActiv.route('/<int:codActivDetalle>')
class RegistrarActivHandler(Resource):
    @token_required
    def get(data,currentUser,codActivDetalle):
        if (currentUser.rol.nombre =='administrador' or currentUser.rol.nombre =='encargadofinca' ):
            return getRegistrarActivCod(codActivDetalle)
        else:
            return notCheck()

    @token_required
    def put(data,currentUser,codActivDetalle):
        if (currentUser.rol.nombre =='administrador' or currentUser.rol.nombre =='encargadofinca' ):
            return putRegistrarActiv(data,codActivDetalle)
        else:
            return notCheck() 

    @token_required
    def delete(data,currentUser,codActivDetalle):
        if (currentUser.rol.nombre =='administrador' or currentUser.rol.nombre =='encargadofinca' ):
            return deleteRegistrarActiv(data,codActivDetalle)
        else:
            return notCheck()

@registrarActiv.route('/parametros/<int:codActividad>')
class RegistrarActivHandler(Resource):
    @token_required
    def get(data,currentUser,codActividad):
        if (currentUser.rol.nombre =='administrador' or currentUser.rol.nombre =='encargadofinca' ):
            return getParametrosFull(codActividad)
        else:
            return notCheck()