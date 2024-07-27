class Restriccion:
    def __init__(self,codigo, restriccion_ing, restriccion_esp, stock, vencimiento, valor_usd ) -> None:
        self.codigo = codigo
        self.restriccion_ing = restriccion_ing
        self.restriccion_esp = restriccion_esp
        self.stock = stock
        self.vencimiento = vencimiento
        self.valor_usd = valor_usd

    def serialize (self):
        return{
            "codigo" : self.codigo,\
            "restriccion_ing" : self.restriccion_ing,\
            "restriccion_esp" : self.restriccion_esp,\
            "stock" : self.restriccion_esp,\
            "vencimiento" : self.vencimiento,\
            "valor_usd" :self.valor_usd\
        }

