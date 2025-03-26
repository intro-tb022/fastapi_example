"""Add relation n:m alumno grupo via integrante

Revision ID: d920ddf9d887
Revises: 0c3021269af5
Create Date: 2025-03-26 17:47:47.573197

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "d920ddf9d887"
down_revision: Union[str, None] = "0c3021269af5"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    with op.batch_alter_table("alumno") as batch_op:
        batch_op.drop_constraint("fk_alumno_grupo", type_="foreignkey")
        batch_op.drop_column("grupo_id")


def downgrade() -> None:
    """Downgrade schema."""
    with op.batch_alter_table("alumno") as batch_op:
        batch_op.add_column(sa.Column("grupo_id", sa.Integer))
        batch_op.create_foreign_key("fk_alumno_grupo", "grupo", ["grupo_id"], ["id"])
