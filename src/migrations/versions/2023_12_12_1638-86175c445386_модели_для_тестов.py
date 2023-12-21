"""модели для тестов

Revision ID: 86175c445386
Revises: 2de137f06674
Create Date: 2023-12-12 16:38:21.400564

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '86175c445386'
down_revision: Union[str, None] = '2de137f06674'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('candies',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=200), nullable=True),
    sa.Column('state', sa.String(length=20), server_default='full', nullable=False),
    sa.Column('owner', sa.String(length=100), server_default='teacher', nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('order_tests',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('customer_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('total_amount', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['customer_id'], ['customers.customer_id'], name='order_tests_customer_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='order_tests_pkey')
    )
    op.create_table('bank_accounts',
    sa.Column('account_id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('balance', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('account_id', name='bank_accounts_pkey')
    )
    op.create_table('customers',
    sa.Column('customer_id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('customer_id', name='customers_pkey')
    )
    op.drop_table('candies')
    # ### end Alembic commands ###
