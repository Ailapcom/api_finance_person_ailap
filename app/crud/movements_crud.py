from app.utils.logger import LoggerApp
from app.db.session import ConnectorPostgreSQL
from fastapi import HTTPException, status

logs = LoggerApp()

def add_ie(ie_obj):
    query = '''
        INSERT INTO public.ingresos_egresos (id, user_id, monto, categoria, descripcion, fecha, cuenta, tipo, fecha_registro)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
    '''
    try:
        sql = ConnectorPostgreSQL()
        logs.login_info(process = 'Add IE', text = 'Agregando IE')
        sql.connect()
        sql.cursor.execute(
            query,
            (ie_obj.id,
            ie_obj.user_id,
            ie_obj.monto,
            ie_obj.categoria,
            ie_obj.descripcion,
            ie_obj.fecha,
            ie_obj.cuenta,
            ie_obj.tipo,
            ie_obj.fecha_registro)
        )
        sql.conexion.commit()
        logs.login_info('Add IE','IE agregado')
        return True
    except Exception as e:
        logs.login_error('Add IE', f'Agrando IE {e.args}')
        sql.conexion.rollback()
        return None
    finally:
        sql.disconnect()

def add_pendientes(obj_pend):
    logs.login_info('Add Pendings', 'Agregando pendientes')
    query = '''
        INSERT INTO public.pendientes (id, user_id, monto, concepto, descripcion, fecha_vencimiento, prioridad, recurrente, estatus, fecha_registro)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
    '''
    try:
        sql = ConnectorPostgreSQL()
        sql.connect()
        sql.cursor.execute(query,
                           (obj_pend.id,
                            obj_pend.user_id,
                            obj_pend.monto,
                            obj_pend.concepto,
                            obj_pend.descripcion,
                            obj_pend.fecha_vencimiento,
                            obj_pend.prioridad,
                            obj_pend.recurrente,
                            obj_pend.estatus,
                            obj_pend.fecha_registro))
        sql.conexion.commit()
        logs.login_info('Add Pendings', 'Pendiente agregado con exito')
        return True
    except Exception as e:
        logs.login_error('Add Pendings', f'Agregando pendiente {e.args}')
        sql.conexion.rollback()
        return None
    finally:
        sql.disconnect()

def add_transfers(obj_transfer):
    logs.login_info('Add Transfer', 'Agregando transferencias')
    query = '''
        INSERT INTO public.transferencias (id, user_id, monto, cuenta_origen, cuenta_destino, descripcion, fecha, fecha_registro)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
    '''
    try:
        sql = ConnectorPostgreSQL()
        sql.connect()
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
        logs.login_info('Add Transfer', 'Transferencia agregada con exito')
        return True
    except Exception as e:
        logs.login_error('Add Transfer', f'Al guardar transferencia {e.args}')
        return None
    finally:
        sql.disconnect()


# def get_movements(user_id : str):
#     logs.login_info('Obteniendo Movimientos')
#     query = f'''
#         SELECT

#         FROM public.ingresos_egresos AS I
#         INEER 
#     '''