from flask_restx import Resource, reqparse, inputs
from database import db, Empresas
from . import api
from .models import empresaModel, personasPgModel, empresasPgModel, empresaBodyRequestModel

@api.route('/empresas')
class EmpresasResource(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('nombre', type=str, location='args')
    parser.add_argument('telefono', type=str, location='args')
    parser.add_argument('direccion', type=str, location='args')
    parser.add_argument('activo', type=inputs.boolean, location='args')

    @api.expect(parser)
    @api.marshal_list_with(empresaModel)
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
        
        return query.order_by(Empresas.codEmpresa).all()

    @api.expect(empresaBodyRequestModel, validate=True)
    @api.marshal_with(empresaModel)
    def post(self):
            try:
                datos = api.payload
                empresa = Empresas(nombre = datos['nombre'], direccion = datos['direccion'], telefono = datos['telefono'])
                db.session.add(empresa)
                db.session.commit()
                return empresa
            except:
                db.session.rollback()


@api.route('/empresas/<int:id>')
class EmpresaResource(Resource):

    @api.marshal_with(empresaModel)
    def get(self, id):
        return db.session.query(Empresas).get(id)

    @api.expect(empresaBodyRequestModel, validate=True)
    @api.marshal_with(empresaModel)
    def put(self, id):
        datos = api.payload
        empresa =  db.session.query(Empresas).get(id)
        empresa.nombre = datos['nombre']
        empresa.direccion = datos['direccion']
        empresa.telefono = datos['telefono']
        db.session.commit()
        return empresa

    @api.marshal_with(empresaModel)
    def delete(self, id):
        empresa =  db.session.query(Empresas).get(id)
        empresa.activo = False
        db.session.commit()
        return empresa

@api.route('/empresas/pg')
class EmpresasPgResource(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('pagina', default=1, type=int)
    parser.add_argument('porPagina', default=10, type=int)
    parser.add_argument('nombre', type=str, location='args')
    parser.add_argument('telefono', type=str, location='args')
    parser.add_argument('direccion', type=str, location='args')
    parser.add_argument('activo', type=inputs.boolean, location='args')

    @api.expect(parser)
    @api.marshal_with(empresasPgModel)
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