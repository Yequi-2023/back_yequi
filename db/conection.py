"""Conexion BD"""
import psycopg2

def get_db():
    """Conexion bd carretera"""
    conn = psycopg2.connect(
        host='localhost',
        database = 'yequinuevo',
        user='postgres',
<<<<<<< HEAD
        password='admin'
=======
        password='123456789'
>>>>>>> 03e55f0fe8a19db63935278cae46520e9375c7ed
    )
    return conn

def get_close_db(conn):
    """Cierre de conexion"""
    conn.close()
