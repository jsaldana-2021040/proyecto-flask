from database import db

class Personas(db.Model):
    __tablename__ = 'personas'

    codPersona: int = db.Column('cod_persona', db.SmallInteger, nullable=False, primary_key=True, autoincrement=True)
    nombres: str = db.Column('nombres',  db.String(100), nullable=False)
    apellidos: str = db.Column('apellidos',  db.String(100), nullable=False)
    tieneVisa: bool = db.Column('tiene_visa', db.Boolean, nullable=True)
    activo: bool = db.Column('activo', db.Boolean, nullable=True, default=True)
    empresaCod = db.Column('empresa_cod', db.SmallInteger, db.ForeignKey('empresas.cod_empresa'), nullable=False)