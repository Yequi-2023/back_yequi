"""Routes"""
from fastapi import APIRouter
<<<<<<< HEAD
from schemas.login import CapturaDatos, CapturaDatos2, LoginUsuario, Mostrar
from schemas.transferencia import Captura_transferencia, Realizar_tranfer
from schemas.pagos import Captura_pago, Realizar_pago
=======
from schemas.login import CapturaDatos
from schemas.login import CapturaDatos2
from schemas.crear_cuenta import CapturaDatos3
from schemas.login import LoginUsuario
from schemas.login import Mostrar
from schemas.crear_cuenta import CrearUsuario
>>>>>>> e673e78020639e9a0a19244ac3269b5dfc9242f6
import json
from schemas.login import mostrar_servicios_publicos

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

<<<<<<< HEAD
@mi_api_router.post("/transfer")
async def view_datos(transferencia: Captura_transferencia):
    try:
        rta_mostrar = Realizar_tranfer(transferencia)
        informacion = rta_mostrar.ejecutar_transfer()
=======
<<<<<<< HEAD
@mi_api_router.post("/crear_usuario")
async def view_crear_usuario(usuario2: CapturaDatos3):
    """Acceso"""
    try:
        rta_login = CrearUsuario(usuario2)
        informacion = rta_login.crear_usuario()
        if informacion == []:
            raise ExceptionCustumizada('')
        else:
        # print (informacion[0][0])
            return "Cuenta con celular "+str(informacion[0][0])+" creada correctamente"
    except ExceptionCustumizada:
        return "error"
=======
@mi_api_router.post("/mostrar_servicios_publicos")
async def view_datos():
    """Acceso"""
    try:
        rta_servicios_publicos= mostrar_servicios_publicos()
        informacion = rta_servicios_publicos
>>>>>>> e673e78020639e9a0a19244ac3269b5dfc9242f6
        if informacion == []:
            raise ExceptionCustumizada('')
        else:
            return informacion
    except ExceptionCustumizada:
<<<<<<< HEAD
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
=======
        return "No existen convenios de servicios publicos"
>>>>>>> 1fc02435dfa9dbe3ec374a61df722226022ea81f
>>>>>>> e673e78020639e9a0a19244ac3269b5dfc9242f6
