from app.repositorio.hlDb import saveEntidad, selectAll, selectByCod, updateEntidad, selectByisActiv
from app.model.hlmodel import Finca, Parcela, Cuadro, EstadoPlanificacion, GrupoCuadro, CuadroCultivo, Cuadro
from app.uses_cases.moduloPlanificacion.shared.sharedFunctions import tipoCultivoListToDict
from app.repositorio.repositorioGestionarFinca import selectFincaCod, selectFinca

#{'codFinca': cod }
#
#
def getParcelasLibres(data):    
    #Extraer Finca de Json
    codFincaJson = data.get('codFinca')
    #Buscar Finca
    fincaRst = selectFincaCod(codFincaJson)
    if not fincaRst: 
            raise Exception('N','No existe finca con código ' + str(codFincaJson))
    #Buscar Parcelas asociadas
    parcelasRstList = fincaRst.parcelaList
    dtoGeneral = []
    dtoParcela = []
    #Por cada parcela, leer cuadro asociado
    dtoCuadroList = []
    for parcelasRst in parcelasRstList:
        dtoParcela.append(parcelasRst)
        dtoCuadroList.append(parcelasRst.cuadroList)
        dtoParcela.append(dtoCuadroList)
        dtoGeneral.append(dtoParcela)
    
    #Leer instancias Planificación asociadas a Finca instanciada.
    planificacionListRst = fincaRst.planificacionList
    dtoCuadroListAux = []
    if not planificacionListRst:
        return dtoGeneral
    else:
        for planificacionRst in planificacionListRst:
            if (planificacionRst.estadoPlanificacion.nombre == "en curso" ):
                for grupoCuadro in planificacionRst.grupoCuadroList:
                    parcelaGrupo = grupoCuadro.parcela
                    #Armar dto con encabezado parcela y cuerpo cuadro
                    for cuadroCultivo in grupoCuadro.cuadroCultivoList:
                        cuadroGrupo = cuadroCultivo.cuadro

    #Comparar las listas de parcelas con los cuadros
    #Si la parcela no esta en la lista de planificaion, se agregan todos sus cuadros al dto final --> Comparar
    #elementos de lista general contra lista de planificacion
    #Si la parcela esta en la lista, se agregan al dto final, los cuadros que no se encuentren en la lista
    #Comparar elementos de lista planificacion contra lista general


    