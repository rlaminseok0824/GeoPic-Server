from nest.core import Controller, Get, Post,Put, Delete
from src.geocodes.geocodes_service import GeoService


@Controller("geocodes")
class GeoController:
    def __init__(self, geo_service: GeoService):
        self.geo_service = geo_service

    @Get("/")
    async def get_geocodes_from_location(self,position: str):
        return await self.geo_service.get_geocodes_from_location(position)