from dotenv import load_dotenv
import grpc
from src.pb import service_pb2
from src.pb.service_pb2_grpc import GetTrackLocalServiceStub
from google.protobuf.json_format import MessageToDict

def get_grpc_channel() -> GetTrackLocalServiceStub:
        load_dotenv()
        # channel = grpc.insecure_channel(f"{os.getenv["GRPC_SERVER_IP"]}:{os.getenv["GRPC_SERVER_PORT"]}")
        channel = grpc.insecure_channel("localhost:4040")
        stub = GetTrackLocalServiceStub(channel)
        return stub


def get_trackLocal():
        client = get_grpc_channel()
        client.GetTrackLocal(service_pb2.Request())



class GrpcClient(object):
        def __init__(self):
                self.channel = grpc.insecure_channel("localhost:4040")
                self.stub = GetTrackLocalServiceStub(self.channel)

        def get_trackLocals(self):
                try:
                        stub = self.stub.GetTrackLocal(service_pb2.Request())
                        return MessageToDict(
                                stub,
                                preserving_proto_field_name=True,
                        )
                except grpc.RpcError as rpc_error:
                        return {"error": rpc_error.details()}