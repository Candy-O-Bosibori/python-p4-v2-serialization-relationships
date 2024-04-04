"""empty message

Revision ID: 0396e1aaf681
Revises: 
Create Date: 2024-04-04 14:19:44.092282

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0396e1aaf681'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('enclosures',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('environment', sa.String(), nullable=True),
    sa.Column('open_to_visitors', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_enclosures'))
    )
    op.create_table('zookeepers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('birthday', sa.Date(), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_zookeepers')),
    sa.UniqueConstraint('name', name=op.f('uq_zookeepers_name'))
    )
    op.create_table('animals',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('species', sa.String(), nullable=True),
    sa.Column('zookeeper_id', sa.Integer(), nullable=True),
    sa.Column('enclosure_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['enclosure_id'], ['enclosures.id'], name=op.f('fk_animals_enclosure_id_enclosures')),
    sa.ForeignKeyConstraint(['zookeeper_id'], ['zookeepers.id'], name=op.f('fk_animals_zookeeper_id_zookeepers')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_animals')),
    sa.UniqueConstraint('name', name=op.f('uq_animals_name'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('animals')
    op.drop_table('zookeepers')
    op.drop_table('enclosures')
    # ### end Alembic commands ###