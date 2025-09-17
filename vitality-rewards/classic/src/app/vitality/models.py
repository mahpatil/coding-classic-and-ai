from pydantic import BaseModel
from sqlalchemy.orm import declarative_base, Mapped, mapped_column
from sqlalchemy import func
from datetime import datetime
from sqlmodel import Field, SQLModel
from .enums import ActivityType


Base = declarative_base()

class RewardPoint(SQLModel, table=True):
    __tablename__ = "reward_point"
    id: int | None = Field(default=None, primary_key=True)
    user_id: int | None = Field(default=None)
    name: str
    date: datetime
    points: int | None = None
    reason: str | None = None

class Activity(Base):
    __tablename__ = "activity"
    id: int | None = Field(default=None, primary_key=True)
    activity_id: int | None = Field(default=None)
    user_id: int | None = Field(default=None)
    date: datetime
    activity_type: Mapped[ActivityType] = mapped_column(ActivityType, nullable=False)
    heartRate: Mapped[int]
    caloriesBurned: Mapped[int]
    steps: Mapped[int]
    maxHeartRate: Mapped[int]
    duration: Mapped[int]

    class Config:
        orm_mode = True
