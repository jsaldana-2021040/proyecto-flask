from flask_restx import Resource, reqparse, inputs, abort
from database import db, Personas
from . import api
from .models import personaModel, personasPgModel, personaBodyRequestModel
from paginacion import Paginacion

@api.route('/personas')
class PersonasResource(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('tieneVisa', type=inputs.boolean, location='args')
    parser.add_argument('activo', type=inputs.boolean, location='args')
    parser.add_argument('nombres', type=str, location='args')
    parser.add_argument('apellidos', type=str, location='args')

    @api.expect(parser)
    @api.marshal_list_with(personaModel)
    def get(self):
        args = self.parser.parse_args()
        query = db.session.query(Personas)
        
        if args['tieneVisa'] != None:
            query = query.filter(Personas.tieneVisa == args['tieneVisa'])
        if args['activo'] != None:
            query = query.filter(Personas.activo == args['activo'])
        if args['nombres'] != None:
            query = query.filter(Personas.nombres.ilike('%'+args['nombres']+'%'))
        if args['apellidos'] != None:
            query = query.filter(Personas.apellidos.ilike('%'+args['apellidos']+'%'))

        return query.order_by(Personas.codPersona).all()

    @api.expect(personaBodyRequestModel, validate=True)
    @api.marshal_with(personaModel)
    def post(self):
        try:
            datos = api.payload
            persona = Personas(
                nombres=datos['nombres'],
                apellidos=datos['apellidos'],
                tieneVisa=datos['tieneVisa'],
                empresaCod= datos['empresaCod'])
            db.session.add(persona)
            db.session.commit()
            return persona
        except:
            abort(500, 'Error al guardar a la persona')

@api.route('/personas/<int:id>')
class PersonaResource(Resource):

    @api.marshal_with(personaModel)
    def get(self, id):
        return db.session.query(Personas).get(id)

    @api.expect(personaBodyRequestModel, validate=True)
    @api.marshal_with(personaModel)
    def put(self, id):
        datos = api.payload
        persona =  db.session.query(Personas).get(id)
        persona.nombres = datos['nombres']
        persona.apellidos = datos['apellidos'] 
        persona.tieneVisa = datos['tieneVisa']
        db.session.commit()
        return persona

    @api.marshal_with(personaModel)
    def delete(self, id):
        persona =  db.session.query(Personas).get(id)
        persona.activo = False
        db.session.commit()
        return persona


@api.route('/personas/pg')
class PersonasPgResource(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('pagina', default=1, type=int)
    parser.add_argument('porPagina', default=10, type=int)
    parser.add_argument('tieneVisa', type=inputs.boolean, location='args')
    parser.add_argument('activo', type=inputs.boolean, location='args')
    parser.add_argument('nombres', type=str, location='args')
    parser.add_argument('apellidos', type=str, location='args')

    @api.expect(parser)
    @api.marshal_with(personasPgModel)
    def get(self):
        args = self.parser.parse_args()
        query = db.session.query(Personas)
        if args['tieneVisa'] != None:
            query = query.filter(Personas.tieneVisa == args['tieneVisa'])
        if args['activo'] != None:
            query = query.filter(Personas.activo == args['activo'])
        if args['nombres'] != None:
            query = query.filter(Personas.nombres.ilike('%'+args['nombres']+'%'))
        if args['apellidos'] != None:
            query = query.filter(Personas.apellidos.ilike('%'+args['apellidos']+'%'))

        return query.order_by(Personas.codPersona).paginate(page=args['pagina'], per_page=args['porPagina'])