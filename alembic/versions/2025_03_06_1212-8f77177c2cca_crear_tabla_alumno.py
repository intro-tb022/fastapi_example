"""Crear tabla alumno

Revision ID: 8f77177c2cca
Revises: 
Create Date: 2025-03-06 12:12:12.052787

"""
from typing import Sequence, Union

from alembic import op
import sqlmodel as sq


# revision identifiers, used by Alembic.
revision: str = '8f77177c2cca'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
   op.create_table(
       'alumno',
       sq.Column('padron', sq.Integer, primary_key=True),
       sq.Column('nombre', sq.Text, nullable=False),
       sq.Column('apellido', sq.Text, nullable=False),
       sq.Column('edad', sq.Integer)
   )

def downgrade() -> None:
    op.drop_table('alumno')
