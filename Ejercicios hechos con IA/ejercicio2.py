#--------------------Ejercicio propuesto:------------------------
# Clase AnalizadorTexto que:
# (1) tenga método agregar_palabra(palabra) que agregue la palabra a un conjunto (para evitar duplicados)
# y a una lista (para el orden);
# (2) tenga método contar_palabras() que retorne cuántas palabras únicas hay;
# (3) tenga método agregar_multiples(*args) que reutilice agregar_palabra para varios.

#-----------------------------EPS---------------------------------
# Entrada:
# palabras individuales o en lotes
# Proceso:
# guardar en conjunto y lista, contar únicas
# Salida:
# cantidad de palabras únicas

#-----------------------bosquejo----------------------------------
# BOSQUEJO (traza de agregar_multiples("hola","mundo","hola") + agregar_palabra("gato")):
# Vuelta 1 | palabra="hola"  | set_palabras={"hola"}                | lista_palabras=["hola"]
# Vuelta 2 | palabra="mundo" | set_palabras={"hola","mundo"}        | lista_palabras=["hola","mundo"]
# Vuelta 3 | palabra="hola"  | set_palabras={"hola","mundo"}        | lista_palabras=["hola","mundo","hola"]
#          | (el set NO cambia porque "hola" ya existía; la lista SÍ crece)
# Luego (fuera del lote):
# agregar_palabra("gato")   | set_palabras={"hola","mundo","gato"} | lista_palabras=["hola","mundo","hola","gato"]
#
# contar_palabras() = len({"hola","mundo","gato"}) = 3
#----------------------Codigo--------------------------------------------------

class AnalizadorTexto:
    def __init__(self):
        self.palabras_unicas = set()
        self.listas_palabras = []

    def agregar_palabra(self, palabra):
        self.palabras_unicas.add(palabra)
        self.listas_palabras.append(palabra)

    def contar_palabras(self):
        return len(self.palabras_unicas)

    def agregar_multiples(self, *args):
        for palabra in args:
            self.agregar_palabra(palabra)


ana = AnalizadorTexto()
ana.agregar_multiples("hola", "mundo", "hola")
ana.agregar_palabra("gato")
print(ana.contar_palabras())   # 3

# print(f"las palabras fueron: {ana.listas_palabras}")
# print(f"las palabras sin repetir fueron: {ana.palabras_unicas}")