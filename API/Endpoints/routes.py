from fastapi import APIRouter

from API.Endpoints.FarmerLands.FarmerLand import farmer_land_router

routers = APIRouter()
router_list = [farmer_land_router]

for router in router_list:
    routers.include_router(router)
