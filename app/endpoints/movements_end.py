from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse

from app.services.movements import MovesServices
from app.schemas.finance_schemas import IngresoGasto, Pendientes, Transferencias

router = APIRouter()

@router.post(
    "/ingreso-gasto",
    status_code=status.HTTP_201_CREATED,
    summary="Registrar Ingreso o gasto"
)
def create_ingreso_gasto(
    ie_in: IngresoGasto,
    moves_services: MovesServices = Depends()
):
    '''
    Docstring para create_ingreso_gasto
    
    :param ie_in: Descripción
    :type ie_in: IngresoGasto
    '''
    result = moves_services.create_ie(ie_in)
    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content= {
            'message' : 'Transación registrada exitosamente',
            'status' : 'success',
            'data' : result,
            'metadata' : {
                'tipo_registrado' : ie_in.tipo,
                'monto' : ie_in.monto
            }
        }
    )

@router.post(
    "/pendiente",
    status_code=status.HTTP_201_CREATED,
    summary= "Regitrar pagos pendientes"
)
def create_pendiente(
    obj_pend : Pendientes,
    pend_services : MovesServices = Depends()
):
    '''
    Docstring para create_pendiente
    
    :param obj_pend: Descripción
    :type obj_pend: Pendientes
    :param pend_services: Descripción
    :type pend_services: MovesServices
    '''
    result =  pend_services.create_pendings(obj_pend)
    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content={
            'message' : 'Pendiente agregado con éxito',
            'status' : 'success',
            'data' : result,
            'metadata' : {
                'prioridad' : obj_pend.prioridad,
                'recurrente' : obj_pend.recurrente,
                'monto' : obj_pend.monto
            }
        }
    )

@router.post(
    "/transferencia",
    status_code= status.HTTP_201_CREATED,
    summary="Registrar transferencias realizadas"
)
def create_transfer(
    obj_transfer : Transferencias,
    transfer_services : MovesServices = Depends()
):
    '''
    Docstring para create_transfer
    
    :param obj_transfer: Descripción
    :type obj_transfer: Transferencias
    :param transfer_services: Descripción
    :type transfer_services: MovesServices
    '''
    return transfer_services.create_transfers(obj_transfer)