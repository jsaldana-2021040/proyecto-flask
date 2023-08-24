from database import db

class Direcciones(db.Model):
    __tablename__ = 'direcciones'

    codDireccion: int = db.Column('cod_direccion', db.SmallInteger, nullable=False, primary_key=True, autoincrement=True)
    direccion: str = db.Column('direccion',  db.String(150), nullable=True)
    zona: str = db.Column('zona', db.String(50), nullable=False)
    activo: bool = db.Column('activo', db.Boolean, nullable=True, default=True)
    personaCod = db.Column('persona_cod', db.SmallInteger, db.ForeignKey('personas.cod_persona'), nullable=False)