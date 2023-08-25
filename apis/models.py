from flask_restx import fields
from . import api

# === modelo Login ===
loginModel = api.model('LoginModel', {
    "access_token": fields.String,
    "msg": fields.String
})

# === modelos Direcciones ===

usuarioModel = api.model('UsuarioModel', {
    'codUsuario' : fields.Integer,
    'email' : fields.String,
    'password' : fields.String,
    'activo' : fields.Boolean,
    'rolCod' : fields.Integer
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

# === modelos Persona ===
personaModel = api.model('PersonaModel', {
    'codPersona': fields.Integer,
    'nombres': fields.String,
    'apellidos': fields.String,
    'tieneVisa': fields.Boolean,
    'activo': fields.Boolean,
    'empresaCod': fields.Integer,
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