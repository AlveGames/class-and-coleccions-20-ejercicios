#intento1
#--------------------Ejercicio propuesto:------------------------
# Clase GestorVelocidades que:

# Tenga método registrar_velocidad(velocidad) 
# que guarde en una lista, solo si la velocidad es mayor a 0 (descarta negativos o cero).
# Tenga métodos minima(), maxima(), promedio().
# Tenga método registrar_multiples(*velocidades) que reutilice el registro.
#-----------------------------EPS---------------------------------
#Entrada:
#velocidades individuales o en lote
#Proceso:
#validar que sea mayor a 0 antes de guardar; calcular mínima, máxima y promedio
#Salida:
#lista filtrada (sin negativos ni cero), y valores estadísticos (mín, máx, promedio)

#-----------------------bosquejo----------------------------------
# BOSQUEJO (traza de registrar_multiples(80, -5, 120, 0, 95)):
# velocidad=80  | 80 > 0? Sí  | self.velocidad=[80]
# velocidad=-5  | -5 > 0? No  | self.velocidad=[80]         (no cambia)
# velocidad=120 | 120 > 0? Sí | self.velocidad=[80,120]
# velocidad=0   | 0 > 0? No   | self.velocidad=[80,120]     (no cambia)
# velocidad=95  | 95 > 0? Sí  | self.velocidad=[80,120,95]
#
# minima()  = min([80,120,95]) = 80
# maxima()  = max([80,120,95]) = 120
# promedio()= sum([80,120,95]) / len([80,120,95]) = 295/3 = 98.33
#----------------------Codigo--------------------------------------------------
class GestorVelocidades:

    def __init__(self):
        self.velocidad = []

    def registrar_velocidad(self,velocidad):
        if velocidad > 0:
            self.velocidad.append(velocidad)


    def minima(self):
        return min(self.velocidad)

    def maxima(self):
        return max(self.velocidad)

    def promedio(self):
        return sum(self.velocidad)/len(self.velocidad)

    def registrar_multiples(self, *temps):
            for temp in temps:
                self.registrar_velocidad(temp)

g = GestorVelocidades()
g.registrar_multiples(80, -5, 120, 0, 95)
print(g.minima())
print(g.maxima())
print(g.promedio())

#comentario:
#es casi igual que el ejercicio 1