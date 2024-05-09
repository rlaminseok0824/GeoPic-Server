from nest.core import Module
from .articles_controller import ArticlesController
from .articles_service import ArticlesService


@Module(
    controllers=[ArticlesController],
    providers=[ArticlesService],
    imports=[]
)   
class ArticlesModule:
    pass

    