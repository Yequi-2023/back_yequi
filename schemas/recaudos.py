"""Pagos"""
from pydantic import BaseModel
from db.conection import get_db, get_close_db

class Captura_recaudo(BaseModel):
    """Captura datos del pago"""
    usuario: int
    referencia: int
    monto: int
    descripcion: str
    tipo_recaudo: int

class Realizar_recaudo():
    """Clase para realizar el pago directamente"""
    def __init__(self, modelo: Captura_recaudo):
        self.monto=modelo.monto
        self.descripcion=modelo.descripcion
        self.usuario=modelo.usuario
        self.referencia=modelo.referencia
        self.recaudo=modelo.tipo_recaudo

    def ejecutar_recaudo(self):
        conn = get_db()
        cursor = conn.cursor()
        query = "INSERT INTO tbl_recaudos (monto,descripcion,fk_id_usuario,fk_id_tipo_recaudo,referencia) VALUES({},'{}',{},{},{})".format(self.monto,self.descripcion,self.usuario,self.recaudo,self.referencia)
        cursor.execute(query)
        conn.commit()
        get_close_db(conn)
        return {
            "status": 200,
            "results":{ },
            "msg":"Pago exitoso"
        }