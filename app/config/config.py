import pathlib
from pydantic_settings import BaseSettings, SettingsConfigDict


class ServerSettings(BaseSettings):
    RABBITMQ_HOST: str
    RABBITMQ_QUEUE: str
    
    BASE_DIR: pathlib.Path = pathlib.Path(__file__).parent.parent
    LOG_LEVEL: str

    model_config = SettingsConfigDict(env_file='.env')

server_settings = ServerSettings()
