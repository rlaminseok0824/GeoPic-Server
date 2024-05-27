from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel


class Articles(BaseModel):
    username: str
    title: str
    content: str
    # images: Optional[List[str]] = ["https://fullstack-be-repo.s3.ap-northeast-2.amazonaws.com/3e1db88d-27c8-4caa-b0df-30a52731123e.png"]
    imageUrl: Optional[str]
    latitude: float
    longitude: float
    tags: Optional[List[str]]
    location: str
    date: datetime



class ArticleResponse(Articles):
    id: str