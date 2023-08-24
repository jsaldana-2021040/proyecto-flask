from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

migration = Migrate()
db = SQLAlchemy()

from .personas import *
from .empresas import *
from .direcciones import *