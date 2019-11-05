from app.extensions import db
from app.model.hlmodel import Finca


def selectFincaCod(codFinca):
    finca = Finca.query.filter(Finca.codFinca == codFinca).first()
    return finca

def selectFinca():
    fincas = Finca.query.filter(Finca.isActiv == True).all()
    return fincas