#intento 1...
#--------------------Ejercicio propuesto:------------------------
# Clase RegistroJugadores que:

# Tenga método agregar_jugador(nombre, nivel) que guarde en un diccionario {nombre: nivel}.
# Tenga método jugadores_avanzados(nivel_minimo) que retorne una lista de nombres 
# cuyo nivel sea mayor (>, no >=) al nivel_minimo.
# Tenga método promedio_avanzados(nivel_minimo) que retorne el promedio de nivel, 
# pero SOLO de los jugadores avanzados (reutiliza jugadores_avanzados para saber qué nombres califican,
#  y de ahí calcula el promedio solo de esos — no de todos).
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
#----------------------Codigo--------------------------------------------------
class RegistroJugadores:

    def __init__(self):
        self.jugadores = {}
    def agregar_jugador(self,nombre, nivel):
        self.jugadores[nombre] = nivel

    def jugadores_avanzados(self,nivel_minimo):
        lista_nombres = []
        for nombre, nivel in self.jugadores.items():
            if nivel > nivel_minimo:
                lista_nombres.append(nombre)
        return lista_nombres


    def promedio_avanzados(self,nivel_minimo):
        nombres_avanzados = self.jugadores_avanzados(nivel_minimo)   # 1. saca los nombres que califican
        niveles = []      
                                                                        # 2. lista vacía para los niveles
        for nombre in nombres_avanzados:
            nivel = self.jugadores[nombre]                            #    busca el nivel de ese nombre
            niveles.append(nivel)                                     #    lo guarda

        return sum(niveles) / len(niveles)  
    
jugadores = RegistroJugadores()

jugadores.agregar_jugador("alve", 26)
jugadores.agregar_jugador("kinshi", 13)
jugadores.agregar_jugador("rasty", 31)

print(jugadores.jugadores_avanzados(15))
print(jugadores.promedio_avanzados(27))

#comentario:
#creo qu7e por el cansancio ya no estoy entendiendo los for...