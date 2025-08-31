from sqlalchemy import create_engine, event
import logging
from typing import Annotated, Any
from sqlalchemy.orm import Session
from fastapi import Depends
from sqlalchemy.orm import sessionmaker

logger = logging.getLogger(__name__)

engine = create_engine(
    "sqlite:///data/vitality-rewards.db", connect_args={"autocommit": False}
)
Session = sessionmaker(bind=engine)
DbSession = Session()
