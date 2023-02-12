"""Pagos"""
from pydantic import BaseModel
from db.conection import get_db, get_close_db

class Captura_pago(BaseModel):
    """Captura datos del pago"""
    usuario: int
    referencia: int
    monto: int
    descripcion: str
    tipoRecaudo: int

class Realizar_pago():
    """Clase para realizar el pago directamente"""
    def __init__(self, modelo: Captura_pago):
        self.monto=modelo.monto
        self.descripcion=modelo.descripcion
        self.usuario=modelo.usuario
        self.referencia=modelo.referencia
        self.tipoRecaudo=modelo.tipoRecaudo

    def tipo_pago(self):
        """Listar servicios publicos"""
        conn = get_db()
        cursor = conn.cursor()
        query = f"""SELECT public.tbl_tipo_recaudos.pk_id_tipo_recaudo
                FROM public.tbl_tipo_recaudos"""
        cursor.execute(query)
        result = cursor.fetchall()
        get_close_db(conn)
        return result

    def validar_saldo(self):
        """Listar servicios publicos"""
        conn = get_db()
        cursor = conn.cursor()
        query = f"""SELECT public.tbl_usuarios.pk_id_celular,public.tbl_usuarios.saldo
                FROM public.tbl_usuarios
                WHERE public.tbl_usuarios.pk_id_celular= '{self.usuario}'"""
        cursor.execute(query)
        result = cursor.fetchall()
        get_close_db(conn)
        return result

    def ejecutar_pago(self):
        conn = get_db()
        cursor = conn.cursor()
        query = "INSERT INTO public.tbl_recaudos (monto,descripcion,referencia,fk_id_usuario,fk_id_tipo_recaudo) VALUES({},'{}',{},{},{})".format(self.monto,self.descripcion,self.referencia,self.usuario,self.tipoRecaudo)
        cursor.execute(query)
        conn.commit()
        get_close_db(conn)
        return {
            "status": 200,
            "results":{ },
            "msg":"Pago exitoso"
        }