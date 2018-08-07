"""empty message

Revision ID: 4f1be19eab44
Revises: 4960130fc7f0
Create Date: 2018-08-06 11:03:25.574437

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '4f1be19eab44'
down_revision = '4960130fc7f0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('forward_primer',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('primer_seq', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('reverse_primer',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('primer_seq', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('primer')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('primer',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('primer_seq', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('repertoire', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['repertoire'], ['repertoire.id'], name='primer_ibfk_1'),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.drop_table('reverse_primer')
    op.drop_table('forward_primer')
    # ### end Alembic commands ###
