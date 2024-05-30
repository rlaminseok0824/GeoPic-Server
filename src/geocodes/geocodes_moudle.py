from nest.core import Module
from .geocodes_controller import GeoController
from .geocodes_service import GeoService


@Module(
    controllers=[GeoController],
    providers=[GeoService],
    imports=[]
)   
class GeoModule:
    pass

    