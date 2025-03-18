"""Add tabla grupo

Revision ID: 9e6f41a4bd49
Revises: 6bdbdd5dfda9
Create Date: 2025-03-17 23:05:12.483667

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "9e6f41a4bd49"
down_revision: Union[str, None] = "6bdbdd5dfda9"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "grupo",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("nombre", sa.Text, nullable=False),
    )


def downgrade() -> None:
    op.drop_table("grupo")
