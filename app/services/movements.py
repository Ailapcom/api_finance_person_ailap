from fastapi import HTTPException, status
from app.schemas.finance_schemas import IngresoGasto, Pendientes, Transferencias
from app.crud.movements_crud import add_ie, add_pendientes, add_transfers

class MovesServices:
    '''
    Servicio para manejar el registro de movimientos del usuario
    '''
    def create_ie(self, ie_in : IngresoGasto):
        result = add_ie(ie_in)
        return result
    
    def create_pendings(self, obj_pend : Pendientes):
        result = add_pendientes(obj_pend)
        return result
    
    def create_transfers(self, obj_transfer : Transferencias):
        result = add_transfers(obj_transfer)
        return result
    