from nest.core import Injectable
from nest.core.decorators.database import db_request_handler

from src.commons.grpc import GrpcClient

from .live_streams_entity import LiveStreams as LiveStreamEntity
from .live_stream_model import LiveStream, LiveStreamResponse


@Injectable
class LiveStreamService:
    @db_request_handler
    async def get_live_streams(self):
        grpc = GrpcClient()
        grpc_response = grpc.get_trackLocals()
        
        if not grpc_response:
            return []
        grpc_ids = {str(response.id) for response in grpc_response}

        live_streams = await LiveStreamEntity.find_all().to_list()

        filtered_live_streams = [
            live_stream for live_stream in live_streams if str(live_stream.id) in grpc_ids
        ]

        return [
            LiveStreamResponse(
                id=str(live_stream.id),
                **live_stream.dict(exclude={"id"})
            )
            for live_stream in filtered_live_streams
        ]
    
    @db_request_handler
    async def add_live_stream(self, live_stream: LiveStream):
        new_live_stream = LiveStreamEntity(
            **live_stream.dict()
        )
        await new_live_stream.save()
        return LiveStreamResponse(id=str(new_live_stream.id), **live_stream.dict())
    
    @db_request_handler
    async def delete_live_stream(self, article_id: str):
        delete = await LiveStreamEntity.get(article_id)
        await delete.delete()
        return "Deleted"
