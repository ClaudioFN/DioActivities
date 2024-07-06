from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    PROJECT_NAME: str = "Store API do Claudio"
    ROOT_PATH: str = "http://127.0.0.1:8000"
    DATABASE_URL: str
    
    #model_config = SettingsConfigDict(env_file=".env", arbitrary_types_allowed=True)
    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()