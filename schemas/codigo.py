"""codigo usuario"""
from pydantic import BaseModel
from db.conection import get_db, get_close_db

class Codigos(BaseModel):
    """Captura datos del pago"""
    usuario: int
    codigo: int
    contrasena: str

class Codigo_retiro():
    """Clase para realizar el pago directamente"""
    def __init__(self, modelo: Codigos):
        self.usuario=modelo.usuario
        self.codigo=modelo.codigo
        self.contrasena=modelo.contrasena

    def validar_contrasena(self):
        conn = get_db()
        cursor = conn.cursor()
        query = f"""SELECT public.tbl_usuarios.pass
                FROM public.tbl_usuarios
                WHERE public.tbl_usuarios.pass= '{self.contrasena}' AND public.tbl_usuarios.pk_id_celular='{self.usuario}'"""
        cursor.execute(query)
        result = cursor.fetchall()
        get_close_db(conn)
        return result

    def enviar_codigo(self):
        conn = get_db()
        cursor = conn.cursor()
        query = "UPDATE public.tbl_usuarios	SET codigo={} WHERE pk_id_celular={} AND pass='{}';".format(self.codigo,self.usuario,self.contrasena)
        cursor.execute(query)
        conn.commit()
        get_close_db(conn)
        return "Codigo generado"