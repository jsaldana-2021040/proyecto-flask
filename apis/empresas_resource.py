from flask_restx import Resource, fields, reqparse, inputs
from database import db, Empresas
from . import api
from .models import empresaModel, PaginacionModel

@api.route('/empresas')
class EmpresasResource(Resource):

    @api.marshal_list_with(empresaModel)
    def get(self):
        empresaList = db.session.query(Empresas).all()
        print(empresaList)
        return empresaList

    @api.marshal_with(empresaModel)
    def post(self):
            datos = api.payload
            empresa = Empresas(nombre = datos['nombre'], direccion = datos['direccion'], telefono = datos['telefono'])
            db.session.add(empresa)
            db.session.commit()


@api.route('/empresas/<int:id>')
class EmpresasResource(Resource):

    @api.marshal_with(empresaModel)
    def get(self, id):
        return db.session.query(Empresas).get(id)

    @api.marshal_with(empresaModel)
    def put(self, id):
        datos = api.payload
        empresa =  db.session.query(Empresas).get(id)
        empresa.nombre = datos['nombre']
        empresa.direccion = datos['direccion']
        empresa.telefono = datos['telefono']
        db.session.commit()

    @api.marshal_with(empresaModel)
    def delete(self, id):
        empresa =  db.session.query(Empresas).get(id)
        empresa.activo = False
        db.session.commit()