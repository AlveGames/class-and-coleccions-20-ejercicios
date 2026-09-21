#intento 1...
#--------------------Ejercicio propuesto:------------------------
# Clase Inventario que:

# Tenga método crear_categoria(nombre_categoria) que inicie la categoría como lista vacía en un diccionario.
# Tenga método agregar_producto(categoria, producto) que añada el producto a esa categoría.
# Tenga método categoria_menos_productos() que retorne el nombre de la categoría 
# con menos productos (lo opuesto: mínimo, no máximo).
#-----------------------------EPS---------------------------------
#Entrada:
#nombres de categorías y productos
#Proceso:
#crear estructura categoria→[productos], contar, comparar para encontrar la mínima cantidad
#Salida:
#categoría con menos productos
#-----------------------bosquejo----------------------------------
# BOSQUEJO (traza de categoria_menos_productos()):
# self.categorias = {"alimentos":["kinoa","manzana","rabano"], "electronicos":["rtx 5070"], "fontaneria":["teflon","tubo 3m"]}
#
# nombre_producto=None | menos_productos=1000000
# categoria="alimentos"    | len(producto)=3 | 3<1000000? Sí -> menos_productos=3, nombre_producto="alimentos"
# categoria="electronicos" | len(producto)=1 | 1<3?       Sí -> menos_productos=1, nombre_producto="electronicos"
# categoria="fontaneria"   | len(producto)=2 | 2<1?       No -> no cambia
#
# resultado: "electronicos"
#----------------------Codigo--------------------------------------------------
class Inventario:
    def __init__(self):
        self.categorias = {}

    def crear_categoria(self,nombre_categoria):
        self.categorias[nombre_categoria] = []

    def agregar_producto(self,categoria, producto):
        self.categorias[categoria].append(producto)

    def categoria_menos_productos(self):
        nombre_producto = None
        menos_productos = 50
        for categoria, producto in self.categorias.items():
            if len(producto) < menos_productos:
                menos_productos = len(producto)
                nombre_producto = categoria
        return nombre_producto

products = Inventario()

products.crear_categoria("alimentos")
products.crear_categoria("electronicos")
products.crear_categoria("fontaneria")
products.agregar_producto("alimentos","kinoa")
products.agregar_producto("alimentos","manzana")
products.agregar_producto("alimentos","rabano")
products.agregar_producto("electronicos","rtx 5070")
products.agregar_producto("fontaneria","teflon")
products.agregar_producto("fontaneria","tubo 3m")
print(products.categoria_menos_productos())