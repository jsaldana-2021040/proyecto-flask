from database import db

class Roles(db.Model):
    __tablename__ = 'roles'

    codRol: int = db.Column('cod_rol', db.SmallInteger, nullable=False, primary_key=True, autoincrement=True)
    nombre: str = db.Column('nombre',  db.String(50), nullable=False)
    descripcion: str = db.Column('descripcion',  db.String(50), nullable=False)
    activo: bool = db.Column('activo', db.Boolean, nullable=True, default=True)
    usuarioCreador: str = db.Column('usuario_creador',  db.String(50), nullable=False)
    usuarioEditor: str = db.Column('usuario_editor',  db.String(50), nullable=True)

    usuarios = db.relationship('Usuarios', backref='rol', lazy=True)

    rolesPermisos = db.relationship('RolesPermisos', backref='rol', lazy=True)