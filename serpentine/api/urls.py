from ninja import NinjaAPI

from .v1.routers import main_router as router_v1

api_v1 = NinjaAPI(version="1.0", title="Serpentine API")

api_v1.add_router("", router_v1)
