from fastapi import APIRouter, HTTPException, status
from .service import get_reward_points
from .models import RewardPoint
from typing import List
from starlette.requests import Request

router = APIRouter(prefix="/rewards", tags=["rewards"])

@router.post("/calculate")
def rewards_calculate():
    """Endpoint to calculate rewards for a user."""
    # Logic to calculate rewards would go here
    # For now, we return a success message
    return {"message": "Rewards calculated successfully"}

@router.get("/{user_id}",
            response_model=list[RewardPoint],
            summary="Retrieves reward points for a user.",)
def get_activities(request: Request) -> List[RewardPoint]:
    case = get_reward_points(user_id=request.path_params["user_id"])
    if not case:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=[{"msg": "The requested case does not exist."}],
        )
    return case



@router.get("/hello/")
def get_hello():
    return {"Hello": "World"}

