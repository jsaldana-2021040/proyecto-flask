from flask_restx import fields
from . import api

# === modelos Persona ===
personaModel = api.model('PersonaModel', {
    'codPersona': fields.Integer,
    'nombres': fields.String,
    'apellidos': fields.String,
    'tieneVisa': fields.Boolean,
    'activo': fields.Boolean,
    'empresaCod': fields.Integer
})

personaBodyRequestModel = api.model('PersonaBodyRequestModel', {
    'nombres': fields.String(required=True),
    'apellidos': fields.String(required=True),
    'tieneVisa': fields.Boolean(required=False),
    'empresaCod': fields.Integer(required=True)
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

empresasPgModel = api.model('EmpresasPgModel', {
    'total': fields.Integer,
    'page': fields.Integer,
    'pages': fields.Integer,
    'items': fields.List(fields.Nested(empresaModel))
})