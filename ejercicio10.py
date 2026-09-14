#Clase Tareas que: 
# (1) tenga método agregar_tarea(descripcion, prioridad) que guarde en una lista de tuplas (descripción, prioridad); 
# (2) tenga método tareas_prioritarias() que retorne solo las de prioridad alta; 
# (3) tenga método eliminar_completada(descripcion) que borre la tarea de la lista.


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