#intento 1
#--------------------Ejercicio propuesto:------------------------
# Clase RotadorLista que:

# -Tenga método rotar_derecha(lista) que mueva el último elemento al inicio de la lista, 
# y retorne la lista rotada (sin usar funciones especiales, con bucle manual — piensa en índices, 
# como hiciste con invertir_lista).
# -Tenga método rotar_multiples(*listas) que reutilice rotar_derecha para varias listas, 
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
class RotadorLista:

    def rotar_derecha(self, lista):
        ultimo = lista[-1]   # hacemos que el ultimo elemento del indice se encuentre al inicio(osea el el numero 4)
        rotado = [ultimo]                 #con esto se confirma que la lista comience con el ultimo indice


        for i in range(0, len(lista) - 1):   #como falta  el resto de la lista recorremos índices 0,1,2 (el resto, sin tocar el 3)
                            #RECORDATORIO.... range no incluye el ultimo elemento que le das en este caso "len(lista) -1"
            rotado.append(lista[i])          # los agregamos en su orden normal

        return rotado

    def rotar_multiples(self, *listas):
        resultado = {}
        for lista in listas:
            rotado = self.rotar_derecha(lista)   # reutiliza el método anterior
            resultado[tuple(lista)] = rotado
        return resultado

r = RotadorLista()
print(r.rotar_derecha([1,2,3,4]))          # [15, 5, 10]
# print(r.rotar_derecha(["gato", "perro"]))    # ['perro', 'gato']
# print(r.rotar_derecha([100]))                # [100]  (un solo elemento, no cambia)
# print(r.rotar_derecha([1, 2, 3, 4, 5, 6]))   # [6, 1, 2, 3, 4, 5]


#comentario:
#al parecer me hace falta practicar con range... ya que no encuentro como hacerlo...
#asi que este intento es fallido...