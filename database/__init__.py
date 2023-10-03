from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

migration = Migrate()
db = SQLAlchemy()

from .personas import *
from .empresas import *
from .direcciones import *
from .usuarios import *
from .usuarios import *
from .pokemons import *
from .modulos import *
from .permisos import *
from .roles_permisos import *
from .roles import *