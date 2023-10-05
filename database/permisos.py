from database import db

class Permisos(db.Model):
    __tablename__ = 'permisos'

    codPermiso: int = db.Column('cod_permiso', db.SmallInteger, nullable=False, primary_key=True, autoincrement=True)
    permiso: str = db.Column('modulo',  db.String(50), nullable=False)
    descripcion: str = db.Column('descripcion',  db.String(50), nullable=False)
    activo: bool = db.Column('activo', db.Boolean, nullable=True, default=True)
    usuarioCreador: str = db.Column('usuario_creador',  db.String(50), nullable=False)
    usuarioEditor: str = db.Column('usuario_editor',  db.String(50), nullable=True)
    moduloCod: int = db.Column('modulo_cod', db.SmallInteger, db.ForeignKey('modulos.cod_modulo'), nullable=False)

    rolesPermisos = db.relationship('RolesPermisos', backref='permisos', lazy=True)