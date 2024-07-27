from flask import Flask, jsonify, request
from controller import select_dietas, insertar_dietas, get_one_dieta
from db_dietas import create_table
from model import Restriccion
from x_rate import get_xr

app =Flask ( __name__)
create_table()

@app.route ("/", methods=["GET"])
def home():
    return "Bienvenidos"

@app.route ("/dietas", methods=["GET"])
def mostrar_dietas():
    lista_dietas = select_dietas()
    return jsonify ([restr.serialize() for restr in lista_dietas])
if __name__ == '__main__':
    app.run()

@app.route ("/post/dietas", methods=["POST"])
def crear_dieta():
    data = request.get_json()

    codigo = data ["codigo"]
    restriccion_ing = data ["restriccion_ing"]
    restriccion_esp = data ["restriccion_esp"]
    stock = data ["stock"]
    vencimiento = data ["vencimiento"]
    valor_usd = data ["valor_usd"]
    objeto_restriccion = Restriccion(codigo,restriccion_ing,restriccion_esp,stock,vencimiento,valor_usd)
    insertar_dietas(objeto_restriccion)
    
    return jsonify (objeto_restriccion.serialize ())

@app.route ("/dietas/<codigo>/pais/<pais>", method = ["GET"])
def select_dieta_por_pais(restr_codigo, pais):
    restr = get_one_dieta(restr_codigo)

    if restr == []:
        return jsonify (status= 400, description= "Codigo de dieta no valido.")
    
    texto_eng = restr.restriccion_ing
    valor_usd = int(restr.valor_usd)
    rta = "The value of ", texto_eng, "es", str(valor_usd)

    if pais == "ARG":
        texto_esp = restr.restriccion_esp
        dolar = get_xr()
        valor_pesos = valor_usd * dolar
        rta = "El valor de " , texto_esp, "es", str(valor_pesos)

    return jsonify (status=200, description = rta),200