# intento 1...
# Ejercicio parecido al 1 — para que lo hagas solo:

# Clase ControlDeStock que:

# Tenga método validar_cantidad(cantidad) que retorne True si la cantidad está entre 1 y 50 (inclusive), 
# False en caso contrario.
# Tenga método cargar_cantidades(*args) que reciba varias cantidades, las valide con el método anterior, 
# guarde solo las válidas en una lista interna, y retorne esa lista.
# Tenga método total_stock() que retorne la suma de todas las cantidades guardadas.

#-----------------------------EPS---------------------------------
#(lo mismo que el anterior del ejercicio 1)
#Entrada:
#cantidades individuales o en lotes (*args)
#Proceso:
#validar cada cantidad (0-50), guardar en lista, calcular la suma total
#Salida:
#True/False, lista de válidas, suma total

#-----------------------bosquejo----------------------------------
# BOSQUEJO (traza de cargar_cantidades(50,25,75)):
# Vuelta 1 | cantidad=50 | validar_cantidad=True  | self.cantidads=[50]
# Vuelta 2 | cantidad=25 | validar_cantidad=True  | self.cantidads=[50, 25]
# Vuelta 3 | cantidad=75 | validar_cantidad=False | self.cantidads=[50, 25] (no cambia)
#
# total_stock = (50+25) = 75
#----------------------Codigo--------------------------------------------------
class ControlDeStock:
    def __init__(self):
        self.cantidades = []

    
    def validar_cantidad(self, cantidad):
        if 0 <= cantidad <= 50:
            return True
        else:
            return False

    def cargar_cantidades(self, *args):
        for cantidad in args:
            if self.validar_cantidad(cantidad):
                self.cantidades.append(cantidad)
        return self.cantidades


    def total_stock(self):
        if len(self.cantidades) == 0:
            return "no existe ninguna nota valida para sumar todo..."

        return sum(self.cantidades)

ctrl = ControlDeStock()

print(ctrl.cargar_cantidades(50,25,75))

print(ctrl.total_stock())

#comentario:
#Al terminarlo, la ia me dio una pista simple ya que encontro un error , 
# no me dio un concepto completo para copy/paste
# ME DIJO: "mira la diferencia entre cómo nombraste la variable en __init__ vs en los otros métodos"
#algo simple pero que me hizo ver varios errores
# (nose si cuenta como intento bueno pero para mi si)