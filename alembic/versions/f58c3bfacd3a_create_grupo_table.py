"""create grupo_tp table

Revision ID: f58c3bfacd3a
Revises: cf84e490c9fc
Create Date: 2024-09-25 15:56:43.560938

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f58c3bfacd3a'
down_revision: Union[str, None] = 'cf84e490c9fc'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'grupo',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('nombre', sa.Text, nullable=False),
    )


def downgrade() -> None:
    op.drop_table('grupo')
