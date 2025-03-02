"""Added alt_text to Photo model

Revision ID: 033ec44f881b
Revises: 
Create Date: 2025-02-16 16:00:24.085549

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '033ec44f881b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('photo', schema=None) as batch_op:
        batch_op.add_column(sa.Column('alt_text', sa.Text(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('photo', schema=None) as batch_op:
        batch_op.drop_column('alt_text')

    # ### end Alembic commands ###
