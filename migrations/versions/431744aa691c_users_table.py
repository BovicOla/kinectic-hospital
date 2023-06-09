"""users table

Revision ID: 431744aa691c
Revises: 
Create Date: 2023-03-28 05:13:32.012178

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '431744aa691c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('firstname', sa.String(length=64), nullable=True),
    sa.Column('lastname', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('age', sa.Integer(), nullable=True),
    sa.Column('phone_number', sa.String(length=16), nullable=True),
    sa.Column('address', sa.String(length=256), nullable=True),
    sa.Column('gender', sa.Enum('male', 'female', name='gender'), nullable=True),
    sa.Column('employment', sa.Enum('student', 'employed', 'self employed', 'unemployed', 'ful time job', 'part time job'), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.Column('last_seen', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_user_email'), ['email'], unique=True)
        batch_op.create_index(batch_op.f('ix_user_firstname'), ['firstname'], unique=False)
        batch_op.create_index(batch_op.f('ix_user_lastname'), ['lastname'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_user_lastname'))
        batch_op.drop_index(batch_op.f('ix_user_firstname'))
        batch_op.drop_index(batch_op.f('ix_user_email'))

    op.drop_table('user')
    # ### end Alembic commands ###
