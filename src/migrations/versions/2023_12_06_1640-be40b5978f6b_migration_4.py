"""migration_4

Revision ID: be40b5978f6b
Revises: 08a85fd8de03
Create Date: 2023-12-06 16:40:32.045736

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'be40b5978f6b'
down_revision: Union[str, None] = '08a85fd8de03'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('customers', sa.Column('name', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('customers', 'name')
    # ### end Alembic commands ###