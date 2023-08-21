from database import db

class Personas(db.Model):
    __tablename__ = 'almacenes'

    codigo = db.Column('codigo', db.SmallInteger, nullable=False, primary_key=True, autoincrement=True)
    nombres = db.Column('nombres',  db.String(100), nullable=False)
    apellidos = db.Column('apellidos',  db.String(100), nullable=False)
    tieneVisa = db.Column('tiene_visa', db.Boolean, nullable=True)
    activo = db.Column('activo', db.Boolean, nullable=True)