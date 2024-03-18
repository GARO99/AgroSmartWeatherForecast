from fastapi import APIRouter

from Domain.Entities.FamerLands.farmer_land import FarmerLand

farmer_land_router = APIRouter(
    prefix="/famerland",
    tags=["famerland"],
)

@farmer_land_router.post("/", response_model=FarmerLand)
async def get_farmer_lands():
    return []