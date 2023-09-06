from database import db

class Usuarios(db.Model):
    __tablename__ = 'usuarios'

    codUsuario: int = db.Column('cod_usuario', db.SmallInteger, nullable=False, primary_key=True, autoincrement=True)
    email: str = db.Column('email',  db.String(50), nullable=False)
    password: str = db.Column('password',  db.String(60), nullable=False)
    activo: bool = db.Column('activo', db.Boolean, nullable=True, default=True)
    rolCod = db.Column('rol_cod', db.SmallInteger, db.ForeignKey('roles.cod_rol'), nullable=False)

    def getUserByIdentity(identity: str):
        usuario = db.session.query(Usuarios).filter(Usuarios.email == identity).first()
        return usuario