from database import db

class Empresas(db.Model):
    __tablename__ = 'empresas'

    id: int = db.Column('id', db.SmallInteger, nullable=False, primary_key=True, autoincrement=True,)
    nombre: str = db.Column('nombre',  db.String(100), nullable=False)
    direccion: str = db.Column('direccion',  db.String(100), nullable=True)
    telefono: str = db.Column('telefono', db.String(12), nullable=False)
    activo: bool = db.Column('activo', db.Boolean, nullable=True, default=True)