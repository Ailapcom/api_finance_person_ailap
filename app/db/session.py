import psycopg2
from psycopg2 import Error
from app.Configs.config import settings
from app.utils.logger import LoggerApp

logs = LoggerApp()

class ConnectorPostgreSQL():
    '''
    Clase para conexión a BD PostgreSQL
    methods: connect & disconnect
    '''
    def __init__(self):
        self.database = settings.DATABASE
        self.server = settings.HOST_DB
        self.port = settings.PORT_DB
        self.user = settings.USER_DB
        self.password = settings.PASS_DB
        self.conexion = None  # ← Inicializar en None
        self.cursor = None    # ← Inicializar en None
    
    def connect(self):
        try:
            logs.login_info('Conexion DB', f'Intentando conectar a {self.server}:{self.port}/{self.database}')
            
            self.conexion = psycopg2.connect(
                host=self.server,
                database=self.database,
                user=self.user,
                password=self.password,
                port=self.port
            )
            self.cursor = self.conexion.cursor()
            logs.login_info('Conexion DB', 'Conexion abierta exitosamente')
            return True
            
        except Error as e:
            logs.login_critical('Conexion DB', f'Error conectando a BD: {e.args}')
            self.conexion = None
            self.cursor = None
            raise  # ← CRÍTICO: Re-lanzar la excepción
    
    def disconnect(self):
        try:
            if self.cursor:  # ← Verificar que existe antes de cerrar
                self.cursor.close()
            if self.conexion:  # ← Verificar que existe antes de cerrar
                self.conexion.close()
            logs.login_info('Conexion BD', 'Conexion cerrada')
        except Error as e:
            logs.login_critical('Conexion BD', f'Desconexion fallida {e.args}')
        finally:
            self.cursor = None
            self.conexion = None
    
    def __enter__(self):
        """Para usar con context manager"""
        self.connect()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Cierra automáticamente la conexión"""
        self.disconnect()