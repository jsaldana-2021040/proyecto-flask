from flask_restx import Namespace, Resource, reqparse, inputs
from database import db, Direcciones
from .models import direccionModel, direccionBodyRequestModel, direccionesPgModel

ns = Namespace('Direcciones')

@ns.route('')
class DireccionesResource(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('zona', type=str, location='args')
    parser.add_argument('direccion', type=str, location='args')
    parser.add_argument('activo', type=inputs.boolean, location='args')

    @ns.expect(parser)
    @ns.marshal_list_with(direccionModel)
    def get(self):
        args = self.parser.parse_args()
        query = db.session.query(Direcciones)

        if args['zona'] != None:
            query = query.filter(Direcciones.zona.ilike('%'+args['zona']+'%'))
        if args['direccion'] != None:
            query = query.filter(Direcciones.direccion.ilike('%'+args['direccion']+'%'))
        if args['activo'] != None:
            query = query.filter(Direcciones.activo == args['activo'])
        
        return query.order_by(Direcciones.codDireccion).all()

    @ns.expect(direccionBodyRequestModel, validate=True)
    @ns.marshal_with(direccionModel)
    def post(self):
            try:
                datos = ns.payload
                direccion = Direcciones(zona = datos['zona'], direccion = datos['direccion'], personaCod = datos['personaCod'])
                db.session.add(direccion)
                db.session.commit()
                return direccion
            except:
                db.session.rollback()


@ns.route('/<int:id>')
class DireccionResource(Resource):

    @ns.marshal_with(direccionModel)
    def get(self, id):
        return db.session.query(Direcciones).get(id)

    @ns.expect(direccionBodyRequestModel, validate=True)
    @ns.marshal_with(direccionModel)
    def put(self, id):
        datos = ns.payload
        direccion =  db.session.query(Direcciones).get(id)
        direccion.zona = datos['zona']
        direccion.direccion = datos['direccion']
        db.session.commit()
        return direccion

    @ns.marshal_with(direccionModel)
    def delete(self, id):
        direccion =  db.session.query(Direcciones).get(id)
        direccion.activo = False
        db.session.commit()
        return direccion

@ns.route('/pg')
class DireccionesPgResource(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('pagina', default=1, type=int)
    parser.add_argument('porPagina', default=10, type=int)
    parser.add_argument('zona', type=str, location='args')
    parser.add_argument('direccion', type=str, location='args')
    parser.add_argument('activo', type=inputs.boolean, location='args')

    @ns.expect(parser)
    @ns.marshal_with(direccionesPgModel)
    def get(self):
        args = self.parser.parse_args()
        query = db.session.query(Direcciones)

        if args['zona'] != None:
            query = query.filter(Direcciones.telefono.ilike('%'+args['zona'])+'%')
        if args['direccion'] != None:
            query = query.filter(Direcciones.direccion.ilike('%'+args['direccion']+'%'))
        if args['activo'] != None:
            query = query.filter(Direcciones.activo == args['activo'])

        return query.order_by(Direcciones.codDireccion).paginate(page=args['pagina'], per_page=args['porPagina'])