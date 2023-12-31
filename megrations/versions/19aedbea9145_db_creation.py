"""DB creation

Revision ID: 19aedbea9145
Revises: 
Create Date: 2023-08-30 20:10:38.018192

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '19aedbea9145'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('obs',
                    sa.Column('host', sa.String(), nullable=False),
                    sa.Column('port', sa.Integer(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
                    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('team',
                    sa.Column('name', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('name')
    )
    template = op.create_table('template',
                               sa.Column('name', sa.String(), nullable=False),
                               sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
                               sa.PrimaryKeyConstraint('id'),
                               sa.UniqueConstraint('name')
    )
    op.create_table('team_obs',
                    sa.Column('team_id', sa.Integer(), nullable=False),
                    sa.Column('obs_id', sa.Integer(), nullable=False),
                    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
                    sa.ForeignKeyConstraint(['obs_id'], ['obs.id'], ),
                    sa.ForeignKeyConstraint(['team_id'], ['team.id'], ),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('obs_id'),
                    sa.UniqueConstraint('team_id')
    )
    op.create_table('team_photo',
                    sa.Column('team_id', sa.Integer(), nullable=False),
                    sa.Column('photo_path', sa.String(), nullable=True),
                    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
                    sa.ForeignKeyConstraint(['team_id'], ['team.id'], ),
                    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('team_template',
                    sa.Column('team_id', sa.Integer(), nullable=False),
                    sa.Column('template_id', sa.Integer(), nullable=False),
                    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
                    sa.ForeignKeyConstraint(['team_id'], ['team.id'], ),
                    sa.ForeignKeyConstraint(['template_id'], ['template.id'], ),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('team_id')
    )
    op.create_table('user_team',
                    sa.Column('id', sa.BigInteger(), nullable=False),
                    sa.Column('team_id', sa.Integer(), nullable=False),
                    sa.ForeignKeyConstraint(['team_id'], ['team.id'], ),
                    sa.PrimaryKeyConstraint('id')
    )
    op.bulk_insert(
        template,
        [
            {
                "id": 0,
                "name": "TITLE1",
            },
            {
                "id": 1,
                "name": "TITLE2",
            },
            {
                "id": 2,
                "name": "TITLE3",
            },
        ],
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_team')
    op.drop_table('team_template')
    op.drop_table('team_photo')
    op.drop_table('team_obs')
    op.drop_table('template')
    op.drop_table('team')
    op.drop_table('obs')
    # ### end Alembic commands ###
