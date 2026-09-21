#intento1
#--------------------Ejercicio propuesto:------------------------
# Clase GestorHorarios que:

# Tenga método crear_intervalo(inicio, fin) que retorne una tupla con las horas en ese rango.
# Tenga método horas_ocupadas(*intervalos) que reciba múltiples tuplas (inicio,fin) y retorne 
# una lista combinada sin duplicados usando un conjunto.
#-----------------------------EPS---------------------------------
#Entrada:
#pares (inicio, fin) para varios intervalos de horas
#Proceso:
#crear cada intervalo como tupla; juntar todas las horas en un conjunto (sin duplicados)
#Salida:
#lista de horas únicas
#-----------------------bosquejo----------------------------------
# BOSQUEJO (traza de horas_ocupadas((9,11), (10,13), (18,19))):
# crear_intervalo(9,11)  -> range(9,12)  -> (9,10,11)
# crear_intervalo(10,13) -> range(10,14) -> (10,11,12,13)
# crear_intervalo(18,19) -> range(18,20) -> (18,19)
#
# combinado (set, vacío): {}
# de (9,10,11):      agrega 9,10,11 -> {9,10,11}
# de (10,11,12,13):  agrega 10(ya existe),11(ya existe),12,13 -> {9,10,11,12,13}
# de (18,19):        agrega 18,19 -> {9,10,11,12,13,18,19}
#
# resultado (ordenado): [9, 10, 11, 12, 13, 18, 19]
#----------------------Codigo--------------------------------------------------
class GestorHorarios:
    def crear_intervalo(self, inicio, fin):
        horas = []
        for h in range(inicio, fin + 1):
            horas.append(h)
        return tuple(horas)

    def horas_ocupadas(self, *intervalos):
        combinado = set()
        for inicio, fin in intervalos:
            for h in self.crear_intervalo(inicio, fin):
                combinado.add(h)
        return sorted(list(combinado))


gh = GestorHorarios()
print(gh.crear_intervalo(14, 16))
print(gh.horas_ocupadas((9, 11), (10, 13), (18, 19)))