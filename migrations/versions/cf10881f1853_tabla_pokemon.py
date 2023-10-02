"""tabla pokemon

Revision ID: cf10881f1853
Revises: 7b1f42fa85c5
Create Date: 2023-09-26 10:19:51.193057

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cf10881f1853'
down_revision = '7b1f42fa85c5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pokemons',
    sa.Column('cod_pokemon', sa.SmallInteger(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('url', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('cod_pokemon')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('pokemons')
    # ### end Alembic commands ###
