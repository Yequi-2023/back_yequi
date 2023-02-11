"""Pagos"""
from pydantic import BaseModel
from db.conection import get_db, get_close_db

class Captura_pago(BaseModel):
    """Captura datos del pago"""
    usuario: int
    referencia: int
    monto: int
    descripcion: str

class Realizar_pago():
    """Clase para realizar el pago directamente"""
    def __init__(self, modelo: Captura_pago):
        self.monto=modelo.monto
        self.descripcion=modelo.descripcion
        self.usuario=modelo.usuario
        self.referencia=modelo.referencia

    def ejecutar_pago(self):
        conn = get_db()
        cursor = conn.cursor()
        query = "INSERT INTO tbl_pagos (monto,descripcion,referencia_pago,fk_id_usuario) VALUES({},'{}',{},{})".format(self.monto,self.descripcion,self.referencia,self.usuario)
        cursor.execute(query)
        conn.commit()
        get_close_db(conn)
        return {
            "status": 200,
            "results":{ },
            "msg":"Pago exitoso"
        }