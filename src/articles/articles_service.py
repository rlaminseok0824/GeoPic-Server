import io
import uuid
from beanie import PydanticObjectId
from fastapi import UploadFile
from .articles_model import Articles,ArticleResponse
from .articles_entity import Articles as ArticlesEntity
from nest.core.decorators.database import db_request_handler
from nest.core import Injectable
import boto3


@Injectable
class ArticlesService:
    @db_request_handler
    async def add_articles(self, articles: Articles):
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
        return await ArticlesEntity.find(
        {
            "$and": [
                {"lat": {"$gte": lat - 50, "$lte": lat + 50}},
                {"lon": {"$gte": lon - 50, "$lte": lon + 50}}
            ]
        }
    ).to_list()

    @db_request_handler
    async def delete_article(self, article_id: str):
        delete = await ArticlesEntity.get(article_id)
        await delete.delete()
        return "Deleted"
    
    @db_request_handler
    async def update_article(self, article_id: str, articles: Articles):
        return await ArticlesEntity.update(article_id, articles.dict())
    
    @db_request_handler
    async def upload_image(self, file: UploadFile):
        s3 = _s3_connect()
        return await upload_file(s3,file)

def _s3_connect() -> boto3.client:
    session = boto3.Session(profile_name='default')
    s3 = session.client('s3')

    return s3

async def upload_file(s3: boto3.client, file: UploadFile) -> str:
    file_content = await file.read()

    fileobj = io.BytesIO(file_content)

    img_name = str(uuid.uuid4()) + "." + file.content_type.split("/")[1]

    s3.upload_fileobj(fileobj, 'fullstack-be-repo', img_name)

    return "https://{0}.s3.ap-northeast-2.amazonaws.com/{1}".format('fullstack-be-repo', img_name)