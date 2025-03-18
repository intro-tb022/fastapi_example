"""Add foreign keys to grupo-alumno

Revision ID: d68057cd1c40
Revises: 9e6f41a4bd49
Create Date: 2025-03-17 23:05:27.593498

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "d68057cd1c40"
down_revision: Union[str, None] = "9e6f41a4bd49"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    with op.batch_alter_table("alumno") as batch_op:
        batch_op.add_column(sa.Column("grupo_id", sa.Integer))
        batch_op.create_foreign_key("fk_alumno_grupo", "grupo", ["grupo_id"], ["id"])


def downgrade() -> None:
    with op.batch_alter_table("alumno") as batch_op:
        batch_op.drop_constraint("fk_alumno_grupo", type_="foreignkey")
        batch_op.drop_column("grupo_id")
