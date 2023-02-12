"""Pagos"""
from pydantic import BaseModel
from db.conection import get_db, get_close_db

class Captura_recaudo(BaseModel):
    """Captura datos del pago"""
    monto: int
    descripcion: str
    referencia: int
    usuario: int
    tipo_recaudo: int

class Realizar_recaudo():
    """Clase para realizar el pago directamente"""
    def __init__(self, modelo: Captura_recaudo):
        self.monto=modelo.monto
        self.descripcion=modelo.descripcion
        self.referencia=modelo.referencia
        self.usuario=modelo.usuario
        self.tipoRecaudo=modelo.tipo_recaudo

    def tipo_pago(self):
        """Listar servicios publicos"""
        conn = get_db()
        cursor = conn.cursor()
        query = f"""SELECT public.tbl_tipo_recaudos.pk_id_tipo_recaudo
                FROM public.tbl_tipo_recaudos
                WHERE public.tbl_tipo_recaudos.pk_id_tipo_recaudo='{self.tipoRecaudo}'"""
        cursor.execute(query)
        result = cursor.fetchall()
        get_close_db(conn)
        return result

    def validar_saldo(self):
        """Validar saldo"""
        conn = get_db()
        cursor = conn.cursor()
        query = f"""SELECT public.tbl_usuarios.pk_id_celular,public.tbl_usuarios.saldo
                FROM public.tbl_usuarios
                WHERE public.tbl_usuarios.pk_id_celular='{self.usuario}' AND (public.tbl_usuarios.saldo >= '{self.monto}')"""
        cursor.execute(query)
        result = cursor.fetchall()
        get_close_db(conn)
        return result

    def ejecutar_recaudo(self):
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