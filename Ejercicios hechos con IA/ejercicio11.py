#--------------------Ejercicio propuesto:------------------------
# Clase ContadorFrecuencia que: 
# (1) tenga método agregar_elemento(elemento) que guarde en un 
# diccionario contando repeticiones; 
# (2) tenga método elemento_mas_frecuente() que retorne el 
# elemento con mayor frecuencia; 
# (3) tenga método frecuencia_elemento(elemento) que retorne 
# cuántas veces aparece.

#-----------------------------EPS---------------------------------
#Entrada:
#elementos individuales o en lote
#Proceso:
#guardar en diccionario contando repeticiones; buscar el de mayor cantidad
#Salida:
#elemento más frecuente, y cuántas veces aparece uno en específico

#-----------------------bosquejo----------------------------------
# BOSQUEJO (traza de agregar_elemento en orden: "a", "b", "a"):
# agregar_elemento("a") -> "a" no está en conteo -> conteo={"a":1}
# agregar_elemento("b") -> "b" no está en conteo -> conteo={"a":1,"b":1}
# agregar_elemento("a") -> "a" SÍ está en conteo -> conteo={"a":2,"b":1}
#
# elemento_mas_frecuente() -> recorre con .items():
# elemento="a" cantidad=2 | 2>0?  Sí -> mejor_cantidad=2, mejor_elemento="a"
# elemento="b" cantidad=1 | 1>2?  No -> no cambia
# resultado: "a"
#
# frecuencia_elemento("a") = conteo.get("a", 0) = 2
#----------------------Codigo--------------------------------------------------

class ContadorFrecuencia:
    def __init__(self):
        self.conteo = {}

    def agregar_elemento(self, elemento):
        if elemento in self.conteo:
            self.conteo[elemento] += 1
        else:
            self.conteo[elemento] = 1

    def elemento_mas_frecuente(self):
        mejor_elemento = None
        mejor_cantidad = 0
        for elemento, cantidad in self.conteo.items():
            if cantidad > mejor_cantidad:
                mejor_cantidad = cantidad
                mejor_elemento = elemento
        return mejor_elemento

    def frecuencia_elemento(self, elemento):
        return self.conteo.get(elemento, 0)


cf = ContadorFrecuencia()
cf.agregar_elemento("a")
cf.agregar_elemento("b")
cf.agregar_elemento("a")
print(cf.elemento_mas_frecuente())
print(cf.frecuencia_elemento("a"))