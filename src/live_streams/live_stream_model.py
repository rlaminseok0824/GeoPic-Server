from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel


class LiveStream(BaseModel):
    username: str
    title: str
    content: str = ""
    videoId: Optional[str]
    latitude: float
    longitude: float
    tags: Optional[List[str]]
    location: str
    date: datetime



class LiveStreamResponse(LiveStream):
    id: str