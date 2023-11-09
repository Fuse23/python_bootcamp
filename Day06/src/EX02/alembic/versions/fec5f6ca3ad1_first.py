"""first

Revision ID: fec5f6ca3ad1
Revises: 
Create Date: 2023-11-09 20:05:39.085355

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'fec5f6ca3ad1'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('ships',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('alignment', sa.String(length=5), nullable=False),
    sa.Column('name', sa.String(length=30), nullable=False),
    sa.Column('ship_class', sa.String(length=30), nullable=False),
    sa.Column('length', sa.Float(), nullable=False),
    sa.Column('crew_size', sa.Integer(), nullable=False),
    sa.Column('armed', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('officers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=30), nullable=False),
    sa.Column('last_name', sa.String(length=30), nullable=False),
    sa.Column('rank', sa.String(length=30), nullable=False),
    sa.Column('ship_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['ship_id'], ['ships.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('officers')
    op.drop_table('ships')
    # ### end Alembic commands ###