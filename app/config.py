
from pydantic_settings import BaseSettings
import os

dotenv_path = os.getenv("DOTENVPATH") #store this in local(pc) environment variable

class Settings(BaseSettings):
    database_hostname:str
    database_port:str
    database_password:str
    database_name:str
    database_username:str
    secret_key:str
    algorithm:str
    access_token_expire_minutes:int

    class Config:
        env_file = dotenv_path

settings = Settings()