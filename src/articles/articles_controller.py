from typing import List
from fastapi import File, UploadFile
from nest.core import Controller, Get, Post,Put, Delete

from .articles_service import ArticlesService
from .articles_model import ArticleResponse, Articles
from .articles_entity import Articles as ArticlesEntity

@Controller("articles")
class ArticlesController:

    def __init__(self, articles_service: ArticlesService):
        self.service = articles_service

    @Get("/")
    async def get_articles(self) -> List[ArticleResponse]:
        return await self.articles_service.get_articles()

    @Post("/")
    async def add_articles(self, articles: Articles):
        return await self.articles_service.add_articles(articles)
    
    @Get("/<article_id>")
    async def get_article(self, article_id: str):
        return await self.articles_service.get_article(article_id)
    
    @Get("/position")
    async def get_articles_by_position(self, lat: float, lon: float):
        return await self.articles_service.get_article_by_position(lat, lon)
    
    @Put("/{article_id}")
    async def update_article(self,article_id: str ,articles: Articles):
        return await self.articles_service.update_article(article_id, articles)
    
    @Delete("/<article_id>")
    async def delete_article(self, article_id: str):
        return await self.articles_service.delete_article(article_id)
    
    @Post("/picture")
    async def upload_image(self, pictures: List[UploadFile] = File(None)):
        return await self.articles_service.upload_image(pictures)
    
    @Delete("/delete")
    async def delete_all(self):
        return ArticlesEntity.delete_all()
    

 