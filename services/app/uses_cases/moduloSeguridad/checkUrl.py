import re
from app.api.helperApi.hlUrl import URL_MC, urlActividad,  urlUsuario, urlLogin ,urlNomenclador,urlFinca,urlRecomendacion , urlAnalisis, urlPlan, urlReporte, urlPlanificacion, urlGrupoPlanificacion, urlLibroCampo, urlParcelas

def checkUrl(method,pat,rol):
    urlAux = method + pat #armo url
    nro = re.sub("\D", "", urlAux) #busco si tiene algun numero
    url = re.sub(nro,"",urlAux)
    isCheck = False


    #Mudolo de configuración 

    #Nomencladores
    MCNOM = '/' + urlNomenclador.name
    MCNOM_GETS = 'GET' + MCNOM
    MCNOM_POST_FILTER = 'POST' + MCNOM + '/'
    isGetNomenclador = False
    isPostFilterNomenclador = False

    if url.count(MCNOM_GETS)>0:
        url = MCNOM_GETS
        isGetNomenclador = True

    if url.count(MCNOM_POST_FILTER)>0:
        url = MCNOM_POST_FILTER
        isPostFilterNomenclador = True
 
    #configuración de parametros y asociaciones
    MC = URL_MC
    if url.count(URL_MC)> 0 and not isGetNomenclador and not isPostFilterNomenclador:
        url = MC
    

    #Modulo de seguridad 
    isAccount = False
    MSACC = urlUsuario.name + '/account'
    if url.count(MSACC)>0:
        isAccount = True
        url = MSACC 

    isLogin=False 
    MSLOG = urlLogin.name #login     
    if url.count(MSLOG)>0 and not isAccount:
        isLogin = True
        url = MSLOG

    MSUSU =  urlUsuario.name  #usuario
    if url.count(MSUSU)>0 and not isLogin and not isAccount: #tengo que hacer esta logica porque comparten url con el login
        url = MSUSU


    #Modulo Actividades
    MA = '/' + urlActividad.name
    MA_REG = 'POST' + MA + '/registrar'
    MA_CON = 'POST' + MA + '/consultar'
    MA_GET = 'GET'  + MA + '/'
    MA_PUT = 'PUT'  + MA + '/'
    MA_DELETE = 'DELETE' + MA + '/'
    MA_PARAM = 'GET' + MA + '/parametros/'

    #Libro Campo 
    LC = '/' + urlLibroCampo.name
    LC_POST = 'POST' + LC
    LC_FIN  = 'POST' + LC + '/finalizar'
    LC_REC  = 'POST' + LC + '/recomendacion'

    #Modulo de Gestion de Finca
    MGF = '/' + urlFinca.name
    MGF_POST =  'POST' + MGF 
    MGF_GETS = 'GET' + MGF
    MGF_GET = MGF_GETS  + '/'
    MGF_PUT = 'PUT' + MGF + '/'
    
    #Modulo de Recomendaciones
    MRREG = '/' + urlRecomendacion.name
    MRREG_POST =  'POST' + MRREG + '/registrar'
    MRRECOMACTIV_POST = 'POST' + MRREG + '/actividad' 
    MRREG_GET = 'GET' + MRREG + '/'
    MRREG_PARAM = 'GET' + MRREG + '/parametros/'
   
   
    #Helper
    #-analisis
    HLA = '/' + urlAnalisis.name
    HLA_POST = 'POST' + HLA
    HLA_GET  = 'GET' + HLA + '/'
    HLA_PARAM = 'GET' + HLA + '/parametros/'
    #-plan
    HLP = '/' + urlPlan.name
    HLP_POST = 'POST' + HLP
    HLP_GET  = 'GET' + HLP + '/'
    HLP_PARAM = 'GET' + HLP + '/parametros/'

    #MODULO DE REPORTES
    MREPOR = 'POST/' + urlReporte.name #son todos POST
    MREPOR_ACTIVBAR = MREPOR + '/actividadGfBar'
    MREPOR_RECOMPIE = MREPOR + '/recomendacionGfPie'
    MREPOR_ACTIVDUALBAR = MREPOR + '/actividadDualGfBar'
    MREPOR_ACTIVOPTIPIE = MREPOR + '/actividadOptionGfPie'

    #MODULO DE PLANIFICACION
    #Grupo Planificacion
    MPGRUPO = '/' + urlGrupoPlanificacion.name
    #print(MPGRUPO)
    MPGRUPO_GET = 'GET' + MPGRUPO + '/'
    MPGRUPO_POST = 'POST' + MPGRUPO
    #print(MPGRUPO_GET)
    #Planificacion 
    MPLAN = '/' + urlPlanificacion.name
    MPLAN_POST = 'POST' + MPLAN
    MPLAN_GET = 'GET' + MPLAN + '/'
    #Parcelas
    MPPAR = '/' + urlParcelas.name
    MPAR_GET = 'GET' + MPPAR + '/'

    #PERMISOS:
    default = (
        MSLOG,MSACC,
        MCNOM_GETS,MCNOM_POST_FILTER,                 #Modulo de Configuración (Nomencladores)
        MGF_GETS, MGF_GET,                            #Modulo de finca
        MREPOR_ACTIVBAR,MREPOR_RECOMPIE,MREPOR_ACTIVDUALBAR,MREPOR_ACTIVOPTIPIE,                         #Modulo de reporte
        LC_POST, LC_REC                                #libro campo
        ) #todos

    administrador = (
        MC,                                           #Modulo de Confiraución (Parametros y asociaciones)
        MSUSU,                                        #Modulo de seguridad
        MA_REG, MA_CON, MA_GET, MA_PUT, MA_DELETE, MA_PARAM, #Modulo de actividad
        MGF_POST,MGF_PUT,                             #Modulo de finca
        MRREG_POST, MRREG_GET, MRRECOMACTIV_POST, MRREG_PARAM, #Modulo de recomendaciones
        HLA_GET, HLA_POST, HLA_PARAM, HLP_POST, HLP_GET , HLP_PARAM, #Helper Analisis - Plan
        LC_FIN,                                          #libro de campo
        MPLAN_POST                                          #Modulo de planificiación
    ) + default
    
    encargadofinca = (
        MA_REG, MA_CON, MA_GET, MA_PUT, MA_DELETE, MA_PARAM, #Modulo de actividad
        MGF_POST,MGF_PUT,                              #Modulo de finca
        MPLAN_POST, MPLAN_GET, MPGRUPO_GET, MPGRUPO_POST, MPAR_GET,   #Modulo Planificacion
        MRRECOMACTIV_POST,                              #modulo de recomendaciones
        LC_FIN                                      #libro de campo
         ) + default
    
    ingeniero = (  
        MA_CON, MA_GET,                         #Modulo de actividad
        MRREG_POST, MRREG_GET, MRRECOMACTIV_POST, MRREG_PARAM, #Modulo de recomendaciones
        HLA_GET, HLA_POST, HLA_PARAM, HLP_POST, HLP_GET , HLP_PARAM, #Helper Analisis - Plan
        MPGRUPO_GET, MPGRUPO_POST, MPAR_GET         #Modulo Planificacion
         )+ default

    supervisor = (  
        MA_REG, MA_CON, MA_GET, MA_PUT, MA_DELETE, MA_PARAM  #Modulo de actividad
         )+ default


    #CHECK FINAL
    roles= {
    "administrador":administrador ,
    "encargadofinca":encargadofinca,
    "ingeniero":ingeniero,
    "supervisor": supervisor,
    }

    isCheck = url in roles[rol]
    #print(url)
    return isCheck
    