#Clase GestorPersonas que: 
# (1) tenga método agregar_persona(nombre, edad) que guarde en un diccionario; 
# (2) tenga método personas_mayores(edad_minima) que retorne una lista de nombres cuya edad sea ≥; 
# (3) tenga método edad_promedio() que retorne el promedio de edades.


class GestorPersonas:
    def __init__(self):
        self.personas = {}

    def agregar_persona(self, nombre, edad):
        self.personas[nombre] = edad

    def personas_mayores(self, edad_minima):
        resultado = []
        for nombre, edad in self.personas.items():
            if edad >= edad_minima:
                resultado.append(nombre)
        return resultado

    def edad_promedio(self):
        return sum(self.personas.values()) / len(self.personas)

gp = GestorPersonas()
gp.agregar_persona("Ana", 28)
gp.agregar_persona("Bob", 17)
print(gp.personas_mayores(18))     # ['Ana']
print(gp.edad_promedio())          # 22.5
