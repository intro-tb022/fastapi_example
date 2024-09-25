"""Add foreign key to alumno


Revision ID: fa3e5ade7ea8
Revises: f58c3bfacd3a
Create Date: 2024-09-25 17:32:35.385499

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'fa3e5ade7ea8'
down_revision: Union[str, None] = 'f58c3bfacd3a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade() -> None:
    with op.batch_alter_table('alumno') as batch_op:
        batch_op.add_column(sa.Column('grupo_id', sa.Integer))
        batch_op.create_foreign_key('fk_alumno_grupo', 'grupo', ['grupo_id'], ['id'])

def downgrade() -> None:
    with op.batch_alter_table('alumno') as batch_op:
        batch_op.drop_constraint(
            'fk_alumno_grupo', type_='foreignkey')
        batch_op.drop_column(
            'grupo_id'
        )
