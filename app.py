from flask import Flask
from flask_restx import Resource, Api

app = Flask(__name__)
api = Api(app)

@api.route('/personas')
class PersonasResource(Resource):
    def get(self):
        return {'post': 'hello'}
    
    def post(self):
        return {'post' : 'world'}


@api.route('/personas/<int:id>')
class PersonaResource(Resource):
    def get(self, id):
        return{'get':'get por id='+str(id)}
    
    def put(self, id):
        return{'put':'put por id='+str(id)}


@api.route('/personas/pg')
class PersonaPgResource(Resource):
    def get(self):
        return {'get':'get de pag'}


if __name__ == '__main__':
    app.run(debug=True)