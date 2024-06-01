from dotenv import load_dotenv
from nest.core import Controller, Get, Post

from src.commons.grpc import GrpcClient, get_grpc_channel
from .app_service import AppService
from .pb import service_pb2
from .pb.service_pb2_grpc import GetTrackLocalServiceStub
import grpc
import os
from google.protobuf.json_format import MessageToDict



@Controller("/")
class AppController:
    def __init__(self, service: AppService):
        self.service = service

    @Get("/")
    def get_app_info(self):
        return self.service.get_app_info()
    
    @Get("/track_ids")
    async def get_track_ids(self):
        try:
            client = GrpcClient()
            return client.get_trackLocals()
        except Exception as e:
            return {"error": str(e)}
