from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPExcption
from app.utils.logger import LoggerApp
import time

from app.routers.finance_router import api_router
from app.Configs.config import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    description="API para la gestión de finanzas personales",
    version="1.0.0",
    openapi_url=f'{settings.API_V1_STR}/openapi.json',
    docs_url='/docs',
    redoc_url='/redoc'
)

app.add_middleware(
    CORSMiddleware,
    allow_origins = settings.ALLOWED_ORIGINS,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)

app.include_router(api_router, prefix=settings.API_V1_STR)

@app.get("/", tags=["root"])
def root():
    """Endpoint raíz de la API"""
    return {
        "message": f"Bienvenido a {settings.PROJECT_NAME}",
        "version": "1.0.0",
        "environment": settings.ENVIRONMENT,
        "docs": "/docs",
        "redoc": "/redoc"
    }

@app.get("/health", tags=["health"])
def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "environment": settings.ENVIRONMENT,
        "api_version": "1.0.0"
    }

@app.get("/info", tags=["info"])
def api_info():
    """Información de la API"""
    return {
        "name": settings.PROJECT_NAME,
        "version": "1.0.0",
        "environment": settings.ENVIRONMENT
    }


if __name__ == "__main__":
    import uvicorn
    logs = LoggerApp()
    logs.login_info('Inicio APP', 'Iniciando API')
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=settings.DEBUG,
        log_level="info"
    )