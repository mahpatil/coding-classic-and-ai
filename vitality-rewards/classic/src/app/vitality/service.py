import logging
from sqlalchemy.orm import Session, joinedload, load_only
from datetime import date, timedelta
from sqlalchemy import select
from ..database import DbSession
from .models import Activity
from .enums import ActivityType

from .models import (
    Activity,
    RewardPoint,
)
log = logging.getLogger(__name__)

def get_reward_points(*, user_id: int) -> list[RewardPoint | None]:
    """Returns reward points for a user."""
    log.info("get_reward_points: user_id=%s", user_id)
    return DbSession.query(RewardPoint).filter(RewardPoint.user_id == user_id).all()

        
    # return (
    #     DbSession.begin().select(RewardPoint)
    #     .filter(RewardPoint.user_id == user_id)
    #     .filter(RewardPoint.date >= date.today(-7))
    #     .all()
    # )

def calculate(*, user_id: int, activities: list[Activity]) -> list[RewardPoint | None]:
    """Returns reward points calculated for a user."""
    log.info("calculate: user_id=%s", user_id)

    ## Calculate points for all activities using vectorize
    reward_points = [calculate_points(activity=activity) for activity in activities]

    ## Remove all duplicate activities per type per day and max points activity
    unique_reward_points = {}
    for rp in reward_points:
        key = (rp.date, rp.activity_type)
        if key not in unique_reward_points or rp.points > unique_reward_points[key].points:
            unique_reward_points[key] = rp
    reward_points = list(unique_reward_points.values())
    ## Add reward points to DB
    for rp in reward_points:
        add_reward_point(reward_point=rp)
    return reward_points.values()

def calculate_points(*, activity: Activity) -> RewardPoint:
    """Calculates points based on activity type and metrics."""
    reward_point = RewardPoint(
                user_id=activity.user_id,
                activity_id=activity.id,
                name=f"User {activity.user_id}",
                date=activity.date,
                points=0,
                reason=f"Points for {activity.activity_type} activity"
            )
    match activity.activity_type:
        case ActivityType.WALKING:
            if activity.steps >= 12500: # 12,500+ steps
                reward_point.points = 8
            elif activity.steps >= 10000: # 10,000 steps or 12,500 steps
                reward_point.points = 5
            elif activity.steps >= 7500: # 7,500 steps or 10,000 steps
                reward_point.points = 3
            

        case _:
            if activity.duration >= 30:
                if activity.maxHeartRate >= 150: ## 30 mins and 70% max HR
                    reward_point.points = 8
                elif activity.maxHeartRate >= 120: ## 30 mins and 60% max HR
                    reward_point.points = 5
                elif activity.caloriesBurned >= 150: ## 30 mins and 150 kcal at 300 kcal/hr
                    reward_point.points = 3
                
            
    return reward_point
            

def add_reward_point(*, reward_point: RewardPoint) -> RewardPoint:
    """Adds a reward point entry."""
    log.info("add_reward_point: user_id=%s, date=%s, points=%s",
             reward_point.user_id, reward_point.date, reward_point.points)
    DbSession.add(reward_point)
    DbSession.commit()
    DbSession.refresh(reward_point)
    return reward_point