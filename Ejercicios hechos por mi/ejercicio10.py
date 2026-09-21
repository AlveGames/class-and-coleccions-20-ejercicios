#intento1
#--------------------Ejercicio propuesto:------------------------
# Clase ListaCompras que:

# Tenga método agregar_item(nombre, urgente) que guarde en una lista de tuplas (nombre, urgente).
# Tenga método items_urgentes() que retorne solo los items marcados como urgentes.
# Tenga método quitar_comprado(nombre) que borre el item de la lista.
#-----------------------------EPS---------------------------------
#Entrada:
#nombre del artículo y si es urgente (True/False)
#Proceso:
#guardar como tuplas en una lista; filtrar los urgentes; buscar y eliminar por nombre
#Salida:
#lista de items urgentes

#-----------------------bosquejo----------------------------------
# BOSQUEJO (traza de agregar_item en orden):
# ("Aceite de cocina", True) -> items=[("Aceite de cocina", True)]
# ("Cuadernos", False)       -> items=[..., ("Cuadernos", False)]
# ("Pilas AA", True)         -> items=[..., ("Pilas AA", True)]
#
# items_urgentes() -> recorre la lista, item[1]==True?
# ("Aceite de cocina", True) -> Sí -> entra
# ("Cuadernos", False)       -> No -> no entra
# ("Pilas AA", True)         -> Sí -> entra
# resultado: [("Aceite de cocina", True), ("Pilas AA", True)]
#
# quitar_comprado("Pilas AA"): busca item[0]=="Pilas AA", lo encuentra, .remove(), break
# items queda: [("Aceite de cocina", True), ("Cuadernos", False)]
#----------------------Codigo--------------------------------------------------
class ListaCompras:
    def __init__(self):
        self.items = []

    def agregar_item(self, nombre, urgente):
        self.items.append((nombre, urgente))

    def items_urgentes(self):
        resultado = []
        for item in self.items:
            if item[1] == True:
                resultado.append(item)
        return resultado

    def quitar_comprado(self, nombre):
        for item in self.items:
            if item[0] == nombre:
                self.items.remove(item)
                break


lc = ListaCompras()
lc.agregar_item("Aceite de cocina", True)
lc.agregar_item("Cuadernos", False)
lc.agregar_item("Pilas AA", True)
print(lc.items_urgentes())

lc.quitar_comprado("Pilas AA")
print(lc.items)