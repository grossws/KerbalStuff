"""Add password reset to schema

Revision ID: f9897e968a
Revises: 59c74736a7f
Create Date: 2014-06-28 10:45:25.221305

"""

# revision identifiers, used by Alembic.
revision = 'f9897e968a'
down_revision = '59c74736a7f'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('passwordReset', sa.String(length=128), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'passwordReset')
    ### end Alembic commands ###
