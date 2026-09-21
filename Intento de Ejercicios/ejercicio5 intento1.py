#intento 1...
#--------------------Ejercicio propuesto:------------------------
# Clase ClasificadorEdades que:

# Tenga método es_mayor_edad(edad) que retorne True si la edad es mayor o igual a 18, False en caso contrario.
# Tenga método clasificar(*edades) que reciba varias edades, reutilice es_mayor_edad, 
# y retorne un diccionario {'mayores': [...], 'menores': [...]}.
# Tenga método promedio_por_grupo() que retorne una tupla con (promedio_mayores, promedio_menores). 
# Si algún grupo queda vacío, 
# ese promedio debe ser 0 (para evitar el error de dividir entre cero que vimos en el Ej. 1).
#-----------------------------EPS---------------------------------
#Entrada:
#
#Proceso:
#
#Salida:
#
#-----------------------bosquejo----------------------------------
#
# 
#
#  
#----------------------Codigo--------------------------------------------------
class ClasificadorEdades():
    def __init__(self):
        pass
    def es_mayor_edad(self, edad):
        if edad >= 18:
            return True
        else:
            return False

    def clasificar(self, *edades):
        mayores = []
        menores = []

        for numero in edades:
            if self.es_mayor_edad(numero):
                mayores.append(numero)
            else:
                menores.append(numero)

        self.mayores = mayores
        self.menores = menores

        return {
            'mayores': mayores,
            'menores' : menores
        }

    def promedio_por_grupo(self):
            return (sum(self.mayores)/len(self.mayores), sum(self.menores)/len(self.menores))

clasi = ClasificadorEdades()
print(clasi.es_mayor_edad(6))
print(clasi.clasificar(16,18,19,12,11))
print(clasi.promedio_por_grupo())

#comentario...
#eso me pasa por no leer bien... la ia me dio el resultado de promedio por grupo ya que se me paso por alto
#que en la lectura decia promedio... y me faltaba... pero no cuenta porque me dio la respuesta :/