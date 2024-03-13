"""employee

Revision ID: c
Revises: 817c53f68f27
Create Date: 2024-03-13 13:04:30.512989

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9cbf8339ff91'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() :
    op.create_table('Employees',
                    sa.Column('id',sa.Integer, primary_key=True, autoincrement=True),
                    sa.Column('name',sa.VARCHAR(50), index=True),
                    sa.Column('age',sa.Integer, index=True),
                    sa.Column('email',sa.String, unique=True, index=True),
                    sa.Column('salary',sa.Integer, index=True),
                    sa.Column('phone_number',sa.String, unique=True, index=True),
                    sa.Column('date',sa.DateTime, unique=True))


def downgrade():
    op.drop_table("Employees")
