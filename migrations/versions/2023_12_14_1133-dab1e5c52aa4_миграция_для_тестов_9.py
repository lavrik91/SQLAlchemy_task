"""миграция для тестов 9

Revision ID: dab1e5c52aa4
Revises: 08956c5d593b
Create Date: 2023-12-14 11:33:08.803663

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'dab1e5c52aa4'
down_revision: Union[str, None] = '08956c5d593b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
