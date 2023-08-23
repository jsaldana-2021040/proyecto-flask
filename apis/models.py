from flask_restx import fields
from . import api

personaModel = api.model('PersonaModel', {
    'codPersona': fields.Integer,
    'nombres': fields.String,
    'apellidos': fields.String,
    'tieneVisa': fields.Boolean,
    'activo': fields.Boolean,
    'empresaCod': fields.Integer
})

empresaModel = api.model('EmpresaModel', {
    'codEmpresa': fields.Integer,
    'nombre': fields.String,
    'direccion': fields.String,
    'telefono': fields.String,
    'activo': fields.Boolean
})

# PaginacionModel = api.model('PaginacionModel', {
#     'totalElementos': fields.Integer,
#     'elementos': fields.List(fields.Nested(personaModel)),
#     'paginaActual': fields.Integer,
#     'elementosPorPagina': fields.Integer,
#     'totalPaginas': fields.Integer
# })

PaginacionModel = api.model('PaginacionModel', {
    'total': fields.Integer,
    'page': fields.Integer,
    'pages': fields.Integer,
    'items': fields.List(fields.Nested(personaModel))
})

# EmpresasPgModel = api.model('EmpresasPgModel', {
#     'totalElementos': fields.Integer,
#     'elementos': fields.List(fields.Nested(empresaModel)),
#     'paginaActual': fields.Integer,
#     'elementosPorPagina': fields.Integer,
#     'totalPaginas': fields.Integer
# })

EmpresasPgModel = api.model('EmpresasPgModel', {
    'total': fields.Integer,
    'page': fields.Integer,
    'pages': fields.Integer,
    'items': fields.List(fields.Nested(empresaModel))
})