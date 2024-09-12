"""add content column to post table

Revision ID: a485651dcaad
Revises: 96e2a1998676
Create Date: 2024-09-12 01:44:43.986266

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a485651dcaad'
down_revision: Union[str, None] = '96e2a1998676'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
