"""empty message

Revision ID: c50a5054da30
Revises: cdb91be9d643
Create Date: 2021-05-15 20:03:33.625722

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c50a5054da30'
down_revision = 'cdb91be9d643'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('dateofbirth', sa.DateTime(), nullable=True))
    op.create_index(op.f('ix_user_dateofbirth'), 'user', ['dateofbirth'], unique=False)
    op.create_index(op.f('ix_user_name'), 'user', ['name'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_name'), table_name='user')
    op.drop_index(op.f('ix_user_dateofbirth'), table_name='user')
    op.drop_column('user', 'dateofbirth')
    # ### end Alembic commands ###