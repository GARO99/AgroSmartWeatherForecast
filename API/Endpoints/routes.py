from fastapi import APIRouter

from API.Endpoints.Farmer_Lands.farmer_land import farmer_land_router

routers = APIRouter()
router_list = [farmer_land_router]

for router in router_list:
    routers.include_router(router)
