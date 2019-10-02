#definiciones de las rutas
from flask_restplus import Namespace

#modulo de configuraciones"
URL_MC = 'api/configuracion/'
urlNomenclador = Namespace(URL_MC + 'nomenclador', description='Modulo de Configuraciones')
urlParametro = Namespace(URL_MC + 'parametro')
urlEntidadInterm = Namespace(URL_MC + 'asociar')

#modulo de recursos
URL_MR = 'api/recurso/'
urlRecurso=Namespace(URL_MR)

#modulo de actividades"
URL_MA= 'api/actividad/'
urlResgistrarActiv = Namespace(URL_MA + 'registrar', description='Registrar Actividad')

#modulo de seguridad
URL_MU = 'api/users'
urlUsuario = Namespace(URL_MU, description = 'Registrar Usuario')