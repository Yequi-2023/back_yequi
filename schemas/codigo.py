"""codigo usuario"""
from pydantic import BaseModel
from db.conection import get_db, get_close_db

class Codigos(BaseModel):
    """Captura datos del pago"""
    usuario: int
    codigo: int

class Codigo_retiro():
    """Clase para realizar el pago directamente"""
    def __init__(self, modelo: Codigos):
        self.usuario=modelo.usuario
        self.codigo=modelo.codigo

    def enviar_codigo(self):
        conn = get_db()
        cursor = conn.cursor()
        query = "UPDATE public.tbl_usuarios	SET codigo={} WHERE pk_id_celular={};".format(self.codigo,self.usuario)
        cursor.execute(query)
        conn.commit()
        get_close_db(conn)
        return {
            "status": 200,
            "results":{},
            "msg":"Codigo exitoso"
        }