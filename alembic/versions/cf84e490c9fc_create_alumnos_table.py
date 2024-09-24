"""create alumnos table

Revision ID: cf84e490c9fc
Revises: 
Create Date: 2024-09-24 16:37:57.152795

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'cf84e490c9fc'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'alumno',
        sa.Column('padron', sa.Integer, primary_key=True),
        sa.Column('nombre', sa.Text, nullable=False),
        sa.Column('apellido', sa.Text, nullable=False),
        sa.Column('edad', sa.Integer),
    )

def downgrade() -> None:
    op.drop_table('alumno')
