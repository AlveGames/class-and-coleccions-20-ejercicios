#intento 3...
#--------------------Ejercicio propuesto:------------------------
# Clase Desplazador que:

# Tenga método mover_dos_al_frente(lista) que mueva los dos últimos elementos al inicio de la lista, 
# manteniendo su orden relativo entre ellos, y el resto después en orden normal.
# Tenga método mover_multiples(*listas) que reutilice el método anterior para varias listas, 
# retornando un diccionario {lista_original: lista_movida}.
#-----------------------------EPS---------------------------------
#Entrada:
#una lista o un grupo de listas
#Proceso:
#desplaza los 2 ultimos elementos al inicio, el otro hace lo mismo pero con un grupo de listas
#Salida:
#sale una lista con elementos desplazados
#-----------------------bosquejo----------------------------------
# BOSQUEJO (traza de mover_dos_al_frente([1,2,3,4,5])):
# ultimo = lista[-1] = 5
# penultimo = lista[-2] = 4
# rotado = [penultimo, ultimo] = [4, 5]
#
# for i in range(0, len(lista)-2) -> range(0, 3) -> i toma 0,1,2
# Vuelta 1 | i=0 | lista[0]=1 | rotado=[4,5,1]
# Vuelta 2 | i=1 | lista[1]=2 | rotado=[4,5,1,2]
# Vuelta 3 | i=2 | lista[2]=3 | rotado=[4,5,1,2,3]
#
# resultado: [4, 5, 1, 2, 3]
#
# mover_multiples([10,20,30,40,50], ["valheim","es","god"]):
# lista=[10,20,30,40,50]     -> rotado=[40,50,10,20,30]     -> resultado[(10,20,30,40,50)]=[40,50,10,20,30]
# lista=["valheim","es","god"] -> rotado=["es","god","valheim"] -> resultado[(...)]=["es","god","valheim"]
#----------------------Codigo--------------------------------------------------
class desplazador:

    def mover_dos_al_frente(self, lista):
        ultimo = lista[-1]
        penultimo = lista[-2]
        rotado = [penultimo,ultimo]

        for i in range(0, len(lista) - 2):
             rotado.append(lista[i]) 
        return rotado

    def mover_multiples(self, *listas):
        resultado = {}
        for lista in listas:
            rotado = self.mover_dos_al_frente(lista)   
            resultado[tuple(lista)] = rotado
        return resultado

r = desplazador()
print(r.mover_dos_al_frente([1,2,3,4,5,6,7]))  

resultado = r.mover_multiples([10, 20, 30,40,50], ["valheim", "es", "god"])
print(resultado)

#comentario:
#lo importante es saber entender lo que pide el enunciado ... 
# despues de 2 intentos fallidos este lo entendi super rapido y reutilice codigo muy rapidamente
