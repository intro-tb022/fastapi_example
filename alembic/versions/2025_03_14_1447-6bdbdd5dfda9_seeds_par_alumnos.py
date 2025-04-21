"""Seeds par alumnos

Revision ID: 6bdbdd5dfda9
Revises: 8f77177c2cca
Create Date: 2025-03-14 14:47:19.590205

"""

import csv
import os
import random
from typing import Sequence, Union

import sqlmodel as sq

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "6bdbdd5dfda9"
down_revision: Union[str, None] = "8f77177c2cca"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))


def upgrade() -> None:
    """Upgrade schema."""
    path = os.path.join(root, "resources", "alumnos.csv")
    alumnos = []
    with open(path) as f:
        csvFile = csv.DictReader(f, delimiter=";")
        for linea in csvFile:
            alumnos.append(
                {
                    "padron": int(linea["Padron"]),
                    "nombre": linea["Nombre"],
                    "apellido": linea["Apellido"],
                    "edad": random.randint(18, 35),
                }
            )

    alumnos_table = sq.table(
        "alumno",
        sq.Column("padron", sq.Integer, primary_key=True),
        sq.Column("nombre", sq.Text, nullable=False),
        sq.Column("apellido", sq.Text, nullable=False),
        sq.Column("edad", sq.Integer),
    )

    op.bulk_insert(alumnos_table, alumnos)


def downgrade() -> None:
    """Downgrade schema."""
    op.execute("DELETE FROM alumno")
