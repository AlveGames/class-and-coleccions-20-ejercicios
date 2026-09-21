#intento 2...
#--------------------Ejercicio propuesto:------------------------
# Clase ControlAsistencia que:

# Tenga método registrar_alumno(nombre, porcentaje_asistencia) que guarde en un diccionario {nombre: porcentaje}.
# Tenga método alumnos_en_riesgo(porcentaje_minimo)
#   que retorne una lista de nombres cuyo porcentaje sea menor (<) al porcentaje_minimo.
# Tenga método promedio_riesgo(porcentaje_minimo) que retorne el promedio de asistencias 
#   solo de los alumnos en riesgo 
# (reutiliza alumnos_en_riesgo, luego busca cada porcentaje en el diccionario y saca el promedio solo de esos).
#-----------------------------EPS---------------------------------
#Entrada:
#nombre y porcentaje de asistencia
#Proceso:
#guardar en diccionario, filtrar los que estén por debajo de un mínimo, calcular promedio solo de esos
#Salida:
#lista de nombres en riesgo, promedio de asistencia de ese grupo

#-----------------------bosquejo----------------------------------
# BOSQUEJO (traza de registrar_alumno en orden):
# nombre="david" porcentaje=78 | self.personas={"david":78}
# nombre="keni"  porcentaje=61 | self.personas={..., "keni":61}
# nombre="caleb" porcentaje=30 | self.personas={..., "caleb":30}
#
# alumnos_en_riesgo(60) -> recorre con .items():
# "david" 78 | 78<60? No  -> no entra
# "keni"  61 | 61<60? No  -> no entra
# "caleb" 30 | 30<60? Sí  -> entra
# resultado = ["caleb"]
#
# promedio_riesgo(75):
# en_riesgo = alumnos_en_riesgo(75) -> "david"(78<75? No), "keni"(61<75? Sí), "caleb"(30<75? Sí)
#           = ["keni", "caleb"]
# asistencias = [self.personas["keni"], self.personas["caleb"]] = [61, 30]
# promedio = (61+30) / 2 = 45.5
#----------------------Codigo--------------------------------------------------
class ControlAsistencia:

    def __init__(self):
        self.personas = {}


    def registrar_alumno(self,nombre, porcentaje_asistencia):
        self.personas[nombre] = porcentaje_asistencia

    def alumnos_en_riesgo(self,porcentaje_minimo):
        resultado = []
        for nombre, porcentaje_asistencia in self.personas.items():
            if porcentaje_asistencia < porcentaje_minimo:
                resultado.append(nombre)
        return resultado

    def promedio_riesgo(self,porcentaje_minimo):
        en_riesgo = self.alumnos_en_riesgo(porcentaje_minimo)   
        asistencias = []      

        for nombre in en_riesgo:
            assism = self.personas[nombre]                            
            asistencias.append(assism)                                     

        return sum(asistencias) / len(asistencias) 


jugadores = ControlAsistencia()

jugadores.registrar_alumno("david", 78)
jugadores.registrar_alumno("keni", 61)
jugadores.registrar_alumno("caleb", 30)

print(jugadores.alumnos_en_riesgo(60))
print(jugadores.promedio_riesgo(75))