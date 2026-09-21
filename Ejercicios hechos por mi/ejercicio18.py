#intento 1...
#--------------------Ejercicio propuesto:------------------------
# Clase ComparadorPrecios que:

# Tenga método diferencia_precio(precio1, precio2) que calcule la diferencia absoluta entre 
# dos precios.
# Tenga método precio_mas_cercano(referencia, *precios) que retorne el precio más cercano a 
# la referencia.
# Tenga un atributo lista para guardar todas las diferencias calculadas.
#-----------------------------EPS---------------------------------
#Entrada:
#precios (números)
#Proceso:
#calcular diferencia absoluta entre precios; comparar para encontrar la menor diferencia
#Salida:
#número (la diferencia), el precio más cercano

#-----------------------bosquejo----------------------------------
# BOSQUEJO (traza de precio_mas_cercano(250, 180, 310, 265)):
# mejor=None, menor_diferencia=infinito
# precio=180 | diferencia_precio(250,180)=abs(250-180)=70 | 70<inf? Sí -> menor_diferencia=70, mejor=180
# precio=310 | diferencia_precio(250,310)=abs(250-310)=60 | 60<70? Sí -> menor_diferencia=60, mejor=310
# precio=265 | diferencia_precio(250,265)=abs(250-265)=15 | 15<60? Sí -> menor_diferencia=15, mejor=265
#
# resultado: 265 (el precio más cercano a 250)
# self.diferencias = [50, 70, 60, 15]  (incluye la llamada suelta anterior + las 3 del bucle)
#----------------------Codigo--------------------------------------------------
class ComparadorPrecios:
    def __init__(self):
        self.diferencias = []

    def diferencia_precio(self, precio1, precio2):
        d = abs(precio1 - precio2)
        self.diferencias.append(d)
        return d

    def precio_mas_cercano(self, referencia, *precios):
        mejor = None
        menor_diferencia = float('inf')
        for p in precios:
            d = self.diferencia_precio(referencia, p)
            if d < menor_diferencia:
                menor_diferencia = d
                mejor = p
        return mejor


cp = ComparadorPrecios()
print(cp.diferencia_precio(250, 300))
print(cp.precio_mas_cercano(250, 180, 310, 265))
print(cp.diferencias)