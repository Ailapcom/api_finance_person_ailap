from pydantic import BaseModel,Field
from datetime import datetime

class IngresoGasto(BaseModel):
    id: int = Field(..., description="Id generado de forma aleatoria para identificar el movimiento", example = 875412415121)
    user_id: str = Field(..., description="Id alfanumérico que identifica al usuario que genera el movimiento", example = "AE123454JGE" )
    monto: float = Field(..., description = "Valor monetario de la transacción", example = 150.52)
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