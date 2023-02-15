"""Conexion BD"""
import psycopg2

def get_db():
    """Conexion bd carretera"""
    conn = psycopg2.connect(
        host='localhost',
        database = 'yequinuevo',
        user='postgres',
        password='admin'
    )
    return conn

def get_close_db(conn):
    """Cierre de conexion"""
    conn.close()
