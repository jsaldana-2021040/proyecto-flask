from flask_restx import Api

api = Api(
    title='Core API',
    version='1.0',
    description='API',
    # authorizations=authorizations,
    # security='token',
    ordered=True
)

from .personas_resource import *