"""empty message

Revision ID: fb4c1b933b7f
Revises: 711f4e827743
Create Date: 2019-08-23 01:41:04.286000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fb4c1b933b7f'
down_revision = '711f4e827743'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index(op.f('ix_hotel_id'), 'hotel', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_hotel_id'), table_name='hotel')
    # ### end Alembic commands ###
