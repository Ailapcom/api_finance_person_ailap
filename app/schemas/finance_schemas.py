from pydantic import BaseModel
from datetime import datetime

class IngresoGasto(BaseModel):
    id: int
    user_id: str
    monto: float
    categoria: str | None
    descripcion: str | None
    fecha: datetime
    cuenta: str | None
    tipo: str | None
    fecha_registro: datetime

class Pendientes(BaseModel):
    id: int
    user_id: str
    monto: float
    concepto: str | None
    descripcion: str | None
    fecha_vencimiento: datetime
    prioridad: str
    recurrente: bool | None
    estatus: str
    fecha_registro: datetime

class Transferencias(BaseModel):
    id: int
    user_id: str
    monto: float
    cuenta_origen: str
    cuenta_destino: str
    descripcion: str | None
    fecha: datetime
    fecha_registro: datetime