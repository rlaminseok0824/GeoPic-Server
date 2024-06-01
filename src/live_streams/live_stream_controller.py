from typing import List
from nest.core import Controller, Get, Post,Put, Delete

from src.live_streams.live_stream_model import LiveStream, LiveStreamResponse
from src.live_streams.live_stream_service import LiveStreamService


@Controller("live_streams")
class LiveStreamController:

    def __init__(self, live_stream_service: LiveStreamService):
        self.service = live_stream_service

    @Get("/")
    async def get_live_streams(self) -> List[LiveStreamResponse]:
        return await self.live_stream_service.get_live_streams()
    
    @Post("/")
    async def add_live_stream(self, live_stream: LiveStream):
        return await self.live_stream_service.add_live_stream(live_stream)
    
    @Delete("/<live_stream_id>")
    async def delete_live_stream(self, live_stream_id: str):
        return await self.live_stream_service.delete_live_stream(live_stream_id)
    