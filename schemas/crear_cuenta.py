"""Crear cuenta"""
from pydantic import BaseModel
from db.conection import get_db, get_close_db

class CapturaDatos3(BaseModel):
    """Captura datos"""
    nombre: str
    email: str
    celular: int
    contraseña:str
    rol:str

class CrearUsuario():
    def __init__(self, model: CapturaDatos3):
        self.nombre = model.nombre
        self.email = model.email
        self.celular = model.celular
        self.contraseña = model.contraseña
        self.rol = model.rol

    def crear_usuario(self):
        """Crear nueva cuenta usuario"""
        conn = get_db()
        cursor = conn.cursor()

        query= f"""INSERT INTO public.tbl_usuarios (pk_id_celular,nombre,pass,email,saldo,rol) 
                VALUES ({self.celular},'{self.nombre}','{self.contraseña}','{self.email}',0,'{self.rol}')"""

        #print(query)
        cursor.execute(query)
        conn.commit()
        #result = cursor.fetchall()
        get_close_db(conn)


        conn = get_db()
        cursor = conn.cursor()
        query = f"""SELECT public.tbl_usuarios.pk_id_celular
            FROM public.tbl_usuarios
            WHERE public.tbl_usuarios.pk_id_celular = '{self.celular}'"""
        cursor.execute(query)
        result = cursor.fetchall()
        get_close_db(conn)
        return result
        