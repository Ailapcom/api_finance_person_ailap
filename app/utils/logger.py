import logging
import os
from logging.handlers import RotatingFileHandler, TimedRotatingFileHandler

LOG_DIR = os.getenv('LOG_DIR', '/app/log')
os.makedirs(LOG_DIR, exist_ok=True)

logger = logging.getLogger('api_finance')
logger.setLevel(logging.DEBUG)

# Formato del logger
formato = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(funcName)s:%(lineno)d - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

handler_rotacion = RotatingFileHandler(
    'app_rotacion.log',
    maxBytes=5*1024*1024,
    backupCount=3
)
handler_rotacion.setFormatter(formato)
handler_rotacion.setLevel(logging.INFO)

handler_diario = TimedRotatingFileHandler(
    'app_diario.log',
    when='midnight',
    interval=1,
    backupCount=7
)

handler_diario.setFormatter(formato)
handler_diario.setLevel(logging.WARNING)

logger.addHandler(handler_diario)
logger.addHandler(handler_rotacion)

class LoggerApp():

    def login_error(self, processs : str, text: str):
        logger.error(f'Error en el proceso: {processs} : Detalles : {text}')

    def login_info(self, process : str, text: str):
        logger.info(f'Estatus: {process} : Detalle : {text}')

    def login_warn(self, process : str, text : str):
        logger.warning(f'Revisión en : {process} : Detalle : {text}')

    def login_critical(self, process: str, text : str):
        logger.critical(f'Error critico en: {process} : Detalle : {text}')