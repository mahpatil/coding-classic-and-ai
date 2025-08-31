"""create rewardpoint table

Revision ID: d86ac8c4097b
Revises: 
Create Date: 2025-08-31 09:27:16.519098

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from datetime import date


# revision identifiers, used by Alembic.
revision: str = 'd86ac8c4097b'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade() -> None:
    """Upgrade schema."""
    reward_point_table = op.create_table(
        'reward_point',
        sa.Column('id', sa.Integer, nullable=False, autoincrement=True, primary_key=True),
        sa.Column('user_id', sa.Integer),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('date', sa.Date, nullable=False),
        sa.Column('points', sa.Integer, nullable=False)
    )
    op.bulk_insert(
        reward_point_table,
            [
                {
                    "user_id": 1,
                    "name": "John Smith",
                    "date": date(2025, 8, 24),
                    "points": 3
                },
                {
                    "user_id": 1,
                    "name": "John Smith",
                    "date": date(2025, 8, 29),
                    "points": 3
                },
                {
                    "user_id": 2,
                    "name": "Ed Williams",
                    "date": date(2025, 8, 30),
                    "points": 5
                },
                {
                    "user_id": 3,
                    "name": "Wendy Jones",
                    "date": date(2025, 8, 30),
                    "points": 5
                },
            ],
    )
def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('reward_point')
