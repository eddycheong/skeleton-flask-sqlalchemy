"""Add user table

Revision ID: 025c38f68c1d
Revises: 
Create Date: 2019-07-21 01:00:09.403084

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '025c38f68c1d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('user',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(length=255), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )

def downgrade():
    op.drop_table('user')
