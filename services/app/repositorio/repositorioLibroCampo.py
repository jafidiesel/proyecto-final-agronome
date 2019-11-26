from app.extensions import db
from app.model.hlmodel import LibroCampo

def selectLibroCod(codLibroCampo):
    obj = LibroCampo.query.filter(LibroCampo.codLibroCampo ==codLibroCampo).first()
    return obj