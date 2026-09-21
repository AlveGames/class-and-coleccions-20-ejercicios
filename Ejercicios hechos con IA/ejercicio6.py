#--------------------Ejercicio propuesto:------------------------
# Clase GestorTemperatura que: 
# (1) tenga método registrar_temperatura(temp) que guarde en una lista; 
# (2) tenga método minima()`, `maxima()`, `promedio() que calculen estadísticas; 
# (3) tenga método registrar_multiples(*temps) que reutilice el registro para varias temperaturas.
#-----------------------------EPS---------------------------------
#Entrada:
#temperaturas individuales o en lote
#Proceso:
#guardar, calcular mín, máx, promedio
#Salida:
#valores estadísticos
#-----------------------bosquejo----------------------------------
# BOSQUEJO (traza de registrar_multiples(27,25,30,40)):
# temp=27 | self.temperaturas=[27]
# temp=25 | self.temperaturas=[27,25]
# temp=30 | self.temperaturas=[27,25,30]
# temp=40 | self.temperaturas=[27,25,30,40]
#
# minima()  = min([27,25,30,40]) = 25
# maxima()  = max([27,25,30,40]) = 40
#----------------------Codigo--------------------------------------------------
class GestorTemperatura:

    def __init__(self):
        self.temperaturas = []

    def registrar_temperatura(self, temp):
        self.temperaturas.append(temp)

    def minima(self):
        return min(self.temperaturas)

    def maxima(self):
        return max(self.temperaturas)

    def promedio(self):
        return sum(self.temperaturas)/len(self.temperaturas)

    def registrar_multiples(self, *temps):
        for temp in temps:
            self.registrar_temperatura(temp)

temp = GestorTemperatura()

temp.registrar_multiples(27,25,30,40)
print(temp.minima())
print(temp.maxima())
print(temp.promedio())