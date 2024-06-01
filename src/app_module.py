from nest.core import PyNestFactory, Module

from src.geocodes.geocodes_moudle import GeoModule
from src.live_streams.live_stream_module import LiveStreamModule
from .config import config
from .app_controller import AppController
from .app_service import AppService
from src.articles.articles_module import ArticlesModule


@Module(imports=[ArticlesModule, GeoModule, LiveStreamModule], controllers=[AppController], providers=[AppService])
class AppModule:
    pass


app = PyNestFactory.create(
    AppModule,
    description="This is my Async PyNest app.",
    title="PyNest Application",
    version="1.0.0",
    debug=True,
)
http_server = app.get_server()


@http_server.on_event("startup")
async def startup():
    await config.create_all()
