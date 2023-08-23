from flask_restx import fields
from . import api

personaModel = api.model('PersonaModel', {
    'codigo': fields.Integer,
    'nombres': fields.String,
    'apellidos': fields.String,
    'tieneVisa': fields.Boolean,
    'activo': fields.Boolean,
    'idEmpresa': fields.Integer
})

empresaModel = api.model('EmpresaModel', {
    'id': fields.Integer,
    'nombre': fields.String,
    'direccion': fields.String,
    'telefono': fields.String,
    'activo': fields.Boolean
})

PaginacionModel = api.model('PaginacionModel', {
    'totalElementos': fields.Integer,
    'elementos': fields.List(fields.Nested(personaModel)),
    'paginaActual': fields.Integer,
    'elementosPorPagina': fields.Integer,
    'totalPaginas': fields.Integer
})