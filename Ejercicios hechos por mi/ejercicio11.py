#intento1
#--------------------Ejercicio propuesto:------------------------
# Clase ContadorVisitas que:

# Tenga método registrar_visita(pagina) que guarde en un diccionario contando repeticiones.
# Tenga método pagina_mas_visitada() que retorne la página con más visitas.
# Tenga método visitas_de(pagina) que retorne cuántas veces se ha visitado esa página.
#-----------------------------EPS---------------------------------
#Entrada:
#nombre de página, una por una
#Proceso:
#guardar en diccionario contando repeticiones; buscar la de mayor cantidad
#Salida:
#página más visitada, y cuántas veces se visitó una en específico

#-----------------------bosquejo----------------------------------
# BOSQUEJO (traza de registrar_visita en orden):
# registrar_visita("tienda-valheim") -> "tienda-valheim" no está -> visitas={"tienda-valheim":1}
# registrar_visita("foro-mods")      -> "foro-mods" no está      -> visitas={..., "foro-mods":1}
# registrar_visita("tienda-valheim") -> "tienda-valheim" SÍ está -> visitas={"tienda-valheim":2, "foro-mods":1}
# registrar_visita("tienda-valheim") -> SÍ está                  -> visitas={"tienda-valheim":3, "foro-mods":1}
#
# pagina_mas_visitada() -> recorre con .items():
# "tienda-valheim" veces=3 | 3>0? Sí -> cantidad=3, mejor="tienda-valheim"
# "foro-mods"      veces=1 | 1>3? No -> no cambia
# resultado: "tienda-valheim"
#
# visitas_de("foro-mods") = visitas.get("foro-mods", 0) = 1
#----------------------Codigo--------------------------------------------------
class ContadorVisitas:
    def __init__(self):
        self.visitas = {}

    def registrar_visita(self, pagina):
        if pagina in self.visitas:
            self.visitas[pagina] += 1
        else:
            self.visitas[pagina] = 1

    def pagina_mas_visitada(self):
        mejor = None
        cantidad = 0
        for pagina, veces in self.visitas.items():
            if veces > cantidad:
                cantidad = veces
                mejor = pagina
        return mejor

    def visitas_de(self, pagina):
        return self.visitas.get(pagina, 0)


cv = ContadorVisitas()
cv.registrar_visita("tienda-valheim")
cv.registrar_visita("foro-mods")
cv.registrar_visita("tienda-valheim")
cv.registrar_visita("tienda-valheim")
print(cv.pagina_mas_visitada())
print(cv.visitas_de("foro-mods"))