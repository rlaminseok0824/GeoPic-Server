from typing import List

from fastapi import File, UploadFile

from src.commons.file_upload import upload_images_to_s3
from .articles_model import Articles,ArticleResponse
from .articles_entity import Articles as ArticlesEntity
from nest.core.decorators.database import db_request_handler
from nest.core import Injectable


@Injectable
class ArticlesService:
    @db_request_handler
    async def add_articles(self, articles: Articles):
        print(articles.dict())
        new_articles = ArticlesEntity(
            **articles.dict()
        )        
        await new_articles.save()
        return ArticleResponse(id=str(new_articles.id), **articles.dict())

    @db_request_handler
    async def get_articles(self):
        return [
            ArticleResponse(
                id=str(article.id),
                         **article.dict(exclude={"id"})                            )
            for article in await ArticlesEntity.find_all().to_list()
        ]
    
    @db_request_handler
    async def get_article(self, article_id: str):
        return await ArticlesEntity.get(article_id)
    
    @db_request_handler
    async def get_article_by_position(self, lat: float, lon: float):
        await ArticlesEntity.find(
        {
            "$and": [
                {"latitude": {"$gte": lat - 50, "$lte": lat + 50}},
                {"longitude": {"$gte": lon - 50, "$lte": lon + 50}}
            ]
        }
    ).to_list()
        return [
            ArticleResponse(
                id=str(article.id),
                **article.dict(exclude={"id"})
            )
            for article in await ArticlesEntity.find(
                {
                    "$and": [
                        {"latitude": {"$gte": lat - 50, "$lte": lat + 50}},
                        {"longitude": {"$gte": lon - 50, "$lte": lon + 50}}
                    ]
                }).to_list()
        ]

    @db_request_handler
    async def delete_article(self, article_id: str):
        delete = await ArticlesEntity.get(article_id)
        await delete.delete()
        return "Deleted"
    
    @db_request_handler
    async def update_article(self, article_id: str, articles: Articles):
        update = await ArticlesEntity.get(article_id)
        update.update(**articles.dict(exclude={"id"}))
        return ArticleResponse(id=str(update.id), **articles.dict(exclude={"id"}))
    
    @db_request_handler
    async def upload_image(self, pictures: List[UploadFile] = File(None)):
        if pictures:
            contents_list = []
            for picture in pictures:
                contents = await picture.read()
                contents_list.append(contents)
            image_urls = upload_images_to_s3(pictures, contents_list)   

        return {"urls": image_urls}


