from beanie import Document
                
from typing import List, Optional
from beanie import Document

class Articles(Document):
    username: str
    title: str
    content: str
    image: Optional[str]
    lat: float
    lon: float
    tags: Optional[List[str]]
    location: str
    
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
                "location": "Article Location"
            }
        }
