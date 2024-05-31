from dotenv import load_dotenv
from nest.core import Controller, Get, Post
from .app_service import AppService
from .pb import service_pb2
from .pb.service_pb2_grpc import GetTrackLocalServiceStub
import grpc
import os
from google.protobuf.json_format import MessageToDict



@Controller("/")
class AppController:
    def _get_grpc_channel(self) -> GetTrackLocalServiceStub:
        load_dotenv()
        channel = grpc.insecure_channel(f"{os.getenv["GRPC_SERVER_IP"]}:{os.getenv["GRPC_SERVER_PORT"]}")
        stub = GetTrackLocalServiceStub(channel)
        return stub

    def __init__(self, service: AppService):
        self.service = service

    @Get("/")
    def get_app_info(self):
        return self.service.get_app_info()
    
    @Get("/track_ids")
    async def get_track_ids(self):
        try:
            client = self._get_grpc_channel()
            stub = client.GetTrackLocal(service_pb2.Request())
            
            return MessageToDict(
                stub,
                preserving_proto_field_name=True,
            )
        except Exception as e:
            return {"error": str(e)}
