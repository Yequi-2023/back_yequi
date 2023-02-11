"""Routes"""
from fastapi import APIRouter
from schemas.login import CapturaDatos, CapturaDatos2, LoginUsuario, Mostrar
from schemas.transferencia import Captura_transferencia, Realizar_tranfer
from schemas.pagos import Captura_pago, Realizar_pago
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

@mi_api_router.post("/transfer")
async def view_datos(transferencia: Captura_transferencia):
    try:
        rta_mostrar = Realizar_tranfer(transferencia)
        informacion = rta_mostrar.ejecutar_transfer()
        if informacion == []:
            raise ExceptionCustumizada('')
        else:
            return informacion
    except ExceptionCustumizada:
        return "transferencia fallida"

@mi_api_router.post("/pagos")
async def view_datos(pago: Captura_pago):
    try:
        rta_mostrar = Realizar_pago(pago)
        informacion = rta_mostrar.ejecutar_pago()
        if informacion == []:
            raise ExceptionCustumizada('')
        else:
            return informacion
    except ExceptionCustumizada:
        return "Pago fallido"