from database import db

class Roles(db.Model):
    __tablename__ = 'roles'

    codRol: int = db.Column('cod_rol', db.SmallInteger, nullable=False, primary_key=True, autoincrement=True)
    tipo: str = db.Column('tipo',  db.String(50), nullable=False)

    usuarios = db.relationship('Usuarios', backref='rol', lazy=True)