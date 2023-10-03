"""tabla roles update

Revision ID: c3eeffa7029e
Revises: ad20add9a76f
Create Date: 2023-10-03 11:44:12.965867

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c3eeffa7029e'
down_revision = 'ad20add9a76f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('roles', schema=None) as batch_op:
        batch_op.alter_column('nombre',
               existing_type=sa.VARCHAR(length=50),
               nullable=False)
        batch_op.alter_column('descripcion',
               existing_type=sa.VARCHAR(length=50),
               nullable=False)
        batch_op.alter_column('usuario_creador',
               existing_type=sa.VARCHAR(length=50),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('roles', schema=None) as batch_op:
        batch_op.alter_column('usuario_creador',
               existing_type=sa.VARCHAR(length=50),
               nullable=True)
        batch_op.alter_column('descripcion',
               existing_type=sa.VARCHAR(length=50),
               nullable=True)
        batch_op.alter_column('nombre',
               existing_type=sa.VARCHAR(length=50),
               nullable=True)

    # ### end Alembic commands ###
