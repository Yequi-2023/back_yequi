"""Routes"""
from fastapi import APIRouter
from schemas.login import CapturaDatos
from schemas.login import CapturaDatos2
from schemas.login import LoginUsuario
from schemas.login import Mostrar
import json

mi_api_router = APIRouter(
    prefix="/mi_api"
)

class ExceptionCustumizada(Exception):
    "Excepcion tipo no existe"

@mi_api_router.post("/login")
async def view_login(user: CapturaDatos):
    """Acceso"""
    try:
        rta_login = LoginUsuario(user)
        informacion = rta_login.validacion()
        if informacion == []:
            raise ExceptionCustumizada('')
        else:
            return informacion
    except ExceptionCustumizada:
        return "error"
    
@mi_api_router.post("/mostrar_datos")
async def view_datos(usuario: CapturaDatos2):
    """Acceso"""
    try:
        rta_mostrar = Mostrar(usuario)
        informacion = rta_mostrar.mostrar_informacion()
        if informacion == []:
            raise ExceptionCustumizada('')
        else:
            respuesta = []
            for registro in informacion:
                objeto = {
                    "saldo": registro[0],
                    "nombre": registro[1]
                }
                respuesta.append(objeto)
            return json.loads(json.dumps(respuesta))
    except ExceptionCustumizada:
        return "El usuario no existe"