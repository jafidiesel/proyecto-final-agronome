#definiciones de las rutas
from flask_restplus import Namespace
#modulo de configuraciones"
URL_MC = 'api/configuracion/'
urlNomenclador = Namespace(URL_MC + 'nomenclador', description='Modulo de Configuraciones')
urlParametro = Namespace(URL_MC + 'parametro', description= 'Gestionar Parametros')
urlEntidadInterm = Namespace(URL_MC + 'asociar', description= 'Gestionar Asociaciones')

#modulo de recursos
URL_MR = 'api/recurso/'
urlRecurso=Namespace(URL_MR)

#modulo de actividades"
URL_MA= 'api/actividad/'
urlResgistrarActiv = Namespace(URL_MA + 'registrar', description='Registrar Actividad')

#modulo de seguridad
URL_MU = 'api/users'
urlUsuario = Namespace(URL_MU , description = 'Registrar Usuario')
urlLogin = Namespace(URL_MU +'/login', description = 'Login Usuario')


#modulo de gestion de finca
URL_MGF = 'api/finca'
urlFinca = Namespace(URL_MGF, description = 'Gestionar Finca')

#modulo de recomendacion
URL_MR = 'api/recomendacion'
urlRegistrarRecom = Namespace (URL_MR, description = 'Registrar Recomendación')




