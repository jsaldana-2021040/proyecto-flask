from flask_restx import Namespace, Resource, reqparse, inputs
from database import db, Usuarios, Roles
from .models import usuarioModel, usuarioBodyRequestModel, usuariosPgModel, loginModel
from sqlalchemy import and_
from flask import jsonify
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required

ns = Namespace('Usuarios')
lg = Namespace('Login')

@lg.route('')
class LoginResource(Resource):
    @lg.marshal_with(loginModel)
    def get(self):
        datos = ns.payload
        email = datos['email']
        password = datos['password']
        usuarios = db.session.query(Usuarios).filter(and_ (Usuarios.email == email, Usuarios.password == password)).first()

        if usuarios != None:
            if email == usuarios.email and password == usuarios.password:
                access_token = create_access_token(identity=email, additional_claims=usuarios.rolCod)
        else:
            return jsonify(msg="email o contraseña incorrectas").get_json(), 403
        
        return jsonify(access_token=access_token, msg="Succes").get_json(), 200
        
    
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

@ns.route('/ADMIN')
class UsuariosResource(Resource):

    @ns.expect(usuarioBodyRequestModel, validate=True)
    @ns.marshal_with(usuarioModel)
    @jwt_required()
    def post(self):
            current_user = get_jwt_identity()
            print('autorizado')
            try:
                datos = ns.payload
                roles = db.session.query(Roles).filter(Roles.tipo == "ADMIN").first()
                print(roles)
                usuario = Usuarios(email = datos['email'], password = datos['password'], rolCod = roles.codRol)
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
    def put(self, id):
        datos = ns.payload
        usuario =  db.session.query(Usuarios).get(id)
        usuario.email = datos['email']
        usuario.password = datos['password']
        db.session.commit()
        return usuario

    @ns.marshal_with(usuarioModel)
    def delete(self, id):
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