#intento 1...
#--------------------Ejercicio propuesto:------------------------
# Clase ControlAforo que:

# Tenga método agregar_capacidad(sala, capacidad) que guarde en un diccionario.
# Tenga método ocupar_espacio(sala, cantidad) que disminuya la capacidad y retorne True si 
# hay suficiente espacio.
# Tenga método salas_con_espacio(minimo) que retorne una lista de salas con capacidad >= mínimo.
#-----------------------------EPS---------------------------------
#Entrada:
#nombre de sala, capacidad/cantidad
#Proceso:
#guardar/actualizar en diccionario; validar antes de restar; filtrar por mínimo
#Salida:
#True/False al ocupar espacio, lista de salas con espacio suficiente

#-----------------------bosquejo----------------------------------
# BOSQUEJO (traza de agregar_capacidad + ocupar_espacio):
# agregar_capacidad("Auditorio",120) -> aforo={"Auditorio":120}
# agregar_capacidad("SalaB",40)      -> aforo={"Auditorio":120,"SalaB":40}
#
# ocupar_espacio("Auditorio",90): "Auditorio" está, 120>=90? Sí
#                                -> aforo["Auditorio"] = 120-90 = 30 -> aforo={"Auditorio":30,"SalaB":40}
#                                -> retorna True
#
# salas_con_espacio(30) -> recorre con .items():
# "Auditorio" capacidad=30 | 30>=30? Sí -> entra
# "SalaB"     capacidad=40 | 40>=30? Sí -> entra
# resultado: ["Auditorio", "SalaB"]
#----------------------Codigo--------------------------------------------------
class ControlAforo:
    def __init__(self):
        self.aforo = {}

    def agregar_capacidad(self, sala, capacidad):
        self.aforo[sala] = capacidad

    def ocupar_espacio(self, sala, cantidad):
        if sala in self.aforo and self.aforo[sala] >= cantidad:
            self.aforo[sala] -= cantidad
            return True
        return False

    def salas_con_espacio(self, minimo):
        resultado = []
        for sala, capacidad in self.aforo.items():
            if capacidad >= minimo:
                resultado.append(sala)
        return resultado


ca = ControlAforo()
ca.agregar_capacidad("Auditorio", 120)
ca.agregar_capacidad("SalaB", 40)
print(ca.ocupar_espacio("Auditorio", 90))
print(ca.salas_con_espacio(30))