import logging
from sqlalchemy.orm import Session, joinedload, load_only
from datetime import date, timedelta
from sqlalchemy import select
from ..database import DbSession

from .models import (
    Activity,
    RewardPoint,
)
log = logging.getLogger(__name__)

def get_reward_points(*, user_id: int) -> list[RewardPoint | None]:
    """Returns reward points for a user."""
    # return DbSession.query(RewardPoint).filter(
    #         RewardPoint.user_id == user_id
    #     ).filter(
    #         RewardPoint.date >= date.today() - timedelta(days=7)
    #     ).all()
    log.info("get_reward_points: user_id=%s", user_id)
    return DbSession.query(RewardPoint).filter(RewardPoint.user_id == user_id).all()

        
    # return (
    #     DbSession.begin().select(RewardPoint)
    #     .filter(RewardPoint.user_id == user_id)
    #     .filter(RewardPoint.date >= date.today(-7))
    #     .all()
    # )