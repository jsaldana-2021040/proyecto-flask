from flask_restx import Namespace, Resource
from .models import rolModel, rolBodyRequestModel
from flask_jwt_extended import get_jwt_identity, jwt_required
from database import db, Roles, Usuarios

ns = Namespace('Roles')
    
@ns.route('')
class RolesResource(Resource):

    @ns.marshal_list_with(rolModel)
    def get(self):
        query = db.session.query(Roles)

        return query.order_by(Roles.codRol).all()
    
    @jwt_required()
    @ns.marshal_with(rolBodyRequestModel)
    def post(self):
        datos = ns.payload

        roles = Roles(nombre= datos['nombre'], descripcion= datos['descripcion'], usuarioCreador = Usuarios.getUserByIdentity(get_jwt_identity()).email)

        db.session.add(roles)
        db.session.commit()
        return roles