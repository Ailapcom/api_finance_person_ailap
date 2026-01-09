from dotenv import load_dotenv
from pathlib import Path
from app.utils.logger import LoggerApp
from pydantic_settings import BaseSettings
from typing import List
import os

try:
    logs = LoggerApp()
    logs.login_info('Importacion variables','Importando variables')
    root = Path().cwd()
    root_env = Path(f'{root}/app/.env').absolute()
    load_dotenv(root_env)
    DATABASE = os.environ['database']
    USER_DB = os.environ['user_db']
    PASS_DB = os.environ['password_db']
    HOST_DB = os.environ['host_db']
    PORT_DB = os.environ['port_db']
    logs.login_info('Importacion variables', 'Variables importadas')
except KeyError as e:
    logs.login_critical('Importacion variables',f'Importacion de variables {e.args}')


class Settings(BaseSettings):
    PROJECT_NAME: str = 'Finance API'
    ENVIRONMENT : str = "development"
    DEBUG : bool = True
    API_V1_STR : str = "/api/v1"

    ALLOWED_ORIGINS : List[str] = [
        "http://localhost:3000",
        "http://localhost:5173",
        "http://localhost:8080",
        "http://127.0.0.1:5500"
    ]

settings = Settings()