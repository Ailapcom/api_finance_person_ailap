from app.utils.logger import LoggerApp
from pydantic_settings import BaseSettings
from typing import List
from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import List
from pydantic import Field

class Settings(BaseSettings):
    '''Se definen las variables de entorno pydantic tomará el .env'''
    DATABASE: str = Field(validation_alias="database")
    USER_DB: str = Field(validation_alias="user_db")
    PASS_DB: str = Field(validation_alias="password_db")
    HOST_DB: str = Field(validate_default="host_db")
    PORT_DB: str = Field(validation_alias="port_db")
    
    PROJECT_NAME: str = 'Finance API'
    ENVIRONMENT: str = "development"
    DEBUG: bool = True
    API_V1_STR: str = "/api/v1"

    # Configuración para permitir todos los orígenes
    ALLOWED_ORIGINS: List[str] = ["*"]

    # Esta es la "magia" de Pydantic para cargar el .env automáticamente
    model_config = SettingsConfigDict(
        env_file=("app/.env", ".env"), 
        env_file_encoding="utf-8",
        extra="ignore" # Ignora variables extras que no estén definidas arriba
    )

try:
    settings = Settings()
    # Si quieres mantener tus logs
    logs = LoggerApp()
    logs.login_info('Importacion variables', 'Variables importadas correctamente')
except Exception as e:
    print(f"Error cargando configuración: {e}")