"""codigo usuario"""
from pydantic import BaseModel
from db.conection import get_db, get_close_db

class Referencias(BaseModel):
    """Captura captura la referencia y el codigo de servicio"""
    referencia: int
    convenio: int

class Referencia_pago():
    """A partir de esta clase se valida si la referencia existe"""
    def __init__(self, modelo: Referencias):
        self.referencia=modelo.referencia
        self.convenio=modelo.convenio

    def validar_referencia(self):
        conn = get_db()
        cursor = conn.cursor()
        query = f"""SELECT public.tbl_recibos.monto
                FROM public.tbl_recibos
                WHERE public.tbl_recibos.pk_id_recibo= '{self.referencia}' AND public.tbl_recibos.fk_id_tipo_recaudo='{self.convenio}'"""
        cursor.execute(query)
        result = cursor.fetchall()
        get_close_db(conn)
        return result
