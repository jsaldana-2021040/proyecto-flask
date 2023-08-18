from flask import Flask
from flask_restx import Resource, Api, fields, reqparse, inputs
from persona import Persona

data = [
    {'nombres': 'Pedro Andrés', 'apellidos': 'Vega Stalling', 'tieneVisa': False},
    {'nombres': 'José Roberto', 'apellidos': 'Saldaña Arrazola', 'tieneVisa': True},
    {'nombres': 'Selvin Fernando', 'apellidos': 'Ac Cucul', 'tieneVisa': False},
    {'nombres': 'Erick Daniel', 'apellidos': 'Poron Muñoz', 'tieneVisa': True},
    {'nombres': 'Erick Fernando', 'apellidos': 'Canto Boton', 'tieneVisa': False},
    {'nombres': 'Elisa María', 'apellidos': 'Jauregui', 'tieneVisa': True},
    {'nombres': 'Ana Beatruiz', 'apellidos': 'Obiols', 'tieneVisa': True},
    {'nombres': 'Jonathan', 'apellidos': 'Monroy', 'tieneVisa': False},
    {'nombres': 'Andres Eduardo', 'apellidos': 'Garcia Salazar', 'tieneVisa': True},
    {'nombres': 'Miguel Fernando', 'apellidos': 'Mendez MOnterroso', 'tieneVisa': True},
    {'nombres': 'Jose Miguel', 'apellidos': 'Martinez Hernandez', 'tieneVisa': False},
    {'nombres': 'Diego Rene', 'apellidos': 'Arriola Ruiz', 'tieneVisa': False},
    {'nombres': 'Pablo Andrez', 'apellidos': 'Mendez Sanchez', 'tieneVisa': True},
    {'nombres': 'Adriana Cristina', 'apellidos': 'Elizabeth Dias', 'tieneVisa': False},
    {'nombres': 'Luis Fernando', 'apellidos': 'Mendoza Alvarado', 'tieneVisa': True},
    {'nombres': 'Luis Francisco', 'apellidos': 'Perez Dias', 'tieneVisa': True},
    {'nombres': 'Diego Josue', 'apellidos': 'Monzon Armando', 'tieneVisa': False},
    {'nombres': 'Mario Roberto', 'apellidos': 'Martinez Sandobal', 'tieneVisa': True},
    {'nombres': 'Daniel Esteban', 'apellidos': 'Sanchez Martinez', 'tieneVisa': True},
    {'nombres': 'Jose Tulio', 'apellidos': 'Jimenez Matul', 'tieneVisa': True},

    {'nombres': 'Diego Josue', 'apellidos': 'Monzon Armando', 'tieneVisa': False},
    {'nombres': 'Mario Roberto', 'apellidos': 'Martinez Sandobal', 'tieneVisa': True},
    {'nombres': 'Daniel Esteban', 'apellidos': 'Sanchez Martinez', 'tieneVisa': True},
    {'nombres': 'Jose Tulio', 'apellidos': 'Jimenez Matul', 'tieneVisa': True},
]

listPersonas = [Persona(i+1, dtPersona['nombres'], dtPersona['apellidos'],
                        dtPersona['tieneVisa']) for i, dtPersona in enumerate(data)]


def find(id: int):
    output: Persona = None
    for persona in listPersonas:
        if persona.codigo == id:
            output = persona
    return output


app = Flask(__name__)
api = Api(app)

personaModel = api.model('PersonaModel', {
    'codigo': fields.Integer,
    'nombres': fields.String,
    'apellidos': fields.String,
    'tieneVisa': fields.Boolean
})


@api.route('/personas')
class PersonasResource(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('tieneVisa', type=inputs.boolean)

    @api.marshal_list_with(personaModel)
    def get(self):
        args = self.parser.parse_args()
        if args['tieneVisa'] != None:
            return [persona for persona in listPersonas if persona.tieneVisa == args['tieneVisa']]
        else:
            return listPersonas

    def post(self):
        return {'post': 'world'}


@api.route('/personas/<int:id>')
class PersonaResource(Resource):

    @api.marshal_with(personaModel)
    def get(self, id):
        return find(id)

    def put(self, id):
        persona = find(id)
        return persona


@api.route('/personas/pg')
class PersonaPgResource(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('pagina', type=int)
    parser.add_argument('porPagina', type=int)

    @api.marshal_list_with(personaModel)
    def get(self):
        args = self.parser.parse_args()
        output = []
        controlador = 0
        pagina: int = args['pagina']
        customPag: int = args['porPagina']
        for persona in listPersonas:
            if controlador in range((customPag * pagina) - customPag, customPag*pagina):
                output.append(persona)
            controlador+=1
        return output


if __name__ == '__main__':
    app.run(debug=True)
