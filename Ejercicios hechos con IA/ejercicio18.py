#--------------------Ejercicio propuesto:------------------------
# Clase CalculadorDistancia que: 
# (1) tenga método distancia_euclidiana(p1, p2) que reciba dos 
# tuplas (x,y) y calcule la distancia; 
# (2) tenga método punto_mas_cercano(referencia, *puntos) 
# que retorne el punto más cercano a referencia; 
# (3) tenga un atributo lista para guardar todas las distancias calculadas.

#-----------------------------EPS---------------------------------
#Entrada:
#tuplas (x, y) que representan puntos
#Proceso:
#calcular la distancia con la fórmula euclidiana; comparar para encontrar el punto más cercano
#Salida:
#un número decimal (la distancia), el punto más cercano; guarda historial en una lista

#-----------------------bosquejo----------------------------------
# BOSQUEJO (traza de distancia_euclidiana((0,0), (3,4))):
# dx = p1[0]-p2[0] = 0-3 = -3
# dy = p1[1]-p2[1] = 0-4 = -4
# distancia = (dx**2 + dy**2) ** 0.5 = ((-3)**2 + (-4)**2) ** 0.5 = (9+16)**0.5 = 25**0.5 = 5.0
#
# resultado: 5.0
#----------------------Codigo--------------------------------------------------

class CalculadorDistancia:
    def __init__(self):
        self.distancias = []

    def distancia_euclidiana(self, p1, p2):
        dx = p1[0] - p2[0]
        dy = p1[1] - p2[1]
        distancia = (dx**2 + dy**2) ** 0.5   # ** 0.5 es la raíz cuadrada
        self.distancias.append(distancia)
        return distancia

    def punto_mas_cercano(self, referencia, *puntos):
        mejor_punto = None
        mejor_distancia = float('inf')   # punto de partida "infinito", cualquier distancia real es menor
        for punto in puntos:
            d = self.distancia_euclidiana(referencia, punto)
            if d < mejor_distancia:
                mejor_distancia = d
                mejor_punto = punto
        return mejor_punto


cd = CalculadorDistancia()
print(cd.distancia_euclidiana((0,0), (3,4)))