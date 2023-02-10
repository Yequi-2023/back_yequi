"""Routes"""
from fastapi import APIRouter
from schemas.login import CapturaDatos
from schemas.login import LoginUsuario

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
    
