"""empty message

Revision ID: 9292b3f21402
Revises: 858c1138572e
Create Date: 2019-02-20 12:32:43.327563

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9292b3f21402'
down_revision = '858c1138572e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('titles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.drop_table('works')
    op.create_foreign_key(None, 'interfacetests', 'interfacetests', ['pid'], ['id'])
    op.create_unique_constraint(None, 'projects', ['project_name'])
    op.create_foreign_key(None, 'tasks', 'ceshihuanjing', ['testevent'], ['id'])
    op.create_foreign_key(None, 'tasks', 'projects', ['prject'], ['id'])
    op.drop_column('tasks', 'taskdesc')
    op.create_foreign_key(None, 'tstresults', 'projects', ['projects_id'], ['id'])
    op.create_foreign_key(None, 'users', 'titles', ['work_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='foreignkey')
    op.drop_constraint(None, 'tstresults', type_='foreignkey')
    op.add_column('tasks', sa.Column('taskdesc', sa.TEXT(length=252), nullable=True))
    op.drop_constraint(None, 'tasks', type_='foreignkey')
    op.drop_constraint(None, 'tasks', type_='foreignkey')
    op.drop_constraint(None, 'projects', type_='unique')
    op.drop_constraint(None, 'interfacetests', type_='foreignkey')
    op.create_table('works',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.drop_table('titles')
    # ### end Alembic commands ###
