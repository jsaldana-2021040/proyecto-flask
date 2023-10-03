from flask_restx import Namespace, Resource, reqparse, inputs, abort
from .models import modulosModel, modulosBodyRequestModel, ModulosPgModel
from flask_jwt_extended import get_jwt_identity, jwt_required
from database import db, Modulos, Usuarios

ns = Namespace('Modulos')
    
@ns.route('')
class ModulosResource(Resource):

    @ns.marshal_list_with(modulosModel)
    def get(self):
        query = db.session.query(Modulos)

        return query.order_by(Modulos.codModulo).all()
    
    @jwt_required()
    @ns.marshal_with(modulosBodyRequestModel)
    def post(self):
        datos = ns.payload

        modulos = Modulos(modulo= datos['modulo'], descripcion= datos['descripcion'], usuarioCreador = Usuarios.getUserByIdentity(get_jwt_identity()).email)

        db.session.add(modulos)
        db.session.commit()
        return modulos
    
@ns.route('/<int:id>')
class ModulosResource(Resource):

    @ns.marshal_with(modulosModel)
    def get(self, id):
        return db.session.query(Modulos).get(id)

    @ns.expect(modulosBodyRequestModel, validate=True)
    @ns.marshal_with(modulosModel)
    @jwt_required()
    def put(self, id):
        
        datos = ns.payload
        modulo =  db.session.query(Modulos).get(id)
        modulo.modulo = datos['modulo']
        modulo.descripcion = datos['descripcion']
        modulo.usuarioEditor = Usuarios.getUserByIdentity(get_jwt_identity()).email
        db.session.commit()
        return modulo

    @ns.marshal_with(modulosModel)
    @jwt_required()
    def delete(self, id):

        modulo =  db.session.query(Modulos).get(id)
        modulo.activo = False
        db.session.commit()
        return modulo
    
@ns.route('/pg')
class ModulosPgResource(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('pagina', default=1, type=int)
    parser.add_argument('porPagina', default=10, type=int)
    parser.add_argument('modulo', type=str, location='args')
    parser.add_argument('descripcion', type=str, location='args')
    parser.add_argument('activo', type=inputs.boolean, location='args')

    @ns.expect(parser)
    @ns.marshal_with(ModulosPgModel)
    def get(self):
        args = self.parser.parse_args()
        query = db.session.query(Modulos)

        if args['modulo'] != None:
            query = query.filter(Modulos.modulo.ilike('%'+args['modulo']+'%'))
        if args['descripcion'] != None:
            query = query.filter(Modulos.descripcion.ilike('%'+args['descripcion']+'%'))
        if args['activo'] != None:
            query = query.filter(Modulos.activo == args['activo'])

        return query.order_by(Modulos.codModulo).paginate(page=args['pagina'], per_page=args['porPagina'])