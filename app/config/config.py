import pathlib
from pydantic_settings import BaseSettings, SettingsConfigDict


class ServerSettings(BaseSettings):
    APP_PORT: int
    APP_HOST: str
    
    BASE_DIR = pathlib.Path(__file__).parent.parent
    LOG_LEVEL: str

    model_config = SettingsConfigDict(env_file='.env')

server_setting = ServerSettings()
