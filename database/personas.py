from database import db

class Personas(db.Model):
    __tablename__ = 'personas'

    codigo: int = db.Column('codigo', db.SmallInteger, nullable=False, primary_key=True, autoincrement=True)
    nombres: str = db.Column('nombres',  db.String(100), nullable=False)
    apellidos: str = db.Column('apellidos',  db.String(100), nullable=False)
    tieneVisa: bool = db.Column('tiene_visa', db.Boolean, nullable=True)
    activo: bool = db.Column('activo', db.Boolean, nullable=True)