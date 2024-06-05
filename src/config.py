import os
from dotenv import load_dotenv
from nest.core.database.odm_provider import OdmProvider
from src.articles.articles_entity import Articles
from src.live_streams.live_streams_entity import LiveStreams

load_dotenv()
config = OdmProvider(
    config_params={
        "db_name": os.getenv("DB_NAME", "default_nest_db"),
        "host": os.getenv("DB_HOST", "localhost"),
        "user": os.getenv("DB_USER", "root"),
        "password": os.getenv("DB_PASSWORD", "root"),
        "port": os.getenv("DB_PORT", 27017),
    },
    document_models=[Articles,LiveStreams],
)
