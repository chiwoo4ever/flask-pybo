"""empty message

Revision ID: c0b3b3bf5bcb
Revises: 857c3b90bec1
Create Date: 2021-08-10 13:37:42.585835

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c0b3b3bf5bcb'
down_revision = '857c3b90bec1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('question', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_id', sa.Integer(), server_default='1', nullable=True))
        #batch_op.create_foreign_key(None, 'user', ['user_id'], ['id'], ondelete='CASCADE')
        batch_op.create_foreign_key('user_id', 'user', ['user_id'], ['id'], ondelete='CASCADE')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('question', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('user_id')

    # ### end Alembic commands ###
