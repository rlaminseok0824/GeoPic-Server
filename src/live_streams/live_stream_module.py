from nest.core import Module
from .live_stream_controller import LiveStreamController
from .live_stream_service import LiveStreamService

@Module(
    controllers=[LiveStreamController],
    providers=[LiveStreamService],
    imports=[]
)
class LiveStreamModule:
    pass