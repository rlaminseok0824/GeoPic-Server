from .articles_model import Articles
from .articles_entity import Articles as ArticlesEntity
from nest.core.decorators.database import db_request_handler
from nest.core import Injectable


@Injectable
class ArticlesService:

    @db_request_handler
    async def add_articles(self, articles: Articles):
        new_articles = ArticlesEntity(
            **articles.dict()
        )
        await new_articles.save()
        return new_articles.id

    @db_request_handler
    async def get_articles(self):
        return await ArticlesEntity.find_all().to_list()
