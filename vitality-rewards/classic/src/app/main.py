from .vitality.router import router as vitality_router
#from app.config import settings
from fastapi import FastAPI

app = FastAPI()
app.include_router(vitality_router)

