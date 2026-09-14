class CarroCompras:
    def __init__(self):
        self.diccionario = {} 

    def agregar_articulo(self,nombre, precio):
        self.diccionario[nombre] = precio

    def total_carrito(self):
        return sum(self.diccionario.values())

    def articulos_por_rango(self,precio_min, precio_max):
        return art = range[self.precio_min,self.precio_max]