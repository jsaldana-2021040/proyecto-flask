"""largo contraseña

Revision ID: be8577ad4b7d
Revises: 7d92bc8829f8
Create Date: 2023-09-07 09:26:52.996610

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'be8577ad4b7d'
down_revision = '7d92bc8829f8'
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column('usuarios', 'password',
               existing_type=sa.VARCHAR(length=8),
               type_=sa.String(length=60),
               nullable=False)


def downgrade():
    op.alter_column('usuarios', 'password',
               existing_type=sa.String(length=60),
               type_=sa.VARCHAR(length=8),
               nullable=False)
