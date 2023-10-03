from flask_restx import Namespace, Resource, reqparse, inputs
from .models import rolesPermisosModel, rolesPermisosBodyRequestModel, rolesPermisosPgModel
from flask_jwt_extended import get_jwt_identity, jwt_required
from database import db, RolesPermisos, Usuarios

ns = Namespace('RolesPermisos')
    
@ns.route('')
class RolesPermisosResource(Resource):

    @ns.marshal_list_with(rolesPermisosModel)
    def get(self):
        query = db.session.query(RolesPermisos)

        return query.order_by(RolesPermisos.codRolPermiso).all()
    
    @jwt_required()
    @ns.marshal_with(rolesPermisosBodyRequestModel)
    def post(self):
        datos = ns.payload

        rolesPermisos = RolesPermisos(rolCod= datos['rolCod'], permisosCod= datos['permisosCod'], usuarioCreador = Usuarios.getUserByIdentity(get_jwt_identity()).email)

        db.session.add(rolesPermisos)
        db.session.commit()
        return rolesPermisos
    
@ns.route('/<int:id>')
class RolesPermisosResource(Resource):

    @ns.marshal_with(rolesPermisosModel)
    def get(self, id):
        return db.session.query(RolesPermisos).get(id)

    @ns.expect(rolesPermisosBodyRequestModel, validate=True)
    @ns.marshal_with(rolesPermisosModel)
    @jwt_required()
    def put(self, id):
        
        datos = ns.payload
        rolesPermisos =  db.session.query(RolesPermisos).get(id)
        rolesPermisos.rolCod = datos['rolCod']
        rolesPermisos.permisosCod = datos['permisosCod']
        rolesPermisos.usuarioEditor = Usuarios.getUserByIdentity(get_jwt_identity()).email
        db.session.commit()
        return rolesPermisos

    @ns.marshal_with(rolesPermisosModel)
    @jwt_required()
    def delete(self, id):

        rolesPermisos = db.session.query(RolesPermisos).get(id)
        rolesPermisos.activo = False
        db.session.commit()
        return rolesPermisos
    
@ns.route('/pg')
class RolesPermisosPgResource(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('pagina', default=1, type=int)
    parser.add_argument('porPagina', default=10, type=int)
    parser.add_argument('activo', type=inputs.boolean, location='args')

    @ns.expect(parser)
    @ns.marshal_with(rolesPermisosPgModel)
    def get(self):
        args = self.parser.parse_args()
        query = db.session.query(RolesPermisos)

        if args['activo'] != None:
            query = query.filter(RolesPermisos.activo == args['activo'])

        return query.order_by(RolesPermisos.codRolPermiso).paginate(page=args['pagina'], per_page=args['porPagina'])