"""Renaming column birthday to born

Revision ID: ee72694d24e9
Revises: 791279dd0760
Create Date: 2023-03-04 22:34:23.535758

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ee72694d24e9'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column("students", "age", new_column_name="born")


def downgrade() -> None:
    pass
