"""codigo servicio"""
from pydantic import BaseModel
from db.conection import get_db, get_close_db

class Creditos(BaseModel):
    """Captura captura la referencia y el codigo de servicio"""
    referencia: int

class Referencia_credito():
    """A partir de esta clase se valida si la referencia existe"""
    def __init__(self, modelo: Creditos):
        self.referencia=modelo.referencia

    def validar_referencia(self):
        conn = get_db()
        cursor = conn.cursor()
        query = f"""SELECT public.tbl_creditos.monto
                FROM public.tbl_creditos
                WHERE public.tbl_creditos.pk_id_credito= '{self.referencia}'"""
        cursor.execute(query)
        result = cursor.fetchall()
        get_close_db(conn)
        return result