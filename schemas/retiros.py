"""Pagos"""
from pydantic import BaseModel
from db.conection import get_db, get_close_db

class Captura_retiro(BaseModel):
    """Captura datos del pago"""
    usuario: int
    codigo: int
    monto: int
    usuario_corresponsal: int

class Realizar_retiro():
    """Clase para realizar el pago directamente"""
    def __init__(self, modelo: Captura_retiro):
        self.monto=modelo.monto
        self.usuario=modelo.usuario
        self.referencia=modelo.usuario_corresponsal
        self.codigo=modelo.codigo

    def ejecutar_retiro(self):
        conn = get_db()
        cursor = conn.cursor()
        query2 = "SELECT codigo FROM public.tbl_usuarios WHERE pk_id_celular={} AND codigo={}".format(self.usuario,self.codigo)
        cursor.execute(query2)
        result = cursor.fetchall()
        if len(result)>0:
            print(result[0][0])
            query = "INSERT INTO tbl_retiros (monto,fk_id_usuario,referencia) VALUES({},{},{})".format(self.monto,self.usuario,self.referencia)
            cursor.execute(query)
            conn.commit()
            get_close_db(conn)
            return {
                "status": 200,
                "results":{ },
                "msg":"Retiro exitoso"
            }
        else:
            return {
                "status": 404,
                "results":{ },
                "msg":"Codigo invalido"
            }