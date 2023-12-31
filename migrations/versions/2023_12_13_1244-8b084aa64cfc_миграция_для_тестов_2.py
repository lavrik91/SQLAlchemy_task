"""миграция для тестов 2

Revision ID: 8b084aa64cfc
Revises: 86175c445386
Create Date: 2023-12-13 12:44:57.216498

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8b084aa64cfc'
down_revision: Union[str, None] = '86175c445386'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('order_tests')
    op.drop_table('bank_accounts')
    op.drop_table('customers')

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('candies',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('title', sa.VARCHAR(length=200), autoincrement=False, nullable=True),
    sa.Column('state', sa.VARCHAR(length=20), server_default=sa.text("'full'::character varying"), autoincrement=False, nullable=False),
    sa.Column('owner', sa.VARCHAR(length=100), server_default=sa.text("'teacher'::character varying"), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='candies_pkey')
    )
    op.create_table('customers',
    sa.Column('customer_id', sa.INTEGER(), server_default=sa.text("nextval('customers_customer_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('customer_id', name='customers_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_table('bank_accounts',
    sa.Column('account_id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('balance', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('account_id', name='bank_accounts_pkey')
    )
    op.create_table('order_tests',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('customer_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('total_amount', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['customer_id'], ['customers.customer_id'], name='order_tests_customer_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='order_tests_pkey')
    )
    # ### end Alembic commands ###
