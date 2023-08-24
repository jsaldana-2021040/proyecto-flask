from flask_restx import Namespace, Resource, reqparse, inputs, abort
from database import db, Personas
from .models import personaModel, personasPgModel, personaBodyRequestModel

ns = Namespace('Personas')

@ns.route('')
class PersonasResource(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('tieneVisa', type=inputs.boolean, location='args')
    parser.add_argument('activo', type=inputs.boolean, location='args')
    parser.add_argument('nombres', type=str, location='args')
    parser.add_argument('apellidos', type=str, location='args')

    @ns.expect(parser)
    @ns.marshal_list_with(personaModel)
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

    @ns.expect(personaBodyRequestModel, validate=True)
    @ns.marshal_with(personaModel)
    def post(self):
        try:
            datos = ns.payload
            persona = Personas(
                nombres=datos['nombres'],
                apellidos=datos['apellidos'],
                tieneVisa=datos['tieneVisa'],
                empresaCod= datos['empresaCod'])
            
            for direccion in datos['direcciones']:
                print(direccion['direccion'])
            db.session.add(persona)
            db.session.commit()
            return persona
        except:
            abort(500, 'Error al guardar a la persona')

@ns.route('/<int:id>')
class PersonaResource(Resource):

    @ns.marshal_with(personaModel)
    def get(self, id):
        return db.session.query(Personas).get(id)

    @ns.expect(personaBodyRequestModel, validate=True)
    @ns.marshal_with(personaModel)
    def put(self, id):
        datos = ns.payload
        persona =  db.session.query(Personas).get(id)
        persona.nombres = datos['nombres']
        persona.apellidos = datos['apellidos'] 
        persona.tieneVisa = datos['tieneVisa']
        db.session.commit()
        return persona

    @ns.marshal_with(personaModel)
    def delete(self, id):
        persona =  db.session.query(Personas).get(id)
        persona.activo = False
        db.session.commit()
        return persona


@ns.route('/pg')
class PersonasPgResource(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('pagina', default=1, type=int)
    parser.add_argument('porPagina', default=10, type=int)
    parser.add_argument('tieneVisa', type=inputs.boolean, location='args')
    parser.add_argument('activo', type=inputs.boolean, location='args')
    parser.add_argument('nombres', type=str, location='args')
    parser.add_argument('apellidos', type=str, location='args')

    @ns.expect(parser)
    @ns.marshal_with(personasPgModel)
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