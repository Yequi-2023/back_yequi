"""Routes"""
from fastapi import APIRouter
from schemas.login import CapturaDatos, CapturaDatos2, LoginUsuario, Mostrar, LoginCorresponsal
from schemas.transferencia import Captura_transferencia, Realizar_tranfer
from schemas.pagos import Captura_pago, Realizar_pago
from schemas.crear_cuenta import CapturaDatos3, CrearUsuario
from schemas.recaudos import Captura_recaudo, Realizar_recaudo
from schemas.retiros import Captura_retiro, Realizar_retiro
from schemas.historial import Realizar_historial
from schemas.codigo import Codigo_retiro, Codigos
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


@mi_api_router.post("/loginCorresponsal")
async def view_login_corresponsal(user: CapturaDatos):
    """Acceso"""
    try:
        rta_login = LoginCorresponsal(user)
        informacion = rta_login.validacion_corresponsal()
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


@mi_api_router.post("/transferencia")
async def view_datos(transferencia: Captura_transferencia):
    try:
        rta_mostrar = Realizar_tranfer(transferencia)
        validaciones = rta_mostrar.exista_cuenta()
        if validaciones != []:
            informacion_usuario = rta_mostrar.validar_saldo()
            if informacion_usuario != []:
                informacion = rta_mostrar.ejecutar_transfer()
                return informacion
        else:
            raise ExceptionCustumizada('')
    except ExceptionCustumizada:
        return "Cuenta destino no existe"


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
            return {
                "status": 200,
                "results": "Cuenta con celular "+str(informacion[0][0])+" creada correctamente",
                "msg": "Creación exitosa"
            }
    except ExceptionCustumizada:
        return "error"


@mi_api_router.post("/pagos")
async def view_datos(pago: Captura_pago):
    try:
        rta_mostrar = Realizar_pago(pago)
        validaciones = rta_mostrar.validar_saldo()
        if validaciones != []:
            informacion = rta_mostrar.ejecutar_pago()
            return informacion
        else:
            raise ExceptionCustumizada('')
    except ExceptionCustumizada:
        return "Pago fallido"


@mi_api_router.post("/recaudos")
async def view_datos(recaudo: Captura_recaudo):
    try:
        rta_mostrar = Realizar_recaudo(recaudo)
        validaciones = rta_mostrar.tipo_pago()
        if validaciones != []:
            informacion_usuario = rta_mostrar.validar_saldo()
            if informacion_usuario != []:
                informacion = rta_mostrar.ejecutar_recaudo()
                return informacion
        else:
            raise ExceptionCustumizada('')
    except ExceptionCustumizada:
        return "Recaudo Fallido"


@mi_api_router.post("/retiros")
async def view_datos(retiro: Captura_retiro):
    try:
        rta_mostrar = Realizar_retiro(retiro)
        informacion = rta_mostrar.ejecutar_retiro()
        if informacion == []:
            raise ExceptionCustumizada('')
        else:
            return informacion
    except ExceptionCustumizada:
        return "Pago fallido"


@mi_api_router.get("/historial")
async def view_datos(usuario: int):
    try:
        rta_mostrar = Realizar_historial(usuario)
        informacion = rta_mostrar.ejecutar_historial()
        if informacion == []:
            raise ExceptionCustumizada('')
        else:
            return informacion
    except ExceptionCustumizada:
        return "Sin historial para mostrar"

@mi_api_router.post("/Codigo")
async def view_datos(codigo: Codigos):
    try:
        rta_mostrar = Codigo_retiro(codigo)
        validacion = rta_mostrar.validar_contrasena()        
        if validacion == []:
            raise ExceptionCustumizada('')
        else:
            rta_mostrar.enviar_codigo()
            return "Codigo generado"
    except ExceptionCustumizada:
        return "Codigo fallido"
