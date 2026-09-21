#--------------------Ejercicio propuesto:------------------------
# Clase Tareas que: (1) tenga método agregar_tarea(descripcion, prioridad) que guarde en una 
# lista de tuplas (descripción, prioridad); (2) tenga método tareas_prioritarias() que retorne 
# solo las de prioridad alta; (3) tenga método eliminar_completada(descripcion) que borre la tarea de la lista.

#-----------------------------EPS---------------------------------
#Entrada:
#descripción y prioridad de cada tarea
#Proceso:
#guardar como tuplas en una lista; filtrar las de prioridad "alta"; buscar y eliminar por descripción
#Salida:
#lista de tareas con prioridad alta

#-----------------------bosquejo----------------------------------
# BOSQUEJO (traza de agregar_tarea en orden):
# agregar_tarea("Estudiar","alta") -> tareas=[("Estudiar","alta")]
# agregar_tarea("Leer","baja")     -> tareas=[("Estudiar","alta"), ("Leer","baja")]
#
# tareas_prioritarias() -> recorre la lista:
# tarea=("Estudiar","alta") | tarea[1]=="alta"? Sí -> entra
# tarea=("Leer","baja")     | tarea[1]=="alta"? No -> no entra
# resultado: [("Estudiar","alta")]
#
# eliminar_completada("Leer"):
# tarea=("Estudiar","alta") | tarea[0]=="Leer"? No
# tarea=("Leer","baja")     | tarea[0]=="Leer"? Sí -> se elimina, se corta el for con break
# tareas queda: [("Estudiar","alta")]
#----------------------Codigo--------------------------------------------------

class Tareas:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, descripcion, prioridad):
        self.tareas.append((descripcion, prioridad))

    def tareas_prioritarias(self):
        resultado = []
        for tarea in self.tareas:
            if tarea[1] == "alta":
                resultado.append(tarea)
        return resultado

    def eliminar_completada(self, descripcion):
        for tarea in self.tareas:
            if tarea[0] == descripcion:
                self.tareas.remove(tarea)
                break


t = Tareas()
t.agregar_tarea("Estudiar", "alta")
t.agregar_tarea("Leer", "baja")
print(t.tareas_prioritarias())

t.eliminar_completada("Leer")
print(t.tareas)