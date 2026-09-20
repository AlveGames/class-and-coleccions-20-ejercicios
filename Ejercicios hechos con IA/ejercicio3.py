#--------------------Ejercicio propuesto:------------------------
# Clase CarroCompras que: 
# (1) tenga método agregar_articulo(nombre, precio) que guarde en un diccionario {nombre: precio}; 
# (2) tenga método total_carrito() que retorne la suma de todos los precios; 
# (3) tenga método articulos_por_rango(precio_min, precio_max) que retorne una lista con artículos dentro del rango.
#-----------------------------EPS---------------------------------
#Entrada:
#nombres de artículos y precios
#Proceso:
#guardar en diccionario, sumar valores, filtrar por rango
#Salida:
#total, artículos en rango

#-----------------------bosquejo----------------------------------
# BOSQUEJO (traza de agregar_articulo en orden):
# Paso 1 | nombre="Pan"    | precio=1.50 | self.articulos={"Pan":1.50}
# Paso 2 | nombre="Leche"  | precio=2.00 | self.articulos={"Pan":1.50,"Leche":2.00}
# Paso 3 | nombre="Arroz"  | precio=3.50 | self.articulos={"Pan":1.50,"Leche":2.00,"Arroz":3.50}
# Paso 4 | nombre="Huevos" | precio=5.00 | self.articulos={..., "Huevos":5.00}
# Paso 5 | nombre="Aceite" | precio=7.00 | self.articulos={..., "Aceite":7.00}
#
# total_carrito() = 1.50+2.00+3.50+5.00+7.00 = 19.0
#
# articulos_por_rango(2, 5) -> recorre con .items():
# nombre="Pan"    precio=1.50 | 1.50 >= 2? No  -> no entra
# nombre="Leche"  precio=2.00 | 2 >= 2 and 2 <= 5? Sí -> entra
# nombre="Arroz"  precio=3.50 | Sí -> entra
# nombre="Huevos" precio=5.00 | 5 <= 5? Sí -> entra
# nombre="Aceite" precio=7.00 | 7 <= 5? No -> no entra
# resultado = ["Leche", "Arroz", "Huevos"]
#----------------------Codigo--------------------------------------------------
class CarroCompras:
    def __init__(self):
        self.articulos = {}

    def agregar_articulo(self, nombre, precio):
        self.articulos[nombre] = precio

    def total_carrito(self):
        return sum(self.articulos.values())

    def articulos_por_rango(self, precio_min, precio_max):
        resultado = []

        for nombre,precio in self.articulos.items():
            if precio >= precio_min and precio <= precio_max:
                resultado.append(nombre)
        return resultado

        
carrito = CarroCompras()

carrito.agregar_articulo("Pan", 1.50)
carrito.agregar_articulo("Leche", 2.00)
carrito.agregar_articulo("Arroz", 3.50)
carrito.agregar_articulo("Huevos", 5.00)
carrito.agregar_articulo("Aceite", 7.00)

print("Total:", carrito.total_carrito())

print("Artículos entre $2 y $5:", carrito.articulos_por_rango(2, 5))