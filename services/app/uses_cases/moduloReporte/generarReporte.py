from app.repositorio.repositorioGenerarReporte import  actividadGfBarDB,recomendacionGfPieDB , siembraGfBarDB

def actividadGfBar(data,currentUser):
    fchDesde = data.get('fchDesde')
    fchHasta = data.get('fchHasta')
    parmIn = dict (fchDesde =fchDesde, fchHasta=fchHasta)
    
    dtoActividad=actividadGfBarDB(parmIn)
    keys = dtoActividad.keys()
    dtoData= []
   
    for key in keys:
        data=[]
        data.append(dtoActividad[key])
        dtoAuxData=dict(data=data,label=key)
        dtoData.append(dtoAuxData)

    labelPpal = fchDesde + ' - ' + fchHasta

    dtoReporte= dict(dataset=dtoData,label=labelPpal)
    return dtoReporte


def recomendacionGfPie(data,currentUser):
    fchDesde = data.get('fchDesde')
    fchHasta = data.get('fchHasta')
    parmIn = dict (fchDesde =fchDesde, fchHasta=fchHasta)
    
    dtoRecom = recomendacionGfPieDB(parmIn)
    keys = dtoRecom.keys()
    number=[]
    labelPpal=[]
    for key in keys:
        number.append(dtoRecom[key])
        labelPpal.append(key)
    dtoAux=dict(number=number)

    dtoReporte= dict(dataset=dtoAux,label=labelPpal)
    return dtoReporte


def siembraGfBar(data,currentUser):
    fchDesde = data.get('fchDesde')
    fchHasta = data.get('fchHasta')
    parmIn = dict (fchDesde =fchDesde, fchHasta=fchHasta)
    dtoReporte=siembraGfBarDB(parmIn)
    return dtoReporte