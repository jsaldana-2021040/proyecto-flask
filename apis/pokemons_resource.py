from flask_restx import Namespace, Resource, reqparse, inputs, abort
from database import db, Pokemons
from .models import pokemonsPgModel, pokemonModel
import requests

ns = Namespace('Pokemons')

@ns.route('/pg')
class PokemonsPgResource(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('pagina', default=1, type=int)
    parser.add_argument('porPagina', default=10, type=int)
    parser.add_argument('nombre', type=str, location='args')

    @ns.expect(parser)
    @ns.marshal_with(pokemonsPgModel)
    def get(self):
        args = self.parser.parse_args()
        query = db.session.query(Pokemons)

        if args['nombre'] != None:
            query = query.filter(Pokemons.name.ilike('%'+args['nombre']+'%'))

        return query.order_by(Pokemons.codPokemon).paginate(page=args['pagina'], per_page=args['porPagina'])
    
@ns.route('/sync')
class PokemonsSyncResource(Resource):
    @ns.marshal_with(pokemonModel)
    def post(self):
            try:
                r = requests.get('https://pokeapi.co/api/v2/pokemon?limit=10000')

                data = r.json()['results']

                for jsPoke in data :
                    existe = db.session.query(Pokemons).filter(Pokemons.name == jsPoke['name']).first()

                    if existe == None:
                        pokemon = Pokemons(name= jsPoke['name'], url= jsPoke['url'])
                        db.session.add(pokemon)
                    
                db.session.commit()

            except:
                db.session.rollback()
                abort(500)