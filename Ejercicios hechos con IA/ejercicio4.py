#--------------------Ejercicio propuesto:------------------------
# Clase InversorSecuencia que: 
# (1) tenga método invertir_lista(lista) que retorne la lista invertida sin usar reversed() 
# (usa manual con bucles); 
# (2) tenga método invertir_multiples(*listas) que reutilice el anterior para invertir varias listas 
# y retorne un diccionario {lista_original: lista_invertida}.
#-----------------------------EPS---------------------------------
#Entrada:
#lista o varias listas
#Proceso:
#invertir manualmente, guardar en diccionario
#Salida:
#lista invertida o diccionario
#-----------------------bosquejo----------------------------------
# BOSQUEJO (traza de invertir_lista([12,13,14,15])):
# i=3 | lista[3]=15 | invertida=[15]
# i=2 | lista[2]=14 | invertida=[15,14]
# i=1 | lista[1]=13 | invertida=[15,14,13]
# i=0 | lista[0]=12 | invertida=[15,14,13,12]
# resultado: [15,14,13,12]
#
# invertir_multiples([50,70,27,26], ["valheim","es","god"], [5,6]):
# lista=[50,70,27,26]        -> invertida=[26,27,70,50]        -> resultado[(50,70,27,26)]=[26,27,70,50]
# lista=["valheim","es","god"] -> invertida=["god","es","valheim"] -> resultado[(...)]=["god","es","valheim"]
# lista=[5,6]                -> invertida=[6,5]                -> resultado[(5,6)]=[6,5]
#----------------------Codigo--------------------------------------------------
class InversorSecuencia:


    def invertir_lista(self,lista):
        invertida = []

        for i in range(len(lista) - 1, -1, -1):
            invertida.append(lista[i])

        return invertida


    def invertir_multiples(self,*listas):
        resultado = {}

        for lista in listas:
            invertida = self.invertir_lista(lista)
            resultado[tuple(lista)] = invertida

        return resultado

inversor = InversorSecuencia()
lista = [12,13,14,15]

print (inversor.invertir_lista(lista))
resultado_multiple = inversor.invertir_multiples(
    [50,70,27,26],
    ["valheim","es","god"],
    [5, 6]
)

print(resultado_multiple)