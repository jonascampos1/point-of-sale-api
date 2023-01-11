"""Initial migration.

Revision ID: 24afe87fb61c
Revises: 
Create Date: 2023-01-10 21:57:24.120266

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '24afe87fb61c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('productotemp')
    op.drop_table('productotemp2')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('productotemp2',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('nombre', sa.VARCHAR(length=150), autoincrement=False, nullable=True),
    sa.Column('precio', sa.SMALLINT(), autoincrement=False, nullable=True),
    sa.Column('estado', sa.VARCHAR(length=45), autoincrement=False, nullable=True),
    sa.Column('foto', sa.VARCHAR(length=45), autoincrement=False, nullable=True),
    sa.Column('descripcion', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('tipo', sa.VARCHAR(length=2), autoincrement=False, nullable=True),
    sa.Column('tipo_foto', sa.SMALLINT(), autoincrement=False, nullable=True),
    sa.Column('rating', sa.SMALLINT(), autoincrement=False, nullable=True),
    sa.Column('comentario', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('comentario2', sa.TEXT(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='productotemp2_pkey')
    )
    op.create_table('productotemp',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('nombre', sa.VARCHAR(length=150), autoincrement=False, nullable=True),
    sa.Column('precio', sa.SMALLINT(), autoincrement=False, nullable=True),
    sa.Column('estado', sa.VARCHAR(length=45), autoincrement=False, nullable=True),
    sa.Column('foto', sa.VARCHAR(length=45), autoincrement=False, nullable=True),
    sa.Column('descripcion', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('tipo', sa.VARCHAR(length=2), autoincrement=False, nullable=True),
    sa.Column('tipo_foto', sa.SMALLINT(), autoincrement=False, nullable=True),
    sa.Column('rating', sa.SMALLINT(), autoincrement=False, nullable=True),
    sa.Column('comentario', sa.TEXT(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='productotemp_pkey')
    )
    op.drop_table('user')
    # ### end Alembic commands ###