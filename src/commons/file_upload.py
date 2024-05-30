from typing import List
import uuid
import boto3
from fastapi import UploadFile


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