# from app.model import hlmodel
# from app.model.hlmodel import TipoRecurso, Recurso
# from app.api.helperApi.hlDb import saveEntidad, selectAll, selectByCod, updateEntidad, selectTipoRecurso
# from app.api.helperApi.hlResponse import ResponseException


# def postRecurso(data):
#         print(data)
#         codTipo = data.get('codTipo')
#         tipo = selectTipoRecurso(TipoRecurso,codTipo)
#         print(tipo.cod)
#         Rec=Recurso(
#             nombre=data.get('nombre'),
#             isActiv=data.get('isActiv'),
#             tipo = tipo.cod
#             )
            
#         saveEntidad(Rec)   
#         return Rec