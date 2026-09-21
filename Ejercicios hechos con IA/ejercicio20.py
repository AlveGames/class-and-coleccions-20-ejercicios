#--------------------Ejercicio propuesto:------------------------
# Clase AnalizadorPatrones que: 
# (1) tenga método encontrar_palabras(texto, patron) que busque palabras que inicien con el patrón y retorne una lista; 
# (2) tenga método agrupar_por_longitud(texto) que retorne un diccionario {longitud: [palabras]}; 
# (3) tenga método palabras_unicas() usando un conjunto.

#-----------------------------EPS---------------------------------
#Entrada:
#texto y patrón de búsqueda
#Proceso:
#split(), filtrar con startswith, agrupar por longitud, eliminar duplicados con set
#Salida:
#listas, diccionario, conjunto

#-----------------------bosquejo----------------------------------
# BOSQUEJO (traza de encontrar_palabras("el gato de mi casa es una gata", "ga")):
# palabra="el"    | startswith("ga")? No
# palabra="gato"  | startswith("ga")? Sí -> resultado=["gato"]
# palabra="de"    | No
# palabra="mi"    | No
# palabra="casa"  | No
# palabra="es"    | No
# palabra="una"   | No
# palabra="gata"  | startswith("ga")? Sí -> resultado=["gato","gata"]
# resultado: ["gato", "gata"]
#
# BOSQUEJO (traza de agrupar_por_longitud("la casa de la esquina")):
# palabra="la"      | longitud=2 | 2 no está en grupos -> grupos={2:[]}    -> grupos={2:["la"]}
# palabra="casa"    | longitud=4 | 4 no está en grupos -> grupos={2:["la"],4:[]}  -> grupos={2:["la"],4:["casa"]}
# palabra="de"      | longitud=2 | 2 SÍ está en grupos -> grupos={2:["la","de"],4:["casa"]}
# palabra="la"      | longitud=2 | 2 SÍ está           -> grupos={2:["la","de","la"],4:["casa"]}
# palabra="esquina" | longitud=7 | 7 no está           -> grupos={..., 7:["esquina"]}
# resultado: {2:["la","de","la"], 4:["casa"], 7:["esquina"]}
# (IMPORTANTE: esto solo funciona si el return está FUERA del for -- ver corrección abajo)
#
# BOSQUEJO (traza de palabras_unicas(), con self.texto="asdqweasd qwsda"):
# palabras = ["asdqweasd", "qwsda"]
# unicas = set(palabras) = {"asdqweasd", "qwsda"}   (ya eran distintas, no había duplicados)
#----------------------Codigo--------------------------------------------------

class AnalizadorPatrones:
    def __init__(self, texto="asdqweasd qwsda"):
        self.texto = texto

    def encontrar_palabras(self, texto, patron):
        palabras = texto.split()
        resultado = []
        for palabra in palabras:
            if palabra.startswith(patron):
                resultado.append(palabra)
        return resultado

    def agrupar_por_longitud(self, texto):
        palabras = texto.split()
        grupos = {}
        for palabra in palabras:
            longitud = len(palabra)
            if longitud not in grupos:
                grupos[longitud] = []
            grupos[longitud].append(palabra)
        return grupos   # <- CORREGIDO: fuera del for, no dentro

    def palabras_unicas(self):
        palabras = self.texto.split()
        unicas = set(palabras)
        return unicas   # si se quiere lista, sería: return list(unicas)


ana1 = AnalizadorPatrones()
print(ana1.encontrar_palabras("el gato de mi casa es una gata", "ga"))
res = ana1.agrupar_por_longitud("la casa de la esquina")
print(res)
unic = ana1.palabras_unicas()
print(unic)