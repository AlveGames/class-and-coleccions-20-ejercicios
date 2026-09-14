class CarroCompras:
    def __init__(self):
        self.diccionario = {}   # diccionario vacío para guardar nombre: precio

    def agregar_articulo(self, nombre, precio):
        self.diccionario[nombre] = precio   # AGREGA una clave, no reemplaza todo

    def total_carrito(self):
        return sum(self.diccionario.values())   # suma solo los VALORES (precios)

    def articulos_por_rango(self, precio_min, precio_max):
        resultado = []   # lista vacía donde guardo los que califican
        for nombre, precio in self.diccionario.items():   # recorro clave y valor juntos
            if precio >= precio_min and precio <= precio_max:
                resultado.append(nombre)   # guardo el NOMBRE, no el precio
        return resultado


# Programa principal
c = CarroCompras()
c.agregar_articulo("pan", 2.50)
c.agregar_articulo("leche", 3.00)
c.agregar_articulo("queso", 8.00)

print(c.total_carrito())                    # 13.5
print(c.articulos_por_rango(2.00, 5.00))    # ['pan', 'leche']