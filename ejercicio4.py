#Clase InversorSecuencia que: 
# (1) tenga método invertir_lista(lista) que retorne la lista invertida sin usar reversed() (usa manual con bucles); 
# (2) tenga método invertir_multiples(*listas) que reutilice el anterior para invertir varias listas y 
# retorne un diccionario {lista_original: lista_invertida}.
class InversorSecuencia:
    def invertir_lista(self, lista):
        resultado = []
        for elemento in lista:
            resultado.insert(0, elemento)  # inserta cada uno al inicio -> queda invertida
        return resultado

    def invertir_multiples(self, *listas):
        resultado = {}
        for lista in listas:
            resultado[tuple(lista)] = self.invertir_lista(lista)  # tuple() porque una lista no puede ser clave de dict
        return resultado


inv = InversorSecuencia()
print(inv.invertir_lista([1, 2, 3]))                  # [3, 2, 1]
print(inv.invertir_multiples([1, 2, 3], [4, 5]))      # {(1,2,3): [3,2,1], (4,5): [5,4]}