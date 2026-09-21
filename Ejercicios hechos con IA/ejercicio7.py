#--------------------Ejercicio propuesto:------------------------
# Clase GestorPersonas que: 
# (1) tenga método agregar_persona(nombre, edad) que guarde en un diccionario; 
# (2) tenga método personas_mayores(edad_minima) que retorne una lista de nombres cuya edad sea ≥; 
# (3) tenga método edad_promedio() que retorne el promedio de edades.
#-----------------------------EPS---------------------------------
#Entrada:
#nombres y edades
#Proceso:
#guardar en diccionario, filtrar, promediar
#Salida:
#lista filtrada, promedio
#-----------------------bosquejo----------------------------------
# BOSQUEJO (traza de agregar_persona en orden):
# nombre="eyser rocha" edad=21 | self.personas={"eyser rocha":21}
# nombre="caizini"     edad=20 | self.personas={..., "caizini":20}
# nombre="rasty"       edad=19 | self.personas={..., "rasty":19}
# nombre="tokiko"      edad=15 | self.personas={..., "tokiko":15}
#
# personas_mayores(18) -> recorre con .items():
# "eyser rocha" edad=21 | 21>=18? Sí -> entra
# "caizini"     edad=20 | 20>=18? Sí -> entra
# "rasty"       edad=19 | 19>=18? Sí -> entra
# "tokiko"      edad=15 | 15>=18? No -> no entra
# resultado = ["eyser rocha", "caizini", "rasty"]
#
# edad_promedio() = (21+20+19+15) / 4 = 75/4 = 18.75
#----------------------Codigo--------------------------------------------------
class GestorPersonas:
    def __init__(self):
        self.personas = {}


    def agregar_persona(self,nombre,edad):
        self.personas[nombre] = edad

    def personas_mayores(self,edad_minima):
        resultado = []
        for nombre, edad in self.personas.items():
            if edad >= edad_minima:
                resultado.append(nombre)
        return resultado

    def edad_promedio(self):
        return sum(self.personas.values()) / len(self.personas)

gper = GestorPersonas()

gper.agregar_persona("eyser rocha",21)
gper.agregar_persona("caizini",20)
gper.agregar_persona("rasty",19)
gper.agregar_persona("tokiko",15)
print(gper.personas_mayores(18))
print(gper.edad_promedio())