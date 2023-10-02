from database import db

class Pokemons(db.Model):
    __tablename__ = 'pokemons'

    codPokemon: int = db.Column('cod_pokemon', db.SmallInteger, nullable=False, primary_key=True, autoincrement=True)
    name: str = db.Column('name', db.String(50), nullable=False)
    url: str = db.Column('url',  db.String(100), nullable=False)