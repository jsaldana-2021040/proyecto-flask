from flask_restx import Api

api = Api(
    title='Core API',
    version='1.0',
    description='API',
    # authorizations=authorizations,
    # security='token',
    ordered=True
)

from .empresas_resource import ns as empresas
from .personas_resource import ns as personas
from .direcciones_resource import ns as direcciones

api.add_namespace(empresas, '/empresas')
api.add_namespace(personas, '/personas')
api.add_namespace(direcciones, '/direcciones')