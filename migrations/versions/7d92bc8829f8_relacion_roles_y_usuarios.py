"""relacion roles y usuarios

Revision ID: 7d92bc8829f8
Revises: de660508856d
Create Date: 2023-08-25 08:50:32.654449

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7d92bc8829f8'
down_revision = 'de660508856d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('usuarios', schema=None) as batch_op:
        batch_op.add_column(sa.Column('rol_cod', sa.SmallInteger(), nullable=False))
        batch_op.create_foreign_key(None, 'roles', ['rol_cod'], ['cod_rol'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('usuarios', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('rol_cod')

    # ### end Alembic commands ###
