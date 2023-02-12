"""historial"""
from db.conection import get_db, get_close_db

class Realizar_historial():
    """Clase para realizar el pago directamente"""
    def __init__(self, modelo: int):
        self.usuario=modelo

    def ejecutar_historial(self):
        conn = get_db()
        cursor = conn.cursor()
        query = "SELECT cuenta_origen, descripcion, monto, cuenta_destino FROM tbl_historiales WHERE cuenta_origen={} OR cuenta_destino={} ;".format(self.usuario,self.usuario)
        cursor.execute(query)
        result = cursor.fetchall()
        get_close_db(conn)
        return {
            "status": 200,
            "results":{"historial": result,
                 },
            "msg":"Historial exitoso"
        }