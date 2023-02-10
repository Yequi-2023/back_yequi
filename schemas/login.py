"""Login"""
from pydantic import BaseModel
from db.conection import get_db,get_close_db

class CapturaDatos(BaseModel):
    """Captura datos"""
    usuario: int
    contrasena: str

class LoginUsuario:
    """Login usuario"""
    def __init__(self, model: CapturaDatos):
        self.usuario = model.usuario
        self.contrasena = model.contrasena

    def validacion(self):
        """Validar si existe usuario"""
        conn = get_db()
        cursor = conn.cursor()
        query = f"""SELECT public.tbl_usuario.nombre_usuario
            FROM public.tbl_usuario
            WHERE telefono = '{self.usuario}' AND password = '{self.contrasena}'"""
        cursor.execute(query)
        result = cursor.fetchall()
        get_close_db(conn)
        return result
        
