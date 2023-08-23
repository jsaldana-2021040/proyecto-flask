from flask_restx import Resource, reqparse, inputs
from database import db, Personas
from . import api
from .models import personaModel, PaginacionModel

@api.route('/personas')
class PersonasResource(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('tieneVisa', type=inputs.boolean, location='args')
    parser.add_argument('activo', type=inputs.boolean, location='args')
    parser.add_argument('nombres', type=str, location='args')
    parser.add_argument('apellidos', type=str, location='args')

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

        return query.all()

    @api.marshal_with(personaModel)
    def post(self):
        try:
            datos = api.payload
            persona = Personas(
                nombres=datos['nombres'],
                apellidos=datos['apellidos'],
                tieneVisa=datos['tieneVisa'],
                id_empresa= datos['id_empresa'])
            db.session.add(persona)
            db.session.commit()
        except:
            db.session.rollback()

@api.route('/personas/<int:id>')
class PersonaResource(Resource):

    @api.marshal_with(personaModel)
    def get(self, id):
        pass

    @api.marshal_with(personaModel)
    def put(self, id):
        datos = api.payload
        persona =  db.session.query(Personas).get(id)
        persona.nombres = datos['nombres']
        persona.apellidos = datos['apellidos'] 
        persona.tieneVisa = datos['tieneVisa']
        db.session.commit()

    @api.marshal_with(personaModel)
    def delete(self, id):
        persona =  db.session.query(Personas).get(id)
        persona.activo = False
        db.session.commit()


@api.route('/personas/pg')
class PersonaPgResource(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('pagina', default=1, type=int)
    parser.add_argument('porPagina', default=10, type=int)
    parser.add_argument('tieneVisa', type=inputs.boolean, location='args')
    parser.add_argument('activo', type=inputs.boolean, location='args')
    parser.add_argument('nombres', type=str, location='args')
    parser.add_argument('apellidos', type=str, location='args')

    @api.marshal_list_with(PaginacionModel)
    def get(self):
        pass