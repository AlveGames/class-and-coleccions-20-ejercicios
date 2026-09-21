#--------------------Ejercicio propuesto:------------------------
# Clase Inventario que: 
# (1) tenga método agregar_stock(producto, cantidad) que guarde en un diccionario; 
# (2) tenga método restar_stock(producto, cantidad) que disminuya y retorne True si hay suficiente; 
# (3) tenga método productos_bajo_stock(minimo) que retorne una lista de productos con cantidad < minimo.

#-----------------------------EPS---------------------------------
#Entrada:
#nombre de producto y cantidad
#Proceso:
#guardar/actualizar en diccionario; validar si hay suficiente antes de restar; filtrar por mínimo
#Salida:
#True/False al restar, lista de productos bajo el mínimo

#-----------------------bosquejo----------------------------------
# BOSQUEJO (traza de agregar_stock("pan",50) + restar_stock("pan",30) + productos_bajo_stock(15)):
# agregar_stock("pan",50): "pan" no está en stock -> stock={"pan":50}
#
# restar_stock("pan",30): "pan" está en stock, 50>=30? Sí
#                        -> stock["pan"] = 50-30 = 20 -> stock={"pan":20}
#                        -> retorna True
#
# productos_bajo_stock(15): recorre con .items():
# producto="pan" cantidad=20 | 20 < 15? No -> "pan" NO entra
# resultado: []
#
# (el HTML dice que la salida esperada es ["pan"], pero con 20 unidades eso es matemáticamente
#  incorrecto contra un mínimo de 15 -- probablemente un error de quien armó la guía;
#  la lógica de tu código, siguiendo el enunciado literal, es la correcta)
#----------------------Codigo--------------------------------------------------

class Inventario:
    def __init__(self):
        self.stock = {}

    def agregar_stock(self, producto, cantidad):
        if producto in self.stock:
            self.stock[producto] += cantidad
        else:
            self.stock[producto] = cantidad

    def restar_stock(self, producto, cantidad):
        if producto in self.stock and self.stock[producto] >= cantidad:
            self.stock[producto] -= cantidad
            return True
        return False

    def productos_bajo_stock(self, minimo):
        resultado = []
        for producto, cantidad in self.stock.items():
            if cantidad < minimo:
                resultado.append(producto)
        return resultado


inv = Inventario()
inv.agregar_stock("pan", 50)
print(inv.restar_stock("pan", 30))
print(inv.productos_bajo_stock(15))