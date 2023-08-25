from flask import Flask
from apis import api
from database import db
from database import migration
from flask_jwt_extended import JWTManager

app = Flask(__name__)
migration.init_app(app, db)
app.config["JWT_SECRET_KEY"] = "t0k3n_s3cr3t0"
jwt = JWTManager(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:123456@localhost/prueba'

db.init_app(app)
api.init_app(app)

if __name__ == '__main__':
    app.run(debug=True)