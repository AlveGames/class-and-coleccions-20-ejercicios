#--------------------Ejercicio propuesto:------------------------
# Clase RegistroNotas que: 
# (1) tenga método registrar(estudiante, nota) que guarde en un 
# diccionario; 
# (2) tenga método estudiantes_aprobados(nota_minima) que retorne lista de 
# estudiantes; 
# (3) tenga método mejor_estudiante() que retorne nombre y nota del que tiene 
# mayor calificación.

#-----------------------------EPS---------------------------------
#Entrada:
#nombre del estudiante y su nota
#Proceso:
#guardar en diccionario; filtrar por nota mínima; buscar el de mayor nota
#Salida:
#lista de aprobados, tupla (nombre, nota) del mejor

#-----------------------bosquejo----------------------------------
# BOSQUEJO (traza de registrar en orden):
# registrar("Ana",95) -> notas={"Ana":95}
# registrar("Bob",70) -> notas={"Ana":95,"Bob":70}
#
# mejor_estudiante() -> recorre con .items():
# estudiante="Ana" nota=95 | 95 > -1? Sí -> mejor_nota=95, mejor_nombre="Ana"
# estudiante="Bob" nota=70 | 70 > 95? No -> no cambia
#
# resultado: ("Ana", 95)
#----------------------Codigo--------------------------------------------------

class RegistroNotas:
    def __init__(self):
        self.notas = {}

    def registrar(self, estudiante, nota):
        self.notas[estudiante] = nota

    def estudiantes_aprobados(self, nota_minima):
        resultado = []
        for estudiante, nota in self.notas.items():
            if nota >= nota_minima:
                resultado.append(estudiante)
        return resultado

    def mejor_estudiante(self):
        mejor_nombre = None
        mejor_nota = -1   # -1 porque ninguna nota real es negativa; así la primera siempre "gana"
        for estudiante, nota in self.notas.items():
            if nota > mejor_nota:
                mejor_nota = nota
                mejor_nombre = estudiante
        return (mejor_nombre, mejor_nota)


rn = RegistroNotas()
rn.registrar("Ana", 95)
rn.registrar("Bob", 70)
print(rn.estudiantes_aprobados(75))
print(rn.mejor_estudiante())