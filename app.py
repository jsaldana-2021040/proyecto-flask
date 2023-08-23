from flask import Flask
from flask_restx import Resource, Api, fields, reqparse, inputs
from persona import Persona
from paginacion import Paginacion
from models import Personas, Empresas
from database import db
from database import migration
from sqlalchemy.exc import IntegrityError

data = [
    {'nombres': 'Pedro Andrés', 'apellidos': 'Vega Stalling', 'tieneVisa': True, 'activo': True},
    {'nombres': 'José Roberto', 'apellidos': 'Saldaña Arrazola', 'tieneVisa': True, 'activo': False},
    {'nombres': 'Selvin Fernando', 'apellidos': 'Ac Cucul', 'tieneVisa': False, 'activo': True},
    {'nombres': 'Erick Daniel', 'apellidos': 'Poron Muñoz', 'tieneVisa': True, 'activo': True},
    {'nombres': 'Erick Fernando', 'apellidos': 'Canto Boton', 'tieneVisa': False, 'activo': False},
    {'nombres': 'Elisa María', 'apellidos': 'Jauregui', 'tieneVisa': True, 'activo': False},
    {'nombres': 'Ana Beatruiz', 'apellidos': 'Obiols', 'tieneVisa': True, 'activo': True},
    {'nombres': 'Jonathan', 'apellidos': 'Monroy', 'tieneVisa': False, 'activo': True},
    {'nombres': 'Andres Eduardo', 'apellidos': 'Garcia Salazar', 'tieneVisa': True, 'activo': True},
    {'nombres': 'Miguel Fernando', 'apellidos': 'Mendez MOnterroso', 'tieneVisa': True, 'activo': True},
    {'nombres': 'Jose Miguel', 'apellidos': 'Martinez Hernandez', 'tieneVisa': False, 'activo': False},
    {'nombres': 'Diego Rene', 'apellidos': 'Arriola Ruiz', 'tieneVisa': False, 'activo': True},
    {'nombres': 'Pablo Andrez', 'apellidos': 'Mendez Sanchez', 'tieneVisa': True, 'activo': True},
    {'nombres': 'Adriana Cristina', 'apellidos': 'Elizabeth Dias', 'tieneVisa': False, 'activo': True},
    {'nombres': 'Luis Fernando', 'apellidos': 'Mendoza Alvarado', 'tieneVisa': True, 'activo': False},
    {'nombres': 'Luis Francisco', 'apellidos': 'Perez Dias', 'tieneVisa': True, 'activo': True},
    {'nombres': 'Diego Josue', 'apellidos': 'Monzon Armando', 'tieneVisa': False, 'activo': True},
    {'nombres': 'Mario Roberto', 'apellidos': 'Martinez Sandobal', 'tieneVisa': True, 'activo': False},
    {'nombres': 'Daniel Esteban', 'apellidos': 'Sanchez Martinez', 'tieneVisa': True, 'activo': True},
    {'nombres': 'Jose Tulio', 'apellidos': 'Jimenez Matul', 'tieneVisa': True, 'activo': True},
    {'nombres': 'Diego Josue', 'apellidos': 'Monzon Armando', 'tieneVisa': False, 'activo': True},
    {'nombres': 'Mario Roberto', 'apellidos': 'Martinez Sandobal', 'tieneVisa': True, 'activo': False},
    {'nombres': 'Daniel Esteban', 'apellidos': 'Sanchez Martinez', 'tieneVisa': True, 'activo': True},
]

listPersonas = [Persona(i+1, dtPersona['nombres'], dtPersona['apellidos'],
                        dtPersona['tieneVisa'], dtPersona['activo']) for i, dtPersona in enumerate(data)]


def find(id: int):
    return next((persona for persona in listPersonas if persona.codigo == id), None)

app = Flask(__name__)
migration.init_app(app, db)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:123456@localhost:5432/prueba'


api = Api(app)
db.init_app(app)
personaModel = api.model('PersonaModel', {
    'codigo': fields.Integer,
    'nombres': fields.String,
    'apellidos': fields.String,
    'tieneVisa': fields.Boolean,
    'activo': fields.Boolean,
    'id_empresa': fields.Integer
})

empresaModel = api.model('EmpresaModel', {
    'id': fields.Integer,
    'nombre': fields.String,
    'direccion': fields.String,
    'telefono': fields.String,
    'activo': fields.Boolean
})

PaginacionModel = api.model('PaginacionModel', {
    'totalElementos': fields.Integer,
    'elementos': fields.List(fields.Nested(personaModel)),
    'paginaActual': fields.Integer,
    'elementosPorPagina': fields.Integer,
    'totalPaginas': fields.Integer
})


@api.route('/personas')
class PersonasResource(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('tieneVisa', type=inputs.boolean, location='args')
    parser.add_argument('activo', type=inputs.boolean, location='args')
    parser.add_argument('nombres', type=str, location='args')
    parser.add_argument('apellidos', type=str, location='args')

    @api.marshal_list_with(personaModel)
    def get(self):
        personasList = db.session.query(Personas).all()
        print(personasList)
        return personasList

    @api.marshal_with(personaModel)
    def post(self):
        try:
            datos = api.payload
            persona = Personas(nombres= datos['nombres'], apellidos=datos['apellidos'],
                           tieneVisa=datos['tieneVisa'], id_empresa= datos['id_empresa'])
            db.session.add(persona)
            db.session.commit()
        except IntegrityError:
            db.session.rollback()


@api.route('/personas/<int:id>')
class PersonaResource(Resource):

    @api.marshal_with(personaModel)
    def get(self, id):
        return find(id)

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
        args = self.parser.parse_args()
        output: list[Persona] = listPersonas
        
        if args['tieneVisa'] != None:
            output = [persona for persona in output if persona.tieneVisa == args['tieneVisa']]
        if args['activo'] != None:
            output = [persona for persona in output if persona.activo == args['activo']]
        if args['nombres'] != None:
            output = [persona for persona in output if args['nombres'].upper() in persona.nombres.upper()]
        if args['apellidos'] != None:
            output = [persona for persona in output if args['apellidos'].upper() in persona.apellidos.upper()]

        indexFinal: int = args['porPagina'] * args['pagina']
        return Paginacion(len(output), output[indexFinal - args['porPagina']: indexFinal], args['pagina'], args['porPagina'])
        # return listPersonas[indexFinal - args['porPagina']: indexFinal]


@api.route('/empresas')
class EmpresasResource(Resource):

    @api.marshal_list_with(empresaModel)
    def get(self):
        empresaList = db.session.query(Empresas).all()
        print(empresaList)
        return empresaList

    @api.marshal_with(empresaModel)
    def post(self):
            datos = api.payload
            empresa = Empresas(nombre = datos['nombre'], direccion = datos['direccion'], telefono = datos['telefono'])
            db.session.add(empresa)
            db.session.commit()


@api.route('/empresas/<int:id>')
class EmpresasResource(Resource):

    @api.marshal_with(empresaModel)
    def get(self, id):
        return db.session.query(Empresas).get(id)

    @api.marshal_with(empresaModel)
    def put(self, id):
        datos = api.payload
        empresa =  db.session.query(Empresas).get(id)
        empresa.nombre = datos['nombre']
        empresa.direccion = datos['direccion']
        empresa.telefono = datos['telefono']
        db.session.commit()

    @api.marshal_with(empresaModel)
    def delete(self, id):
        empresa =  db.session.query(Empresas).get(id)
        empresa.activo = False
        db.session.commit()


if __name__ == '__main__':
    app.run(debug=True)
