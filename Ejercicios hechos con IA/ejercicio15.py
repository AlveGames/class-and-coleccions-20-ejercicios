#--------------------Ejercicio propuesto:------------------------
# Clase DivisorFinder que: 
# (1) tenga método encontrar_divisores(numero) que retorne una tupla 
# con todos los divisores; 
# (2) tenga método es_perfecto(numero) que retorne True si la suma de 
# sus divisores (excepto él mismo) es igual a él; 
# (3) tenga método 
# encontrar_multiples_divisores(*numeros) que retorne un diccionario {número: tupla_divisores}.

#-----------------------------EPS---------------------------------
#Entrada:
#uno o varios números
#Proceso:
#probar cada número del 1 hasta el mismo número, ver cuáles dividen exacto (resto 0 con %)
#Salida:
#tupla de divisores, booleano (si es perfecto), diccionario con varios números

#-----------------------bosquejo----------------------------------
# BOSQUEJO (traza de encontrar_divisores(12)):
# i=1  | 12%1==0?  Sí -> divisores=[1]
# i=2  | 12%2==0?  Sí -> divisores=[1,2]
# i=3  | 12%3==0?  Sí -> divisores=[1,2,3]
# i=4  | 12%4==0?  Sí -> divisores=[1,2,3,4]
# i=5  | 12%5==0?  No
# i=6  | 12%6==0?  Sí -> divisores=[1,2,3,4,6]
# i=7,8,9,10,11 | ninguno divide exacto
# i=12 | 12%12==0? Sí -> divisores=[1,2,3,4,6,12]
# resultado: (1,2,3,4,6,12)
#
# es_perfecto(6): divisores=(1,2,3,6)
# suma (sin contar el 6 mismo) = 1+2+3 = 6
# 6 == 6? Sí -> True (6 es un número perfecto)
#----------------------Codigo--------------------------------------------------

class DivisorFinder:
    def encontrar_divisores(self, numero):
        divisores = []
        for i in range(1, numero + 1):
            if numero % i == 0:
                divisores.append(i)
        return tuple(divisores)

    def es_perfecto(self, numero):
        divisores = self.encontrar_divisores(numero)
        suma = 0
        for d in divisores:
            if d != numero:      # no cuenta el número mismo, solo sus divisores "propios"
                suma += d
        return suma == numero

    def encontrar_multiples_divisores(self, *numeros):
        resultado = {}
        for numero in numeros:
            resultado[numero] = self.encontrar_divisores(numero)
        return resultado


df = DivisorFinder()
print(df.encontrar_divisores(12))
print(df.es_perfecto(6))