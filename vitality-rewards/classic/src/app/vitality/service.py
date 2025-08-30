import logging
from sqlalchemy.orm import Session, joinedload, load_only
from datetime import date

from .models import (
    Activity,
    RewardPoint,
)
log = logging.getLogger(__name__)
db_session, db_engine = None, None
def get_reward_points(*, user_id: int) -> list[RewardPoint | None]:
    """Returns reward points for a user."""
    return (
        db_session.query(RewardPoint)
        .filter(RewardPoint.user_id == user_id)
        .filter(RewardPoint.date >= date.today(-7))
        .all()
    )