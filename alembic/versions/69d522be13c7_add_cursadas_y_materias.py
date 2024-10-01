"""Add cursadas

Revision ID: 69d522be13c7
Revises: fa3e5ade7ea8
Create Date: 2024-09-25 20:50:18.407295

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '69d522be13c7'
down_revision: Union[str, None] = 'fa3e5ade7ea8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'materia',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('nombre', sa.Text, nullable=False),
    )
    op.create_table(
        'cursada',
        sa.Column('materia_id', sa.Integer, primary_key=True),
        sa.Column('alumno_padron', sa.Integer, primary_key=True),
        sa.ForeignKeyConstraint(
            ["materia_id"],
            ["materia.id"],
        ),
        sa.ForeignKeyConstraint(
            ["alumno_padron"],
            ["alumno.padron"],
        ),
    )

def downgrade() -> None:
    op.drop_table('cursada')
    op.drop_table('materia')
