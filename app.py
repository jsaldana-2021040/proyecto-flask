from flask import Flask
from flask_restx import Resource, Api, fields, reqparse, inputs
from persona import Persona

listPersonas = [
    Persona(1, 'Pedro Andrés', 'Vega Stalling', False),
    Persona(2, 'José Roberto', 'Saldaña Arrazola', True),
    Persona(3, 'Selvin Fernando', 'Ac Cucul', False),
    Persona(4, 'Erick Daniel', 'Poron Muñoz', True),
    Persona(5, 'Erick Fernando', 'Canto Boton', False),
    Persona(6, 'Elisa María', 'Jauregui', True),
    Persona(7, 'Ana Beatruiz', 'Obiols', True),
    Persona(8, 'Jonathan', 'Monroy', False),
]

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
        output=[]
        if args['tieneVisa']!=None:
            for i in listPersonas:
                if i.tieneVisa==args['tieneVisa']:
                    output.append(i)
        else:
            return listPersonas
        return output
    
    def post(self):
        return {'post' : 'world'}


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
    def get(self):
        return {'get':'get de pag'}


if __name__ == '__main__':
    app.run(debug=True)