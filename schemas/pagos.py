"""Pagos"""
from pydantic import BaseModel
from db.conection import get_db, get_close_db

class Captura_pago(BaseModel):
    """Captura datos del pago"""
    monto: int
    descripcion: str
    referencia: int
    usuario: int

class Realizar_pago():
    """Clase para realizar el pago directamente"""
    def __init__(self, modelo: Captura_pago):
        self.monto=modelo.monto
        self.descripcion=modelo.descripcion
        self.referencia=modelo.referencia
        self.usuario=modelo.usuario

    def validar_saldo(self):
        """Validar si tiene saldo superior para el pago"""
        conn = get_db()
        cursor = conn.cursor()
        query = f"""SELECT public.tbl_usuarios.pk_id_celular,public.tbl_usuarios.saldo
                FROM public.tbl_usuarios
                WHERE public.tbl_usuarios.pk_id_celular='{self.usuario}' AND (public.tbl_usuarios.saldo >= '{self.monto}')"""
        cursor.execute(query)
        result = cursor.fetchall()
        get_close_db(conn)
        return result

    def ejecutar_pago(self):
        conn = get_db()
        cursor = conn.cursor()
        query = "INSERT INTO public.tbl_pagos (monto,descripcion,referencia_pago,fk_id_usuario) VALUES({},'{}',{},{})".format(self.monto,self.descripcion,self.referencia,self.usuario)
        cursor.execute(query)
        conn.commit()
        get_close_db(conn)
        return {
            "status": 200,
            "results":{ },
            "msg":"Pago exitoso"
        }