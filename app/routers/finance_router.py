from fastapi import APIRouter
from app.endpoints import movements_end

api_router = APIRouter()

api_router.include_router(
    movements_end.router,
    prefix="/movements",
    tags = ["movimientos"]
)