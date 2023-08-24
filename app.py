from flask import Flask
from apis import api
from database import db
from database import migration

app = Flask(__name__)
migration.init_app(app, db)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:d3v-database@10.20.20.6:5432/practicas'

db.init_app(app)
api.init_app(app)

if __name__ == '__main__':
    app.run(debug=True)