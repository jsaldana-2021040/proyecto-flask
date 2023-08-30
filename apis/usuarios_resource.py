from flask_restx import Namespace, Resource, reqparse, inputs, abort
from database import db, Usuarios, Roles
from .models import usuarioModel, usuarioBodyRequestModel, usuariosPgModel
from flask_jwt_extended import get_jwt_identity, jwt_required

ns = Namespace('Usuarios')
    
@ns.route('')
class UsuariosResource(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('email', type=str, location='args')
    parser.add_argument('activo', type=inputs.boolean, location='args')

    @ns.expect(parser)
    @ns.marshal_list_with(usuarioModel)
    def get(self):
        args = self.parser.parse_args()
        query = db.session.query(Usuarios)

        if args['email'] != None:
            query = query.filter(Usuarios.zona.ilike('%'+args['email']+'%'))
        if args['activo'] != None:
            query = query.filter(Usuarios.activo == args['activo'])
        
        return query.order_by(Usuarios.codUsuario).all()

    @ns.expect(usuarioBodyRequestModel, validate=True)
    @ns.marshal_with(usuarioModel)
    def post(self):
            try:
                datos = ns.payload
                roles = db.session.query(Roles).filter(Roles.tipo == "CLIENT").first()
                print(roles)
                usuario = Usuarios(email = datos['email'], password = datos['password'], rolCod = roles.codRol)
                db.session.add(usuario)
                db.session.commit()
                return usuario
            except:
                db.session.rollback()

@ns.route('/admin')
class UsuariosResource(Resource):

    @ns.expect(usuarioBodyRequestModel, validate=True)
    @ns.marshal_with(usuarioModel)
    @jwt_required()
    @ns.doc(security='apikey')
    def post(self):
            usuario = Usuarios.getUserByIdentity(get_jwt_identity())
            if usuario.rol.tipo != "ADMIN":
                abort(403, 'El usuario no tiene permisos suficientes')
            try:
                datos = ns.payload
                usuario = Usuarios(email = datos['email'], password = datos['password'], rolCod = usuario.rolCod)
                db.session.add(usuario)
                db.session.commit()
                return usuario
            except:
                db.session.rollback()


@ns.route('/<int:id>')
class UsuarioResource(Resource):

    @ns.marshal_with(usuarioModel)
    def get(self, id):
        return db.session.query(Usuarios).get(id)

    @ns.expect(usuarioBodyRequestModel, validate=True)
    @ns.marshal_with(usuarioModel)
    @jwt_required()
    def put(self, id):

        usuario = Usuarios.getUserByIdentity(get_jwt_identity())
        if usuario.rol.tipo != "ADMIN":
            abort(403, 'El usuario no tiene permisos suficientes')
       
        datos = ns.payload
        usuario =  db.session.query(Usuarios).get(id)
        usuario.email = datos['email']
        usuario.password = datos['password']
        db.session.commit()
        return usuario

    @ns.marshal_with(usuarioModel)
    @jwt_required()
    def delete(self, id):
        
        usuario = Usuarios.getUserByIdentity(get_jwt_identity())
        if usuario.rol.tipo != "ADMIN":
            abort(403, 'El usuario no tiene permisos suficientes')
        
        usuario =  db.session.query(Usuarios).get(id)
        usuario.activo = False
        db.session.commit()
        return usuario

@ns.route('/pg')
class UsuariosPgResource(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('pagina', default=1, type=int)
    parser.add_argument('porPagina', default=10, type=int)
    parser.add_argument('email', type=str, location='args')
    parser.add_argument('activo', type=inputs.boolean, location='args')

    @ns.expect(parser)
    @ns.marshal_with(usuariosPgModel)
    def get(self):
        args = self.parser.parse_args()
        query = db.session.query(Usuarios)

        if args['email'] != None:
            query = query.filter(Usuarios.telefono.ilike('%'+args['email'])+'%')
        if args['activo'] != None:
            query = query.filter(Usuarios.activo == args['activo'])

        return query.order_by(Usuarios.codUsuario).paginate(page=args['pagina'], per_page=args['porPagina'])