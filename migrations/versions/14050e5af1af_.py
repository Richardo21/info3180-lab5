"""empty message

Revision ID: 14050e5af1af
Revises: 89ec9d388f0b
Create Date: 2019-03-10 13:26:36.737205

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '14050e5af1af'
down_revision = '89ec9d388f0b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_profiles', sa.Column('photo', sa.String(length=100), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user_profiles', 'photo')
    # ### end Alembic commands ###
