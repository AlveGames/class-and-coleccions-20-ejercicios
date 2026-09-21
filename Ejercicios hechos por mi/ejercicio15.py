#intento 1...
#--------------------Ejercicio propuesto:------------------------
# Clase FactorFinder que:

# Tenga método encontrar_factores(numero) que retorne una tupla con todos los divisores.
# Tenga método es_abundante(numero) que retorne True si la suma de sus divisores (sin contar 
# el mismo número) es MAYOR a él.
# Tenga método encontrar_multiples_factores(*numeros) que retorne un diccionario 
# {número: tupla_factores}.
#-----------------------------EPS---------------------------------
#Entrada:
#uno o varios números
#Proceso:
#probar divisores del 1 al mismo número; sumar los divisores propios y comparar contra el número
#Salida:
#tupla de factores, booleano, diccionario con varios números

#-----------------------bosquejo----------------------------------
# BOSQUEJO (traza de encontrar_factores(18)):
# i=1 | 18%1==0? Sí -> factores=[1]
# i=2 | 18%2==0? Sí -> factores=[1,2]
# i=3 | 18%3==0? Sí -> factores=[1,2,3]
# i=4,5 | no dividen exacto
# i=6 | 18%6==0? Sí -> factores=[1,2,3,6]
# i=7,8 | no dividen
# i=9 | 18%9==0? Sí -> factores=[1,2,3,6,9]
# i=10..17 | ninguno divide
# i=18 | 18%18==0? Sí -> factores=[1,2,3,6,9,18]
#
# resultado: (1,2,3,6,9,18)
#
# es_abundante(18): suma sin contar 18 = 1+2+3+6+9 = 21
# 21 > 18? Sí -> True (18 es "abundante")
#----------------------Codigo--------------------------------------------------
class FactorFinder:
    def encontrar_factores(self, numero):
        factores = []
        for i in range(1, numero + 1):
            if numero % i == 0:
                factores.append(i)
        return tuple(factores)

    def es_abundante(self, numero):
        factores = self.encontrar_factores(numero)
        suma = 0
        for f in factores:
            if f != numero:
                suma += f
        return suma > numero

    def encontrar_multiples_factores(self, *numeros):
        resultado = {}
        for numero in numeros:
            resultado[numero] = self.encontrar_factores(numero)
        return resultado


ff = FactorFinder()
print(ff.encontrar_factores(18))
print(ff.es_abundante(18))
print(ff.encontrar_multiples_factores(12, 18))