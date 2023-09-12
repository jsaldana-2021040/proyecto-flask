from flask_restx import Namespace, Resource, reqparse, inputs, abort
from database import db, Empresas, Usuarios
from .models import empresaModel, empresasPgModel, empresaBodyRequestModel
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask import request

ns = Namespace('Empresas')

@ns.route('')
class EmpresasResource(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('nombre', type=str, location='args')
    parser.add_argument('telefono', type=str, location='args')
    parser.add_argument('direccion', type=str, location='args')
    parser.add_argument('activo', type=inputs.boolean, location='args')

    @ns.expect(parser)
    @ns.marshal_list_with(empresaModel)
    @jwt_required()
    def get(self):

        usuario = Usuarios.getUserByIdentity(get_jwt_identity())
        if usuario.rol.tipo != "ADMIN":
            abort(401, 'El usuario no tiene permisos suficientes')

        args = self.parser.parse_args()
        query = db.session.query(Empresas)

        if args['nombre'] != None:
            query = query.filter(Empresas.nombre.ilike('%'+args['nombre']+'%'))
        if args['telefono'] != None:
            query = query.filter(Empresas.telefono.ilike(args['telefono']))
        if args['direccion'] != None:
            query = query.filter(Empresas.direccion.ilike('%'+args['direccion']+'%'))
        if args['activo'] != None:
            query = query.filter(Empresas.activo == args['activo'])
        
        return query.order_by(Empresas.codEmpresa).all()

    @ns.expect(empresaBodyRequestModel, validate=True)
    @ns.marshal_with(empresaModel)
    @jwt_required()
    def post(self):
            
            usuario = Usuarios.getUserByIdentity(get_jwt_identity())
            if usuario.rol.tipo != "ADMIN":
                abort(401, 'El usuario no tiene permisos suficientes')
                
            try:
                datos = ns.payload
                empresa = Empresas(nombre = datos['nombre'], direccion = datos['direccion'], telefono = datos['telefono'])
                db.session.add(empresa)
                db.session.commit()
                return empresa
            except:
                db.session.rollback()
                abort(500, 'Error al guardar la empresa')


@ns.route('/<int:id>')
class EmpresaResource(Resource):

    @ns.marshal_with(empresaModel)
    def get(self, id):
        return db.session.query(Empresas).get(id)

    @ns.expect(empresaBodyRequestModel, validate=True)
    @ns.marshal_with(empresaModel)
    @jwt_required()
    def put(self, id):

        usuario = Usuarios.getUserByIdentity(get_jwt_identity())
        if usuario.rol.tipo != "ADMIN":
            abort(401, 'El usuario no tiene permisos suficientes')
        
        datos = ns.payload
        empresa =  db.session.query(Empresas).get(id)
        empresa.nombre = datos['nombre']
        empresa.direccion = datos['direccion']
        empresa.telefono = datos['telefono']
        db.session.commit()
        return empresa

    @ns.marshal_with(empresaModel)
    @jwt_required()
    def delete(self, id):

        usuario = Usuarios.getUserByIdentity(get_jwt_identity())
        if usuario.rol.tipo != "ADMIN":
            abort(401, 'El usuario no tiene permisos suficientes')

        empresa =  db.session.query(Empresas).get(id)
        empresa.activo = False
        db.session.commit()
        return empresa

@ns.route('/pg')
class EmpresasPgResource(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('pagina', default=1, type=int)
    parser.add_argument('porPagina', default=10, type=int)
    parser.add_argument('nombre', type=str, location='args')
    parser.add_argument('telefono', type=str, location='args')
    parser.add_argument('direccion', type=str, location='args')
    parser.add_argument('activo', type=inputs.boolean, location='args')

    @ns.expect(parser)
    @ns.marshal_with(empresasPgModel)
    def get(self):
        args = self.parser.parse_args()
        query = db.session.query(Empresas)

        if args['nombre'] != None:
            query = query.filter(Empresas.nombre.ilike('%'+args['nombre']+'%'))
        if args['telefono'] != None:
            query = query.filter(Empresas.telefono.ilike(args['telefono']))
        if args['direccion'] != None:
            query = query.filter(Empresas.direccion.ilike('%'+args['direccion']+'%'))
        if args['activo'] != None:
            query = query.filter(Empresas.activo == args['activo'])

        return query.order_by(Empresas.codEmpresa).paginate(page=args['pagina'], per_page=args['porPagina'])