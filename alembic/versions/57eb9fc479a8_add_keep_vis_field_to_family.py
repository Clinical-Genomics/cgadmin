"""add keep vis field to family

Revision ID: 57eb9fc479a8
Revises: c9e97d4c09c2
Create Date: 2017-05-09 15:33:40.534285

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '57eb9fc479a8'
down_revision = 'c9e97d4c09c2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('family', sa.Column('keep_vis', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('family', 'keep_vis')
    # ### end Alembic commands ###