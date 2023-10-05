from database import db

class Modulos(db.Model):
    __tablename__ = 'modulos'

    codModulo: int = db.Column('cod_modulo', db.SmallInteger, nullable=False, primary_key=True, autoincrement=True)
    modulo: str = db.Column('modulo',  db.String(50), nullable=False)
    descripcion: str = db.Column('descripcion',  db.String(50), nullable=False)
    activo: bool = db.Column('activo', db.Boolean, nullable=True, default=True)
    usuarioCreador: str = db.Column('usuario_creador',  db.String(50), nullable=False)
    usuarioEditor: str = db.Column('usuario_editor',  db.String(50), nullable=True)

    permisos = db.relationship('Permisos', backref='modulo', lazy=True)

    