#intento 1...
#--------------------Ejercicio propuesto:------------------------
# Clase Almacen que:

# Tenga método agregar_producto(nombre, unidad) que guarde en un diccionario {nombre: unidad}.
# Tenga método total_unidades() que retorne la suma de todas las cantidades.
# Tenga método productos_bajo_stock(minimo) que retorne una lista con los nombres de los productos 
# cuya unidad sea menor al minimo dado (ojo: aquí es una sola condición, 
# no un rango entre dos números como en unidades_por_rango).


#-----------------------------EPS---------------------------------
#Entrada:
#nombres de los productos y la unidad
#Proceso:
#guardar en el diccionario , sumar unidad y filtrar para un valor minimo
#Salida:
#total , stock bajo

#-----------------------bosquejo----------------------------------
#
# 
#
#  
#----------------------Codigo--------------------------------------------------
class Almacen:
    def __init__(self):
        self.cantidades = {}

    def agregar_producto(self, nombre, unidad):
        self.cantidades[nombre] = unidad

    def total_unidades(self):
        return sum(self.cantidades.values())

    def  productos_bajo_stock(self, minimo = 5):
        resultado = []

        for nombre,unidad in self.cantidades.items():
            if unidad < minimo:           
#aqui me ayudo la ia... viendo el simbolo que estaba "<=" y me dijo que lo cambie por "<"
                resultado.append(nombre)
        return resultado

alma = Almacen()

alma.agregar_producto("vino tinto", 25)
alma.agregar_producto("cifrut", 4)
alma.agregar_producto("teclado gamer", 7)
alma.agregar_producto("mause g502", 1)
print(f"los  productos con menos stock que hay son: " ,alma.productos_bajo_stock())
print("la cantidad total de productos que hay en el almacen son: ",alma.total_unidades())
#comentario:
#aqui la ia me ayudo viendo un simbolo asi que eso cuenta como ayuda de la ia
#este ejercicio ya no cuenta como hecho por mi porque me ayudo en algo :,(
