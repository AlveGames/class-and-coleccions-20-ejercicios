#intento1
#--------------------Ejercicio propuesto:------------------------
# Clase RegistroVentas que:

# Tenga método registrar(vendedor, monto) que guarde en un diccionario.
# Tenga método vendedores_destacados(monto_minimo) que retorne lista de vendedores con monto 
# igual o mayor al mínimo.
# Tenga método mejor_vendedor() que retorne nombre y monto del que vendió más (sin usar max()).
#-----------------------------EPS---------------------------------
#Entrada:
#nombre del vendedor y monto de venta
#Proceso:
#guardar en diccionario; filtrar por mínimo; comparar uno por uno para encontrar el mayor
#Salida:
#lista de destacados, tupla (nombre, monto) del mejor

#-----------------------bosquejo----------------------------------
# BOSQUEJO (traza de registrar en orden):
# registrar("Camila",850) -> ventas={"Camila":850}
# registrar("Eyser",620)  -> ventas={"Camila":850,"Eyser":620}
# registrar("Rasty",990)  -> ventas={"Camila":850,"Eyser":620,"Rasty":990}
#
# vendedores_destacados(700) -> recorre con .items():
# "Camila" 850 | 850>=700? Sí -> entra
# "Eyser"  620 | 620>=700? No -> no entra
# "Rasty"  990 | 990>=700? Sí -> entra
# resultado: ["Camila", "Rasty"]
#
# mejor_vendedor(): mejor_nombre=None, mejor_monto=-1
# "Camila" 850 | 850>-1? Sí -> mejor_monto=850, mejor_nombre="Camila"
# "Eyser"  620 | 620>850? No -> no cambia
# "Rasty"  990 | 990>850? Sí -> mejor_monto=990, mejor_nombre="Rasty"
# resultado: ("Rasty", 990)
#----------------------Codigo--------------------------------------------------
class RegistroVentas:
    def __init__(self):
        self.ventas = {}

    def registrar(self, vendedor, monto):
        self.ventas[vendedor] = monto

    def vendedores_destacados(self, monto_minimo):
        resultado = []
        for vendedor, monto in self.ventas.items():
            if monto >= monto_minimo:
                resultado.append(vendedor)
        return resultado

    def mejor_vendedor(self):
        mejor_nombre = None
        mejor_monto = -1
        for vendedor, monto in self.ventas.items():
            if monto > mejor_monto:
                mejor_monto = monto
                mejor_nombre = vendedor
        return (mejor_nombre, mejor_monto)


rv = RegistroVentas()
rv.registrar("Camila", 850)
rv.registrar("Eyser", 620)
rv.registrar("Rasty", 990)
print(rv.vendedores_destacados(700))
print(rv.mejor_vendedor())