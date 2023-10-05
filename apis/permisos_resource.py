from flask_restx import Namespace, Resource, reqparse, inputs, abort
from .models import permisosModel, permisosBodyRequestModel, permisosPgModel
from flask_jwt_extended import get_jwt_identity, jwt_required
from database import db, Permisos, Usuarios

ns = Namespace('Permisos')
    
@ns.route('')
class PermisosResource(Resource):

    @ns.marshal_list_with(permisosModel)
    def get(self):
        query = db.session.query(Permisos)

        return query.order_by(Permisos.codPermiso).all()
    
    @jwt_required()
    @ns.marshal_with(permisosBodyRequestModel)
    def post(self):
        datos = ns.payload

        permisos = Permisos(permiso= datos['permiso'], descripcion= datos['descripcion'], moduloCod=datos['moduloCod'], usuarioCreador = Usuarios.getUserByIdentity(get_jwt_identity()).email)

        db.session.add(permisos)
        db.session.commit()
        return permisos
    
@ns.route('/<int:id>')
class PermisosResource(Resource):

    @ns.marshal_with(permisosModel)
    def get(self, id):
        return db.session.query(Permisos).get(id)

    @ns.expect(permisosBodyRequestModel, validate=True)
    @ns.marshal_with(permisosModel)
    @jwt_required()
    def put(self, id):
        
        datos = ns.payload
        permisos =  db.session.query(Permisos).get(id)
        permisos.permiso = datos['permiso']
        permisos.descripcion = datos['descripcion']
        permisos.usuarioEditor = Usuarios.getUserByIdentity(get_jwt_identity()).email
        db.session.commit()
        return permisos

    @ns.marshal_with(permisosModel)
    @jwt_required()
    def delete(self, id):

        permisos =  db.session.query(Permisos).get(id)
        permisos.activo = False
        db.session.commit()
        return permisos
    
@ns.route('/pg')
class PermisosPgResource(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('pagina', default=1, type=int)
    parser.add_argument('porPagina', default=10, type=int)
    parser.add_argument('permiso', type=str, location='args')
    parser.add_argument('activo', type=inputs.boolean, location='args')

    @ns.expect(parser)
    @ns.marshal_with(permisosPgModel)
    def get(self):
        args = self.parser.parse_args()
        query = db.session.query(Permisos)

        if args['permiso'] != None:
            query = query.filter(Permisos.permiso.ilike('%'+args['permiso']+'%'))
        if args['activo'] != None:
            query = query.filter(Permisos.activo == args['activo'])

        return query.order_by(Permisos.codPermiso).paginate(page=args['pagina'], per_page=args['porPagina'])