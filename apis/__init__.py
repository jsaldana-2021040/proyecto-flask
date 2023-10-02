from flask_restx import Api

authorizations = {
    'apikey': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization'
    }
}

api = Api(
    title='Core API',
    version='1.0',
    description='API',
    authorizations=authorizations,
    ordered=True
)

from .empresas_resource import ns as empresas
from .personas_resource import ns as personas
from .direcciones_resource import ns as direcciones
from .usuarios_resource import ns as usuarios
from .login_resource import lg as login
from .pokemons_resource import ns as pokemons

api.add_namespace(empresas, '/empresas')
api.add_namespace(personas, '/personas')
api.add_namespace(direcciones, '/direcciones')
api.add_namespace(usuarios, '/usuarios')
api.add_namespace(login, '/login')
api.add_namespace(pokemons, '/pokemons')