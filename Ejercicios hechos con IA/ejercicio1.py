#--------------------Ejercicio propuesto:------------------------
# Clase Calificador que: 
# (1) tenga método validar_nota(nota) que retorne True si 0 ≤ nota ≤ 100, False en caso contrario; 
# (2) tenga método cargar_notas(*args) que reciba múltiples notas, las valide, agregue solo las válidas a una lista interna, y retorne esa lista; 
# (3) tenga método promedio() que retorne el promedio de notas almacenadas.


#-----------------------------EPS---------------------------------
#Entrada:
#notas individuales o en lotes (*args)
#Proceso:
#validar cada nota (0-100), guardar en lista, calcular promedio
#Salida:
#True/False, lista de válidas, promedio

#-----------------------bosquejo----------------------------------
# BOSQUEJO (traza de cargar_notas(100, 75, 40, 500)):
# Vuelta 1 | nota=100 | validar_nota=True  | self.notas=[100]
# Vuelta 2 | nota=75  | validar_nota=True  | self.notas=[100, 75]
# Vuelta 3 | nota=40  | validar_nota=True  | self.notas=[100, 75, 40]
# Vuelta 4 | nota=500 | validar_nota=False | self.notas=[100, 75, 40]  (no cambia)
#
# promedio() = (100+75+40) / 3 = 71.67
#----------------------Codigo--------------------------------------------------

class Calificador:
    def __init__(self):
        self.notas = []

    def validar_nota(self,nota):
        if 0 <= nota <= 100:
            return True
        else:
            return False

    def cargar_notas(self, *args):

        for nota in args:
            if self.validar_nota(nota):
                self.notas.append(nota)
        return self.notas

    def promedio(self):
        if len(self.notas) == 0:
            return "no existe ninguna nota valida para ver el promedio"

        return sum(self.notas)/ len(self.notas)


# cal = Calificador()
# print(cal.cargar_notas(500))
# print(cal.promedio())

cal = Calificador()
print(cal.cargar_notas(100, 75, 40, 500))
print(cal.promedio())