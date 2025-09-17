from fastapi import APIRouter, HTTPException, status
from .service import get_reward_points
from .models import RewardPoint, Activity
from typing import List
from starlette.requests import Request

router = APIRouter(prefix="/rewards", tags=["rewards"])

@router.post("/calculate",
            response_model=list[RewardPoint],
            summary="Calculates and returns reward points for a user.",)
def rewards_calculate(user_id: int, activities: list[Activity], request: Request) -> List[RewardPoint]:
    """Endpoint to calculate rewards for a user."""
    # Logic to calculate rewards would go here
    # For now, we return a success message
    return {"message": "Rewards calculated successfully"}


@router.get("/health", status_code=status.HTTP_200_OK)
def get_health():
    return {"Health": "OK"}

@router.get("/for-user/{user_id}",
            response_model=list[RewardPoint],
            summary="Retrieves reward points for a user.",)
def get_activities(user_id) -> List[RewardPoint]:
    reward_points = get_reward_points(user_id=user_id)
    if not reward_points:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=[{"msg": "The requested userid does not exist."}],
        )
    return reward_points

