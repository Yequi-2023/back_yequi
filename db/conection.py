"""Conexion BD"""
import psycopg2

def get_db():
    """Conexion bd carretera"""
    conn = psycopg2.connect(
        host='localhost',
        database = 'yequi',
        user='postgres',
        password='123456'
    )
    return conn

def get_close_db(conn):
    """Cierre de conexion"""
    conn.close()
