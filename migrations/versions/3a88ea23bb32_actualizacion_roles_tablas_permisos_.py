"""actualizacion roles,tablas permisos, modulos y rolesPermisos

Revision ID: 3a88ea23bb32
Revises: ad20add9a76f
Create Date: 2023-10-04 08:42:32.358285

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3a88ea23bb32'
down_revision = 'ad20add9a76f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('modulos',
    sa.Column('cod_modulo', sa.SmallInteger(), autoincrement=True, nullable=False),
    sa.Column('modulo', sa.String(length=50), nullable=False),
    sa.Column('descripcion', sa.String(length=50), nullable=False),
    sa.Column('activo', sa.Boolean(), nullable=True),
    sa.Column('usuario_creador', sa.String(length=50), nullable=False),
    sa.Column('usuario_editor', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('cod_modulo')
    )
    op.create_table('permisos',
    sa.Column('cod_permiso', sa.SmallInteger(), autoincrement=True, nullable=False),
    sa.Column('modulo', sa.String(length=50), nullable=False),
    sa.Column('descripcion', sa.String(length=50), nullable=False),
    sa.Column('activo', sa.Boolean(), nullable=True),
    sa.Column('usuario_creador', sa.String(length=50), nullable=False),
    sa.Column('usuario_editor', sa.String(length=50), nullable=True),
    sa.Column('modulo_cod', sa.SmallInteger(), nullable=False),
    sa.ForeignKeyConstraint(['modulo_cod'], ['modulos.cod_modulo'], ),
    sa.PrimaryKeyConstraint('cod_permiso')
    )
    op.create_table('roles_permisos',
    sa.Column('cod_rol_permiso', sa.SmallInteger(), autoincrement=True, nullable=False),
    sa.Column('rol_cod', sa.SmallInteger(), nullable=True),
    sa.Column('permisos_cod', sa.SmallInteger(), nullable=True),
    sa.Column('activo', sa.Boolean(), nullable=True),
    sa.Column('usuario_creador', sa.String(length=50), nullable=False),
    sa.Column('usuario_editor', sa.String(length=50), nullable=True),
    sa.ForeignKeyConstraint(['permisos_cod'], ['permisos.cod_permiso'], ),
    sa.ForeignKeyConstraint(['rol_cod'], ['roles.cod_rol'], ),
    sa.PrimaryKeyConstraint('cod_rol_permiso')
    )
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

    op.drop_table('roles_permisos')
    op.drop_table('permisos')
    op.drop_table('modulos')
    # ### end Alembic commands ###
