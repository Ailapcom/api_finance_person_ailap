from app.utils.logger import LoggerApp
from app.db.session import ConnectorPostgreSQL
from fastapi import HTTPException, status
from typing import Optional

logs = LoggerApp()

def add_ie(ie_obj):
    """Agregar ingreso/egreso"""
    query = '''
        INSERT INTO public.ingresos_egresos 
        (id, user_id, monto, categoria, descripcion, fecha, cuenta, tipo, fecha_registro)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
        RETURNING id
    '''
    sql = ConnectorPostgreSQL()
    
    try:
        logs.login_info(process='Add IE', text='Agregando IE')
        sql.connect()

        if not sql.cursor or not sql.conexion:
            raise Exception("No se pudo establecer conexión con la base de datos")
        
        sql.cursor.execute(query, (ie_obj.id,
                 ie_obj.user_id,
                 ie_obj.monto,
                 ie_obj.categoria,
                 ie_obj.descripcion,
                 ie_obj.fecha,
                 ie_obj.cuenta,
                 ie_obj.tipo,
                 ie_obj.fecha_registro))
        sql.conexion.commit()

        result = sql.cursor.fetchone()
        logs.login_info(process='Add IE',text= 'Registro Insertado correctamete')
        return result
        
    except Exception as e:
        logs.login_error('Add IE', f'Error agregando IE: {str(e)}')
        if sql.conexion:
            sql.conexion.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error al agregar IE: {str(e)}"
        )
    finally:
        if sql.conexion:
            sql.disconnect()


def add_pendientes(obj_pend):
    """Agregar pendiente"""
    query = '''
        INSERT INTO public.pendientes 
        (id, user_id, monto, concepto, descripcion, fecha_vencimiento, prioridad, recurrente, estatus, fecha_registro)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        RETURNING id
    '''
    sql = ConnectorPostgreSQL()
    
    try:
        logs.login_info('Add Pendings', 'Agregando pendiente')
        sql.connect()
        
        if not sql.cursor or not sql.conexion:
            raise Exception("No se pudo establecer conexión con la base de datos")
        
        sql.cursor.execute(
                query,
                (obj_pend.id,
                 obj_pend.user_id,
                 obj_pend.monto,
                 obj_pend.concepto,
                 obj_pend.descripcion,
                 obj_pend.fecha_vencimiento,
                 obj_pend.prioridad,
                 obj_pend.recurrente,
                 obj_pend.estatus,
                 obj_pend.fecha_registro)
            )
        sql.conexion.commit()
        result = sql.cursor.fetchone() 
        logs.login_info('Add Pendings', 'Pendiente agregado con éxito')
        return result
        
    except Exception as e:
        logs.login_error('Add Pendings', f'Error agregando pendiente: {str(e)}')
        if sql.conexion:
            sql.conexion.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error al agregar pendiente: {str(e)}"
        )
    finally:
        if sql.conexion:
            sql.disconnect()


def add_transfers(obj_transfer):
    """Agregar transferencia"""
    query = '''
        INSERT INTO public.transferencias 
        (id, user_id, monto, cuenta_origen, cuenta_destino, descripcion, fecha, fecha_registro)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
        RETURNING id
    '''
    sql = ConnectorPostgreSQL()
    
    try:
        logs.login_info('Add Transfer', 'Agregando transferencia')
        sql.connect()
        if not sql.cursor or not sql.conexion:
            raise Exception("No se pudo establecer conexión con la base de datos")
        
        sql.cursor.execute(
                query,
                (obj_transfer.id,
                 obj_transfer.user_id,
                 obj_transfer.monto,
                 obj_transfer.cuenta_origen,
                 obj_transfer.cuenta_destino,
                 obj_transfer.descripcion,
                 obj_transfer.fecha,
                 obj_transfer.fecha_registro)
            )
        sql.conexion.commit()
        result = sql.cursor.fetchone()     
        logs.login_info('Add Transfer', 'Transferencia agregada con éxito')
        return result
           
    except Exception as e:
        logs.login_error('Add Transfer', f'Error al guardar transferencia: {str(e)}')
        if sql.conexion:
            sql.conexion.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error al agregar transferencia: {str(e)}"
        )
    finally:
        if sql.conexion:
            sql.disconnect()