#--------------------Ejercicio propuesto:------------------------
# Clase AnalizadorNumeros que: 
# (1) tenga método es_par(numero) que retorne True/False; 
# (2) tenga método separar(*numeros) que retorne un diccionario 
# {'pares': [...], 'impares': [...]} reutilizando es_par; 
# (3) tenga método cantidad_pares_impares() que retorne una tupla (cant_pares, cant_impares).


#-----------------------------EPS---------------------------------
#Entrada:
#números en lote
#Proceso:
#lasificar pares e impares con operador %
#Salida:
#diccionario y tupla con cantidades

#-----------------------bosquejo----------------------------------
# BOSQUEJO (traza de separar(1,2,3,4,5,6,7,8,9)):
# numero=1 | es_par=False | pares=[]        | impares=[1]
# numero=2 | es_par=True  | pares=[2]       | impares=[1]
# numero=3 | es_par=False | pares=[2]       | impares=[1,3]
# numero=4 | es_par=True  | pares=[2,4]     | impares=[1,3]
# numero=5 | es_par=False | pares=[2,4]     | impares=[1,3,5]
# numero=6 | es_par=True  | pares=[2,4,6]   | impares=[1,3,5]
# numero=7 | es_par=False | pares=[2,4,6]   | impares=[1,3,5,7]
# numero=8 | es_par=True  | pares=[2,4,6,8] | impares=[1,3,5,7]
# numero=9 | es_par=False | pares=[2,4,6,8] | impares=[1,3,5,7,9]
#
# separar() retorna: {'pares': [2,4,6,8], 'impares': [1,3,5,7,9]}
# cantidad_pares_impares() = (len([2,4,6,8]), len([1,3,5,7,9])) = (4, 5)
#----------------------Codigo--------------------------------------------------
class AnalizadorNumeros:

    def es_par(self, numero):
        if numero % 2 ==0:
            return True
        else:
            return False

    def separar(self,*numeros):
        pares = []
        impares = []

        for numero in numeros:
            if self.es_par(numero):
                pares.append(numero)
            else:
                impares.append(numero)

        self.pares = pares
        self.impares = impares

        return {
            'pares': pares,
            'impares' : impares
        }
    

    def cantidad_pares_impares(self):
        return (len(self.pares), len(self.impares))

anaNum = AnalizadorNumeros()
print(anaNum.es_par(6))
print(anaNum.separar(1, 2, 3, 4, 5, 6, 7, 8,9))
print(anaNum.cantidad_pares_impares())