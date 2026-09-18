#--------------------Ejercicio propuesto:------------------------
# Clase RegistroEtiquetas que:

# Tenga método agregar_etiqueta(etiqueta) que agregue la etiqueta a un conjunto (para evitar duplicados) y 
#       a una lista (para mantener el orden en que se agregaron, con repetidos incluidos).
# Tenga método contar_etiquetas_unicas() que retorne cuántas etiquetas únicas hay.
# Tenga método agregar_varias(*args) que reciba múltiples etiquetas y reutilice agregar_etiqueta para cada una.
#-----------------------------EPS---------------------------------
#Entrada:
# etiquetas individuales o en lotes
#Proceso:
#guardar en conjunto y lista, contar únicas
#Salida:
#cantidad de palabras únicas
#-----------------------bosquejo----------------------------------
# BOSQUEJO (traza de agregar_varias("accion","rpg","accion","survival") + agregar_etiqueta("rpg")):
# Vuelta 1 | etiqueta="accion"   | etiquetas_unicas={"accion"}                     | lista_etiquetas=["accion"]
# Vuelta 2 | etiqueta="rpg"      | etiquetas_unicas={"accion","rpg"}               | lista_etiquetas=["accion","rpg"]
# Vuelta 3 | etiqueta="accion"   | etiquetas_unicas={"accion","rpg"}  (no cambia)  | lista_etiquetas=["accion","rpg","accion"]
# Vuelta 4 | etiqueta="survival" | etiquetas_unicas={"accion","rpg","survival"}    | lista_etiquetas=["accion","rpg","accion","survival"]
# Luego (fuera del lote):
# agregar_etiqueta("rpg") | etiquetas_unicas={"accion","rpg","survival"} (no cambia) | lista_etiquetas=["accion","rpg","accion","survival","rpg"]

# contar_etiquetas_unicas() = len({"accion","rpg","survival"}) = 3
#----------------------Codigo--------------------------------------------------
class RegistroEtiquetas:
    def __init__(self):
        self.etiquetas_unicas = set()
        self.lista_etiquetas = []
        
    def agregar_etiqueta(self, etiqueta):
        self.etiquetas_unicas.add(etiqueta)
        self.lista_etiquetas.append(etiqueta)

    def contar_etiquetas_unicas(self):
        return len(self.etiquetas_unicas)

    def agregar_varias(self, *args):
        for etiqueta in args:
            self.agregar_etiqueta(etiqueta)

r = RegistroEtiquetas()
r.agregar_varias("accion", "rpg", "accion", "survival")
r.agregar_etiqueta("rpg")
print(r.contar_etiquetas_unicas())

#comentario:
#veo que la ia no se le complico mucho volver a hacer un caso nuevo, 
# de hecho solo me hizo reemplazar algunas cosas, y no agregó nada nuevo, creo que le
#tendre que pedirle que le suba la dificultad
