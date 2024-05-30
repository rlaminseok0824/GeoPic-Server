import os
from dotenv import load_dotenv
from nest.core import Injectable

from httpx import AsyncClient

from src.geocodes.geocodes_model import GeoCodesResponse

load_dotenv()

@Injectable
class GeoService:
    base_url = "https://naveropenapi.apigw.ntruss.com/map-geocode/v2/geocode"
    naver_client_id = os.getenv("NAVER_CLIENT_ID")
    naver_client_secret = os.getenv("NAVER_CLIENT_SECRET")
    client = AsyncClient()
  
    def set_header(self):
        headers = {
            "X-NCP-APIGW-API-KEY-ID": self.naver_client_id,
            "X-NCP-APIGW-API-KEY": self.naver_client_secret,
        }
        
        return headers



    async def get_geocodes_from_location(self,  location: str):
        response = await self.client.get(self.base_url, headers=self.set_header(),params={
            "query": location
        })
        response_json = response.json()
        return GeoCodesResponse(
            latitude=response_json["addresses"][0]["x"]
            ,longitude=response_json["addresses"][0]["y"]
        )