from flask import Flask
from apis import api
from database import db
from database import migration

app = Flask(__name__)
migration.init_app(app, db)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:123456@localhost:5432/prueba'

db.init_app(app)
api.init_app(app)

if __name__ == '__main__':
    app.run(debug=True)