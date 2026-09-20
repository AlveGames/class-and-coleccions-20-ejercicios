#intento 2...
#--------------------Ejercicio propuesto:------------------------
# Clase RotadorInverso que:

# Tenga método rotar_izquierda(lista) que mueva el primer elemento al final de la lista 
# (lo opuesto a lo que hiciste: en vez de mover el último al frente, mueves el primero al final). Sin funciones especiales, con índices manuales.
# Tenga método rotar_multiples(*listas) que reutilice rotar_izquierda para varias listas, 
# y retorne un diccionario {lista_original: lista_rotada}.
#-----------------------------EPS---------------------------------
#Entrada:
#
#Proceso:
#
#Salida:
#
#-----------------------bosquejo----------------------------------
#
#----------------------Codigo--------------------------------------------------
class RotadorInverso:

    def rotar_izquierda(self, lista):
        primero = lista[0]  
        rotado = [] 


        for i in range(1, len(lista)): 
            rotado.append(lista[i])
        rotado.append(primero)          
        return rotado
        
    def rotar_multiples(self, *listas):
        resultado = {}
        for lista in listas:
            rotado = self.rotar_izquierda(lista)  
            resultado[tuple(lista)] = rotado
        return resultado

r = RotadorInverso()
print(r.rotar_izquierda([1, 2, 3, 4]))   # debería dar [2, 3, 4, 1]

resultado = r.rotar_multiples([10, 20, 30], ["a", "b", "c"])
print(resultado)
#comentario...
#otro error mas pero al menos se entiende mejor como funciona todo
#tocara ir al tercer intento...