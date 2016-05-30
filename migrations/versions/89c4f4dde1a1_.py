"""empty message

Revision ID: 89c4f4dde1a1
Revises: 700efd2e57b0
Create Date: 2016-05-26 17:27:10.115413

"""

# revision identifiers, used by Alembic.
revision = '89c4f4dde1a1'
down_revision = '700efd2e57b0'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('vuls',
    sa.Column('id', mysql.INTEGER(unsigned=True), nullable=False),
    sa.Column('name', sa.String(length=56), nullable=True),
    sa.Column('description', sa.String(length=512), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('vuls')
    ### end Alembic commands ###