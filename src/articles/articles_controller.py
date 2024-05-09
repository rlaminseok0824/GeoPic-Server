from nest.core import Controller, Get, Post

from .articles_service import ArticlesService
from .articles_model import Articles


@Controller("articles")
class ArticlesController:

    def __init__(self, articles_service: ArticlesService):
        self.service = articles_service

    @Get("/")
    async def get_articles(self):
        return await self.articles_service.get_articles()

    @Post("/")
    async def add_articles(self, articles: Articles):
        return await self.articles_service.add_articles(articles)
 