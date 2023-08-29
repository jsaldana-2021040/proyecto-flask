from flask import Flask
from apis import api
from database import db
from database import migration
from flask_jwt_extended import JWTManager
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
migration.init_app(app, db)
app.config["JWT_SECRET_KEY"] = "t0k3n_s3cr3t0"
jwt = JWTManager(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:123456@localhost/prueba'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:d3v-database@10.20.20.6:5432/practicas'

db.init_app(app)
api.init_app(app)

if __name__ == '__main__':
    app.run(debug=True)