#--------------------Ejercicio propuesto:------------------------
# Clase CombinadorListas que: 
# (1) tenga método intercalar(lista1, lista2) que retorne una lista 
# alternando elementos de ambas; 
# (2) tenga método intercalar_multiples(*listas) que reutilice para varias listas.

#-----------------------------EPS---------------------------------
#Entrada:
#dos o más listas
#Proceso:
#recorrer con índices, alternando un elemento de cada lista
#Salida:
#una sola lista con los elementos intercalados

#-----------------------bosquejo----------------------------------
# BOSQUEJO (traza de intercalar([1,2], [3,4])):
# largo_max = max(2,2) = 2
# i=0 | i<len(lista1)? Sí -> agrega lista1[0]=1 -> resultado=[1]
#     | i<len(lista2)? Sí -> agrega lista2[0]=3 -> resultado=[1,3]
# i=1 | i<len(lista1)? Sí -> agrega lista1[1]=2 -> resultado=[1,3,2]
#     | i<len(lista2)? Sí -> agrega lista2[1]=4 -> resultado=[1,3,2,4]
#
# resultado: [1, 3, 2, 4]
#----------------------Codigo--------------------------------------------------

class CombinadorListas:
    def intercalar(self, lista1, lista2):
        resultado = []
        largo_max = max(len(lista1), len(lista2))   # por si una lista es más larga que la otra
        for i in range(largo_max):
            if i < len(lista1):
                resultado.append(lista1[i])
            if i < len(lista2):
                resultado.append(lista2[i])
        return resultado

    def intercalar_multiples(self, *listas):
        resultado = listas[0]
        for i in range(1, len(listas)):
            resultado = self.intercalar(resultado, listas[i])
        return resultado


cl = CombinadorListas()
print(cl.intercalar([1, 2], [3, 4]))