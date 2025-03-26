"""Add table integrante

Revision ID: 0c3021269af5
Revises: d68057cd1c40
Create Date: 2025-03-26 17:42:54.987793

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "0c3021269af5"
down_revision: Union[str, None] = "d68057cd1c40"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "integrante",
        sa.Column("id", sa.Integer, primary_key=False),
        sa.Column("nota", sa.Integer),
        sa.Column("alumno_padron", sa.Integer, primary_key=True),
        sa.Column("grupo_id", sa.Integer, primary_key=True),
        sa.ForeignKeyConstraint(
            ["alumno_padron"],
            ["alumno.padron"],
        ),
        sa.ForeignKeyConstraint(
            ["grupo_id"],
            ["grupo.id"],
        ),
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table("integrante")
