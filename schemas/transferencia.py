"""Transferencia"""
from pydantic import BaseModel
from db.conection import get_db, get_close_db

class Captura_transferencia(BaseModel):
    """Captura datos de la transferencia"""
    usuario_origen: int
    usuario_destino: int
    monto: int
    descripcion: str

class Realizar_tranfer():
    """Clase para realizar la transferencia directamente"""
    def __init__(self, modelo: Captura_transferencia):
        self.monto=modelo.monto
        self.descripcion=modelo.descripcion
        self.usuario_origen=modelo.usuario_origen
        self.usuario_destino=modelo.usuario_destino

    def exista_cuenta(self):
        """Validar que existe cuenta origen"""
        conn = get_db()
        cursor = conn.cursor()
        query = f"""SELECT public.tbl_usuarios.pk_id_celular
                FROM public.tbl_usuarios
                WHERE public.tbl_usuarios.pk_id_celular='{self.usuario_destino}'"""
        cursor.execute(query)
        result = cursor.fetchall()
        get_close_db(conn)
        return result

    def validar_saldo(self):
        """Validar si tiene saldo superarior a la transferencia"""
        conn = get_db()
        cursor = conn.cursor()
        query = f"""SELECT public.tbl_usuarios.pk_id_celular,public.tbl_usuarios.saldo
                FROM public.tbl_usuarios
                WHERE public.tbl_usuarios.pk_id_celular='{self.usuario_origen}' AND (public.tbl_usuarios.saldo >= '{self.monto}')"""
        cursor.execute(query)
        result = cursor.fetchall()
        get_close_db(conn)
        return result
        
    def ejecutar_transfer(self):
        conn = get_db()
        cursor = conn.cursor()
        query = "INSERT INTO public.tbl_transferencias (monto,descripcion,fk_id_usuario_origen,fk_id_usuario_detino) VALUES({},'{}',{},{})".format(self.monto,self.descripcion,self.usuario_origen,self.usuario_destino)
        cursor.execute(query)
        conn.commit()
        get_close_db(conn)
        return {
            "status": 200,
            "results":{ },
            "msg":"Transaccion exitosa"
        }