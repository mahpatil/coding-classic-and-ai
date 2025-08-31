#from pydantic.dataclasses import dataclass
from pydantic import BaseModel
from sqlalchemy.orm import declarative_base, Mapped, mapped_column
from sqlalchemy import func
from datetime import datetime
from sqlmodel import Field, SQLModel


Base = declarative_base()
#@dataclass
# class RewardPoint(Base, BaseModel):
#     __tablename__ = "reward_point"
#     user_id: Mapped[int] = mapped_column(primary_key=True)
#     name: Mapped[str]
#     date: Mapped[datetime] = mapped_column(
#         insert_default=func.utc_date(), default=None
#     )
#     points: Mapped[int] = mapped_column(default=0)

#     class Config:
#         orm_mode = True


class RewardPoint(SQLModel, table=True):
    __tablename__ = "reward_point"
    id: int | None = Field(default=None, primary_key=True)
    user_id: int | None = Field(default=None)
    name: str
    date: datetime
    points: int | None = None

class Activity(Base):
    __tablename__ = "activity"
    user_id:  Mapped[int] = mapped_column(primary_key=True)
    activity_type: Mapped[str]
    heartRate: Mapped[int]
    caloriesBurned: Mapped[int]
    steps: Mapped[int]
    maxHeartRate: Mapped[int]
    duration: Mapped[int]

    class Config:
        orm_mode = True
