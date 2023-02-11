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

    def ejecutar_transfer(self):
        conn = get_db()
        cursor = conn.cursor()
        query = "INSERT INTO tbl_transferencias (monto,descripcion,fk_id_usuario_origen,fk_id_usuario_detino) VALUES({},'{}',{},{})".format(self.monto,self.descripcion,self.usuario_destino,self.usuario_origen)
        cursor.execute(query)
        conn.commit()
        get_close_db(conn)
        return {
            "status": 200,
            "results":{ },
            "msg":"Transaccion exitosa"
        }