#--------------------Ejercicio propuesto:------------------------
# Clase Equipos que: 
# (1) tenga método crear_equipo(nombre_equipo) que inicie un equipo como una lista vacía en un diccionario; 
# (2) tenga método agregar_jugador(equipo, jugador) que añada el jugador al equipo; 
# (3) tenga método equipo_mayor_integrantes() que retorne el nombre del equipo con más jugadores.


#-----------------------------EPS---------------------------------
#Entrada:
#nombres de equipos y jugadores
#Proceso:
#crear estructura equipo→[jugadores], contar, comparar
#Salida:
#equipo con mayor cantidad
#-----------------------bosquejo----------------------------------
# BOSQUEJO (traza de equipo_mayor_integrantes()):
# self.equipos = {"Barcelona":["Juan","Pedro","Luis"], "Emelec":["Carlos"], "Liga":["Ana","Jose"]}

# mayor_equipo=None | mayor_cantidad=0
# equipo="Barcelona" | len(jugadores)=3 | 3>0? Sí -> mayor_cantidad=3, mayor_equipo="Barcelona"
# equipo="Emelec"    | len(jugadores)=1 | 1>3? No  -> no cambia
# equipo="Liga"      | len(jugadores)=2 | 2>3? No  -> no cambia
#
# resultado: "Barcelona"
#----------------------Codigo--------------------------------------------------
class Equipos:
    def __init__(self):
        self.equipos = {}
    def crear_equipo(self,nombre_equipo):
        self.equipos[nombre_equipo] = []

    def agregar_jugador(self,equipo, jugador):
        self.equipos[equipo].append(jugador)

    def equipo_mayor_integrantes(self):
        mayor_equipo = None
        mayor_cantidad = 0
        for equipo, jugadores in self.equipos.items():
            if len(jugadores) > mayor_cantidad:
                mayor_cantidad = len(jugadores)
                mayor_equipo = equipo
        return mayor_equipo

gestor = Equipos()

gestor.crear_equipo("Barcelona") 
gestor.crear_equipo("Emelec") 
gestor.crear_equipo("Liga")
gestor.agregar_jugador("Barcelona", "Juan") 
gestor.agregar_jugador("Barcelona", "Pedro") 
gestor.agregar_jugador("Barcelona", "Luis") 
gestor.agregar_jugador("Emelec", "Carlos")
gestor.agregar_jugador("Liga", "Ana") 
gestor.agregar_jugador("Liga", "Jose")

print(gestor.equipo_mayor_integrantes())

