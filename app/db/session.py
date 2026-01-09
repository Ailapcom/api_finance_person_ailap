import psycopg2
from psycopg2 import Error
from app.Configs.config import USER_DB, PASS_DB, HOST_DB, PORT_DB, DATABASE
from app.utils.logger import LoggerApp

logs = LoggerApp()

class ConnectorPostgreSQL():
    '''
    Clase para conexión a BD PostgreSQL
    methods: connect & disconnect
    '''
    def __init__(self):
        self.database = DATABASE
        self.server = HOST_DB
        self.port = PORT_DB
        self.user =  USER_DB
        self.password = PASS_DB
    
    def connect(self):
        try:
            self.conexion = psycopg2.connect(
                host = self.server,
                database = self.database,
                user = self.user,
                password = self.password,
                port = self.port
            )
            self.cursor = self.conexion.cursor()
            logs.login_info('Conexion DB','Conexion abierta')
        except Error as e:
            logs.login_critical('Conexion DB', f'Conexion a BD {e.args}')
    
    def disconnect(self):
        try:
            self.cursor.close()
            self.conexion.close()
            logs.login_info('Conexion BD','Conexion cerrada')
        except Error as e:
            logs.login_critical('Conexion BD',f'Desconexion fallida {e.args}')