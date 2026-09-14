#Clase AnalizadorNumeros que: 
# (1) tenga método es_par(numero) que retorne True/False; 
# (2) tenga método separar(*numeros) que retorne un diccionario {'pares': [...], 'impares': [...]} reutilizando es_par; 
# (3) tenga método cantidad_pares_impares() que retorne una tupla (cant_pares, cant_impares).

class AnalizadorNumeros:
    def __init__(self):
        self._pares = []
        self._impares = []

    def es_par(self, numero):
        return numero % 2 == 0

    def separar(self, *numeros):
        for n in numeros:
            if self.es_par(n):
                self._pares.append(n)
            else:
                self._impares.append(n)
        return {'pares': self._pares, 'impares': self._impares}

    def cantidad_pares_impares(self):
        return (len(self._pares), len(self._impares))


an = AnalizadorNumeros()
print(an.separar(1, 2, 3, 4, 5))          # {'pares': [2,4], 'impares': [1,3,5]}
print(an.cantidad_pares_impares())        # (2, 3)