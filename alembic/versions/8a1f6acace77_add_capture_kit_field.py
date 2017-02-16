"""add capture kit field

Revision ID: 8a1f6acace77
Revises: 9ae66982d962
Create Date: 2017-02-16 10:16:34.077075

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8a1f6acace77'
down_revision = '9ae66982d962'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('sample', sa.Column('capture_kit', sa.Enum('Agilent Sureselect CRE', 'Agilent Sureselect V5', 'SureSelect Focused Exome', 'other'), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('sample', 'capture_kit')
    # ### end Alembic commands ###