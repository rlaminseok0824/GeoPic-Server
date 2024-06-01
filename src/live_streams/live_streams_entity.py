from datetime import datetime
from typing import List, Optional
from beanie import Document


class LiveStreams(Document):
    username: str
    title: str
    content: str
    videoID: str
    latitude: float
    longitude: float
    tags: Optional[List[str]]
    location: str
    date: datetime

    class Config:
        schema_extra = {
            "example": {
                "username": "user123",
                "title": "Live Stream Title",
                "content": "Live Stream Content",
                "videoID": "videoID",
                "lat": 123.456,
                "lon": 789.012,
                "tags": ["tag1", "tag2"],
                "location": "Live Stream Location",
                "date": "2022-01-01T00:00:00.000Z"
            }
        }