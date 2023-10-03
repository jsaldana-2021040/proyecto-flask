from flask_restx import fields
from . import api

# === modelos Roles ===

rolModel = api.model('RolModel',{
    'codRol' : fields.Integer,
    'nombre' : fields.String,
    'descripcion' : fields.String,
    'activo' : fields.Boolean,
    'usuarioCreador' : fields.String,
    'usuarioEditor' : fields.String
})

rolBodyRequestModel = api.model('RolBodyRequestModel',{
    'nombre' : fields.String,
    'descripcion' : fields.String
})

# === modelos Direcciones ===

usuarioModel = api.model('UsuarioModel', {
    'codUsuario' : fields.Integer,
    'email' : fields.String,
    'activo' : fields.Boolean,
    'rolCod' : fields.Integer,
    'rol' : fields.Nested(rolModel)
})

usuarioBodyRequestModel = api.model('UsuarioBodyRequestModel', {
    'email' : fields.String(required=True),
    'password' : fields.String(required=True),
})

usuariosPgModel = api.model('UsuariosPgModel', {
    'total': fields.Integer,
    'page': fields.Integer,
    'pages': fields.Integer,
    'items': fields.List(fields.Nested(usuarioModel))
})

# === modelos Direcciones ===

direccionModel = api.model('direccionModel', {
    'codDireccion' : fields.Integer,
    'direccion' : fields.String,
    'zona' : fields.String,
    'activo' : fields.Boolean,
    'personaCod' : fields.Integer,
})

direccionBodyRequestModel = api.model('DireccionBodyRequestModel', {
    'direccion' : fields.String(required=True),
    'zona' : fields.String(required=True),
    'personaCod' : fields.Integer(required=True),
})

direccionesPersonaModel = api.model('DireccionesPersonaModel', {
    'direccion' : fields.String(required=True),
    'zona' : fields.String(required=True),
})

direccionesPgModel = api.model('DireccionesPgModel', {
    'total': fields.Integer,
    'page': fields.Integer,
    'pages': fields.Integer,
    'items': fields.List(fields.Nested(direccionModel))
})

# === modelos Empresa ===

empresaModel = api.model('EmpresaModel', {
    'codEmpresa': fields.Integer,
    'nombre': fields.String,
    'direccion': fields.String,
    'telefono': fields.String,
    'activo': fields.Boolean
})

empresaBodyRequestModel = api.model('EmpresaBodyRequestModel', {
    'nombre': fields.String(required=True),
    'direccion': fields.String(required=True),
    'telefono': fields.String(required=False),
})

empresasPgModel = api.model('EmpresasPgModel', {
    'total': fields.Integer,
    'page': fields.Integer,
    'pages': fields.Integer,
    'items': fields.List(fields.Nested(empresaModel))
})

# === modelos Persona ===

personaModel = api.model('PersonaModel', {
    'codPersona': fields.Integer,
    'nombres': fields.String,
    'apellidos': fields.String,
    'tieneVisa': fields.Boolean,
    'activo': fields.Boolean,
    'empresaCod': fields.Integer,
    'empresa': fields.Nested(empresaModel),
    'direcciones': fields.List(fields.Nested(direccionModel))
})

personaBodyRequestModel = api.model('PersonaBodyRequestModel', {
    'nombres': fields.String(required=True),
    'apellidos': fields.String(required=True),
    'tieneVisa': fields.Boolean(required=False),
    'empresaCod': fields.Integer(required=True),
    'direcciones': fields.List(fields.Nested(direccionesPersonaModel), required=False)
})

personasPgModel = api.model('PersonaPgModel', {
    'total': fields.Integer,
    'page': fields.Integer,
    'pages': fields.Integer,
    'items': fields.List(fields.Nested(personaModel))
})

# Pokemons

pokemonModel = api.model('PokemonModel',{
    'codPokemon' : fields.Integer,
    'name' : fields.String,
    'url' : fields.String
})

pokemonsPgModel = api.model('PokemonsPgModel',{
    'total': fields.Integer,
    'page': fields.Integer,
    'pages': fields.Integer,
    'items': fields.List(fields.Nested(pokemonModel))
})

# === modelos Roles ===

modulosModel = api.model('modulosModel',{
    'codModulo' : fields.Integer,
    'modulo' : fields.String,
    'descripcion' : fields.String,
    'activo' : fields.Boolean,
    'usuarioCreador' : fields.String,
    'usuarioEditor' : fields.String
})

modulosBodyRequestModel = api.model('modulosBodyRequestModel',{
    'modulo' : fields.String,
    'descripcion' : fields.String
})

ModulosPgModel = api.model('ModulosPgModel',{
    'total': fields.Integer,
    'page': fields.Integer,
    'pages': fields.Integer,
    'items': fields.List(fields.Nested(modulosModel))
})

# === modelos Permisos ===

permisosModel = api.model('PermisosModel',{
    'codPermiso' : fields.Integer,
    'permiso' : fields.String,
    'descripcion' : fields.String,
    'activo' : fields.Boolean,
    'usuarioCreador' : fields.String,
    'usuarioEditor' : fields.String,
    'moduloCod': fields.Integer
})

permisosBodyRequestModel = api.model('PermisosBodyRequestModel',{
    'permiso' : fields.String,
    'descripcion' : fields.String,
    'moduloCod': fields.Integer
})

permisosPgModel = api.model('PermisosPgModel',{
    'total': fields.Integer,
    'page': fields.Integer,
    'pages': fields.Integer,
    'items': fields.List(fields.Nested(permisosModel))
})

# === modelos Roles Permisos ===

rolesPermisosModel = api.model('rolesPermisosModel',{
    'codRolPermiso' : fields.Integer,
    'rolCod' : fields.Integer,
    'permisosCod' : fields.Integer,
    'activo' : fields.Boolean,
    'usuarioCreador' : fields.String,
    'usuarioEditor' : fields.String
})

rolesPermisosBodyRequestModel = api.model('rolesPermisosBodyRequestModel',{
    'rolCod' : fields.Integer,
    'permisosCod' : fields.Integer,
})

rolesPermisosPgModel = api.model('rolesPermisosPgModel',{
    'total': fields.Integer,
    'page': fields.Integer,
    'pages': fields.Integer,
    'items': fields.List(fields.Nested(rolesPermisosModel))
})