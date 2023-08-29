from flask_restx import Namespace, Resource, fields, abort
from database import db, Usuarios
from flask import jsonify
from flask_jwt_extended import create_access_token

lg = Namespace('Login')

@lg.route('')
class LoginResource(Resource):

    loginBodyRequest = lg.model('LoginBodyRequest', {
        'email': fields.String(required=True),
        'password': fields.String(required=True),
    })

    @lg.expect(loginBodyRequest)
    def post(self):
        datos = lg.payload
        email = datos['email']
        password = datos['password']

        usuario = db.session.query(Usuarios).filter(Usuarios.email == email).first()
        
        if usuario == None:
            return abort(403, 'email incorrecto')
        if usuario.password != password:
            abort(403, 'contraseña incorrecta')
        return create_access_token(identity=email)
            