"""add 3 bullet columns

Revision ID: fd1d45695f45
Revises: 76164053a403
Create Date: 2023-09-01 11:45:42.056049

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fd1d45695f45'
down_revision = '76164053a403'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('projects', schema=None) as batch_op:
        batch_op.add_column(sa.Column('bullet1', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('bullet2', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('bullet3', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('projects', schema=None) as batch_op:
        batch_op.drop_column('bullet3')
        batch_op.drop_column('bullet2')
        batch_op.drop_column('bullet1')

    # ### end Alembic commands ###
