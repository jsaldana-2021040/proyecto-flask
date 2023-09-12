from flask_restx import Namespace, Resource, fields, abort
from database import db, Usuarios
from flask import jsonify
from flask_jwt_extended import create_access_token
from flask_bcrypt import Bcrypt
import flask

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

        bcrypt = Bcrypt()

        usuario = db.session.query(Usuarios).filter(Usuarios.email == email).first()
        
        if usuario == None or not bcrypt.check_password_hash(usuario.password, password):
            return abort(401, 'Credenciales incorrectas')
        
        access_token = create_access_token(identity=email, additional_claims = {"rol": usuario.rol.tipo})
        
        return access_token
        
            