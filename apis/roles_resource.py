from flask_restx import Namespace, Resource, reqparse, inputs
from .models import rolModel, rolBodyRequestModel, rolPgModel
from flask_jwt_extended import get_jwt_identity, jwt_required
from database import db, Roles, Usuarios, RolesPermisos

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

        if 'permisos' in datos:
                for permiso in datos['permisos']:
                    nuevoRolesPermisos = RolesPermisos(permisosCod = permiso, usuarioCreador = Usuarios.getUserByIdentity(get_jwt_identity()).email)
                    roles.rolesPermisos.append(nuevoRolesPermisos)

        db.session.add(roles)
        db.session.commit()
        return roles
    
@ns.route('/<int:id>')
class RolesResource(Resource):

    @ns.marshal_with(rolModel)
    def get(self, id):
        return db.session.query(Roles).get(id)

    @ns.expect(rolBodyRequestModel, validate=True)
    @ns.marshal_with(rolModel)
    @jwt_required()
    def put(self, id):
        usr: Usuarios = Usuarios.getUserByIdentity(get_jwt_identity())

        query = db.session.query(RolesPermisos)

        existentes = query.order_by(RolesPermisos.codRolPermiso).filter(RolesPermisos.rolCod == id).all()
        
        datos = ns.payload
        roles =  db.session.query(Roles).get(id)
        roles.nombre = datos['nombre']
        roles.descripcion = datos['descripcion']
        roles.usuarioEditor = usr.email

        if 'permisos' in datos:
                
                for permisoBody in datos['permisos']:
                    existeEnBd = False

                    for existente in existentes:
                        if permisoBody == existente.permisosCod:
                            existeEnBd = True
                            
                    if not existeEnBd:
                        nuevoRolesPermisos = RolesPermisos(permisosCod = permisoBody, usuarioCreador = usr.email)
                        roles.rolesPermisos.append(nuevoRolesPermisos)

                for permiso in existentes :
                    if permiso.permisosCod not in datos['permisos']:
                        permiso.activo = False
                    else:
                        if permiso.permisosCod in datos['permisos']:
                            if permiso.activo == False:
                                permiso.activo = True

        db.session.commit()
        return roles

    @ns.marshal_with(rolModel)
    @jwt_required()
    def delete(self, id):

        roles = db.session.query(Roles).get(id)
        roles.activo = False
        db.session.commit()
        return roles
    
@ns.route('/pg')
class RolesPgResource(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('pagina', default=1, type=int)
    parser.add_argument('porPagina', default=10, type=int)
    parser.add_argument('nombre', type=str, location='args')
    parser.add_argument('activo', type=inputs.boolean, location='args')

    @ns.expect(parser)
    @ns.marshal_with(rolPgModel)
    def get(self):
        args = self.parser.parse_args()
        query = db.session.query(Roles)

        if args['activo'] != None:
            query = query.filter(Roles.activo == args['activo'])

        if args['nombre'] != None:
            query = query.filter(Roles.nombre.ilike('%'+args['nombre']+'%'))

        return query.order_by(Roles.codRol).paginate(page=args['pagina'], per_page=args['porPagina'])