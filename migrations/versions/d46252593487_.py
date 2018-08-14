"""empty message

Revision ID: d46252593487
Revises: f5a221feed22
Create Date: 2018-08-14 14:33:48.847011

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd46252593487'
down_revision = 'f5a221feed22'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('genotype_description', sa.Column('inference_tool_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'genotype_description', 'inference_tool', ['inference_tool_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'genotype_description', type_='foreignkey')
    op.drop_column('genotype_description', 'inference_tool_id')
    # ### end Alembic commands ###
