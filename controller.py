from db_dietas import database_name
import sqlite3
from model import Restriccion
import os
os.system ("cls")

def get_db():
    conn=sqlite3.connect (database_name)
    return conn

def select_dietas():
    db = get_db()
    cursor = db.cursor()
    statement= "SELECT codigo, restriccion_ing, restriccion_esp, stock, vencimiento, valor_usd FROM Dietas"
    cursor.execute (statement)
    lista_dietas= cursor.fetchall()

    lista_restricciones=[]

    for row in lista_dietas:
        codigo=row[0]
        restriccion_ing=row[1]
        restriccion_esp=row[2]
        stock= row[3]
        vencimiento = row[4]
        valor_usd=row[5]

        objeto_restriccion = Restriccion(codigo, restriccion_esp, restriccion_ing, stock, vencimiento, valor_usd)
        lista_restricciones.append (objeto_restriccion)
    db.close()
    return lista_restricciones

def insertar_dietas(objeto_restriccion):
    db = get_db()
    cursor = db.cursor()

    objeto = objeto_restriccion
    statement = """INSERT OR IGNORE INTO Dietas (codigo, restriccion_ing, restriccion_esp, stock, vencimiento, valor_usd) 
                                           VALUES (?, ?, ?, ? ,?, ?)"""
    cursor.execute (statement, [objeto.codigo, objeto.restriccion_ing, objeto.restriccion_esp, objeto.stock, objeto.vencimiento, objeto.valor_usd])
    db.commit()
    db.close()

def get_one_dieta(restr_codigo):
    db = get_db()
    cursor=db.cursor()
    query= "SELECT codigo, restriccion_ing, restriccion_esp, stock, vencimiento, valor_usd FROM Dietas WHERE codigo =  '" + restr_codigo + "'" 
    cursor.execute(query)

    row=cursor.fetchone()
    if row == None:
        return []
    
    codigo=row[0]
    restriccion_ing=row[1]
    restriccion_esp=row[2]
    stock= row[3]
    vencimiento = row[4]
    valor_usd=row[5]

    objeto_restriccion = Restriccion(codigo, restriccion_ing, restriccion_esp, stock, vencimiento, valor_usd)
    db.close()
    return objeto_restriccion