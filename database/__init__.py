from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

migration = Migrate()
db = SQLAlchemy()

from models.personas import *