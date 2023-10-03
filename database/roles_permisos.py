from database import db

class RolesPermisos(db.Model):
    __tablename__ = 'roles_permisos'

    codRolPermiso: int = db.Column('cod_rol_permiso', db.SmallInteger, nullable=False, primary_key=True, autoincrement=True)
    rolCod: int = db.Column('rol_cod', db.SmallInteger, db.ForeignKey('roles.cod_rol'))
    permisosCod: int = db.Column('permisos_cod', db.SmallInteger, db.ForeignKey('permisos.cod_permiso'))
    activo: bool = db.Column('activo', db.Boolean, nullable=True, default=True)
    usuarioCreador: str = db.Column('usuario_creador',  db.String(50), nullable=False)
    usuarioEditor: str = db.Column('usuario_editor',  db.String(50), nullable=True)

    roles = db.relationship('Roles', backref='roles', lazy=True)