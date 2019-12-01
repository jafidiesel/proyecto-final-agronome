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
URL_MA= 'api/actividad'
urlActividad = Namespace(URL_MA, description='Registrar y Consultar Actividades')

#libro de campo (no es un modulo pero es importatante x eso se desacopla)
URL_LC = 'api/libroCampo'
urlLibroCampo = Namespace(URL_LC, description= 'Libro de Campo')


#modulo de seguridad
URL_MU = 'api/users'
urlUsuario = Namespace(URL_MU , description = 'Registrar Usuario')
urlLogin = Namespace(URL_MU +'/login', description = 'Login Usuario')


#modulo de gestion de finca
URL_MGF = 'api/finca'
urlFinca = Namespace(URL_MGF, description = 'Gestionar Finca')

#modulo de recomendacion
URL_MR = 'api/recomendacion'
urlRecomendacion = Namespace (URL_MR, description = 'Registrar Recomendación')

#modulo de helper 
URL_HL = 'api/hl'
#helperAnalisis
urlAnalisis = Namespace (URL_HL + '/analisis', description = 'Helper analisis')
#helperPlan
urlPlan = Namespace (URL_HL + '/plan', description = 'Helper plan')

#modulo de planificacion
URL_MP = 'api/planificacion'
urlPlanificacion = Namespace(URL_MP,desciption = 'Gestionar planificacion ')
urlGrupoPlanificacion = Namespace(URL_MP +'/grupos', description = 'Gestionar grupos de planificaciones' )
urlParcelas = Namespace(URL_MP +'/parcelas', description = 'Gestionar grupos de planificaciones' )


#modulo de reportes
URL_MREPOR = 'api/reporte'
urlReporte = Namespace (URL_MREPOR, description= 'Reportes')