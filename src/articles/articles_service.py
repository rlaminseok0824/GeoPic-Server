import io
from typing import List
import uuid
from beanie import PydanticObjectId
from fastapi import File, UploadFile
from .articles_model import Articles,ArticleResponse
from .articles_entity import Articles as ArticlesEntity
from nest.core.decorators.database import db_request_handler
from nest.core import Injectable
import boto3


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
    async def upload_image(self, pictures: List[UploadFile] = File(None)):
        if pictures:
            contents_list = []
            for picture in pictures:
                contents = await picture.read()
                contents_list.append(contents)
            image_urls = upload_images_to_s3(pictures, contents_list)   

        return {"urls": image_urls}

def _s3_connect() -> boto3.client:
    session = boto3.Session(profile_name='default')
    s3 = session.client('s3')

    return s3

def upload_images_to_s3(
    files: List[UploadFile],
    contents_list: List[bytes],
) -> List[str]:
    s3 = _s3_connect()
    imageUrls = []
    try:
        for idx, file in enumerate(files):
            image_name = str(uuid.uuid4()) + "." + file.content_type.split("/")[1]

            # image_name = file.filename
            s3.put_object(
                Bucket='fullstack-be-repo',
                Body=contents_list[idx],
                Key=image_name,
                ContentType=file.content_type,
            )
            imageUrls.append(
                "https://{0}.s3.ap-northeast-2.amazonaws.com/".format(
                    'fullstack-be-repo'
                )
                + image_name
            )
    except Exception as e:
        print(e)
        return []
    return imageUrls