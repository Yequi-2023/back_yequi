"""Login"""
from pydantic import BaseModel
from db.conection import get_db, get_close_db


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
        query = f"""SELECT public.tbl_usuarios.pk_id_celular, public.tbl_usuarios.nombre, public.tbl_usuarios.pass, public.tbl_usuarios.email, 
            public.tbl_usuarios.saldo, public.tbl_usuarios.rol
            FROM public.tbl_usuarios
            WHERE public.tbl_usuarios.pk_id_celular = '{self.usuario}' AND public.tbl_usuarios.pass = '{self.contrasena}'"""
        cursor.execute(query)
        result = cursor.fetchall()
        get_close_db(conn)
        return {
            "status": 200,
            "results":{
                "cuenta": result[0][0],
                "name": result[0][1],
                "pass": result[0][2],
                "email": result[0][3],
                "saldo": result[0][4],
                "rol":result[0][5]
            },
            "msg":"Peticion correcta"
        }

class CapturaDatos2(BaseModel):
    """Captura datos"""
    usuario: int

class Mostrar():
    def __init__(self, model: CapturaDatos2):
        self.usuario = model.usuario

    def mostrar_informacion(self):
        """Validar si existe usuario"""
        conn = get_db()
        cursor = conn.cursor()
        query = f"""SELECT public.tbl_usuarios.saldo, public.tbl_usuarios.nombre
                FROM public.tbl_usuarios
                WHERE public.tbl_usuarios.pk_id_celular= '{self.usuario}'"""
        cursor.execute(query)
        result = cursor.fetchall()
        get_close_db(conn)
        return result
    
def mostrar_servicios_publicos():
        """VListar servicios publicos"""
        conn = get_db()
        cursor = conn.cursor()
        query = f"""SELECT public.tbl_tipo_recaudos.nombre_convenio
                FROM public.tbl_tipo_recaudos"""
        cursor.execute(query)
        result = cursor.fetchall()
        get_close_db(conn)
        return result