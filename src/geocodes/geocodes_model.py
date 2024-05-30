from pydantic import BaseModel


class GeoCodesResponse(BaseModel):
    latitude: float # x
    longitude: float # y