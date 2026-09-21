#--------------------Ejercicio propuesto:------------------------
# Clase SelectorRango que: 
# (1) tenga método crear_rango(inicio, fin) que retorne una tupla con 
# números en ese rango; 
# (2) tenga método elementos_en_multiples_rangos(*rangos) que reciba 
# múltiples tuplas (inicio,fin) y retorne una lista combinada sin duplicados usando un conjunto.

#-----------------------------EPS---------------------------------
#Entrada:
#pares (inicio, fin) para varios rangos
#Proceso:
#crear cada rango como tupla; juntar todos los números en un conjunto (elimina duplicados)
#Salida:
#lista de números únicos

#-----------------------bosquejo----------------------------------
# BOSQUEJO (traza de elementos_en_multiples_rangos((1,3), (2,4))):
# crear_rango(1,3) -> range(1,4) -> (1,2,3)
# crear_rango(2,4) -> range(2,5) -> (2,3,4)
#
# combinado (set, vacío al inicio): {}
# de (1,2,3): agrega 1 -> {1}; agrega 2 -> {1,2}; agrega 3 -> {1,2,3}
# de (2,3,4): agrega 2 -> ya existe, no cambia; agrega 3 -> ya existe; agrega 4 -> {1,2,3,4}
#
# resultado: [1, 2, 3, 4]
#----------------------Codigo--------------------------------------------------

class SelectorRango:
    def crear_rango(self, inicio, fin):
        numeros = []
        for n in range(inicio, fin + 1):   # +1 porque range no incluye el último número
            numeros.append(n)
        return tuple(numeros)

    def elementos_en_multiples_rangos(self, *rangos):
        combinado = set()
        for inicio, fin in rangos:
            rango_actual = self.crear_rango(inicio, fin)
            for numero in rango_actual:
                combinado.add(numero)
        return list(combinado)


sr = SelectorRango()
print(sr.crear_rango(1, 3))
print(sr.elementos_en_multiples_rangos((1,3), (2,4)))