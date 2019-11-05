from app.extensions import db
from app.model.hlmodel import Analisis



def selectAnalisisCod(codAnalisis):
    analisis = Analisis.query.filter(Analisis.codAnalisis == codAnalisis).first()
    return analisis