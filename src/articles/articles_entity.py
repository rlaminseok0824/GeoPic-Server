from datetime import datetime
from beanie import Document
                
from typing import List, Optional
from beanie import Document

class Articles(Document):
    username: str
    title: str
    content: str
    imageUrl: Optional[str]
    latitude: float
    longitude: float
    tags: Optional[List[str]]
    location: str
    date: datetime
    
    class Config:
        schema_extra = {
            "example": {
                "username": "user123",
                "title": "Article Title",
                "content": "Article Content",
                "images": ["image1.jpg", "image2.jpg"],
                "lat": 123.456,
                "lon": 789.012,
                "tags": ["tag1", "tag2"],
                "location": "Article Location",
                "date" : "2022-01-01T00:00:00.000Z"
            }
        }
