"""empty message

Revision ID: 18a8b9188750
Revises: 248699827598
Create Date: 2018-08-09 10:58:16.399590

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '18a8b9188750'
down_revision = '248699827598'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('forward_primer', sa.Column('fw_primer_seq', sa.String(length=255), nullable=True))
    op.drop_column('forward_primer', 'primer_seq')
    op.add_column('reverse_primer', sa.Column('rv_primer_seq', sa.String(length=255), nullable=True))
    op.drop_column('reverse_primer', 'primer_seq')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('reverse_primer', sa.Column('primer_seq', mysql.VARCHAR(length=255), nullable=True))
    op.drop_column('reverse_primer', 'rv_primer_seq')
    op.add_column('forward_primer', sa.Column('primer_seq', mysql.VARCHAR(length=255), nullable=True))
    op.drop_column('forward_primer', 'fw_primer_seq')
    # ### end Alembic commands ###
