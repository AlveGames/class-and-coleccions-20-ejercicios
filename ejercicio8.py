#Clase Equipos que: 
# (1) tenga método crear_equipo(nombre_equipo) que inicie un equipo como una lista vacía en un diccionario; 
# (2) tenga método agregar_jugador(equipo, jugador) que añada el jugador al equipo; 
# (3) tenga método equipo_mayor_integrantes() que retorne el nombre del equipo con más jugadores.


class Equipos:
    def __init__(self):
        self.equipos = {}

    def crear_equipo(self, nombre_equipo):
        self.equipos[nombre_equipo] = []

    def agregar_jugador(self, equipo, jugador):
        self.equipos[equipo].append(jugador)

    def equipo_mayor_integrantes(self):
        mayor = None
        for nombre, jugadores in self.equipos.items():
            if mayor is None or len(jugadores) > len(self.equipos[mayor]):
                mayor = nombre
        return mayor