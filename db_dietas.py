import sqlite3
from model import Restriccion

database_name="DreamFly.db"

def get_db():
    conn= sqlite3.connect(database_name)
    return conn

def create_table():
    statement= """CREATE TABLE IF NOT EXISTS Dietas (
                codigo TEXT PRIMARY KEY,
                restriccion_ing TEXT NOT NULL,
                restriccion_esp TEXT NOT NULL,
                stock INTEGER NOT NULL,
                vencimiento TEXT NOT NULL,
                valor_usd INTEGER NOT NULL
            )"""

    db=get_db()
    cursor = db.cursor()
    cursor.execute(statement)

def data_inicial():
    db=get_db()
    cursor = db.cursor()
    statement = """INSERT OR IGNORE INTO Dietas (codigo, restriccion_ing, restriccion_esp, stock, vencimiento, valor_usd) 
                                               VALUES (?, ?, ?, ? ,?, ?)"""
    codigo='R001'
    restriccion_ing= 'Gluten-free'
    restriccion_esp= 'Libre de Gluten'
    stock =350
    vencimiento= '12/08/2024'
    valor_usd= 100
    cursor.execute (statement, [codigo, restriccion_ing, restriccion_esp, stock, vencimiento, valor_usd])
    
    codigo='R002'
    restriccion_ing= 'Dairy-free'
    restriccion_esp= 'Libre de Lacteos'
    stock =240
    vencimiento= '24/07/2024'
    valor_usd= 112
    cursor.execute (statement, [codigo, restriccion_ing, restriccion_esp, stock, vencimiento, valor_usd])
    db.commit()
    db.close()

create_table()
data_inicial()