#intento 1...
#--------------------Ejercicio propuesto:------------------------
# Clase BuscadorTexto que:

# Tenga método buscar_terminaciones(texto, sufijo) que retorne las palabras que TERMINEN con 
# el sufijo (usa .endswith(), lo opuesto a .startswith()).
# Tenga método agrupar_por_primera_letra(texto) que retorne un diccionario {letra: [palabras]}.
# Tenga método letras_unicas(texto) que retorne un conjunto con las primeras letras, sin repetir.
#-----------------------------EPS---------------------------------
#Entrada:
#texto y un sufijo de búsqueda
#Proceso:
#split(), filtrar con endswith, agrupar por primera letra, eliminar duplicados con set
#Salida:
#lista de palabras, diccionario agrupado, conjunto de letras

#-----------------------bosquejo----------------------------------
# BOSQUEJO (traza de buscar_terminaciones("el guerrero recolecta madera y piedra", "era")):
# "el"        | endswith("era")? No
# "guerrero"  | endswith("era")? No
# "recolecta" | endswith("era")? No
# "madera"    | endswith("era")? Sí -> resultado=["madera"]
# "y"         | No
# "piedra"    | No
# resultado: ["madera"]
#
# BOSQUEJO (traza de agrupar_por_primera_letra, mismo texto):
# "el"->letra="e"        -> grupos={"e":["el"]}
# "guerrero"->letra="g"  -> grupos={..., "g":["guerrero"]}
# "recolecta"->letra="r" -> grupos={..., "r":["recolecta"]}
# "madera"->letra="m"    -> grupos={..., "m":["madera"]}
# "y"->letra="y"         -> grupos={..., "y":["y"]}
# "piedra"->letra="p"    -> grupos={..., "p":["piedra"]}
#
# letras_unicas() = {"e","g","r","m","y","p"}
#----------------------Codigo--------------------------------------------------
class BuscadorTexto:
    def buscar_terminaciones(self, texto, sufijo):
        palabras = texto.split()
        resultado = []
        for p in palabras:
            if p.endswith(sufijo):
                resultado.append(p)
        return resultado

    def agrupar_por_primera_letra(self, texto):
        palabras = texto.split()
        grupos = {}
        for p in palabras:
            letra = p[0]
            if letra not in grupos:
                grupos[letra] = []
            grupos[letra].append(p)
        return grupos

    def letras_unicas(self, texto):
        palabras = texto.split()
        letras = set()
        for p in palabras:
            letras.add(p[0])
        return letras


bt = BuscadorTexto()
print(bt.buscar_terminaciones("el guerrero recolecta madera y piedra", "era"))
print(bt.agrupar_por_primera_letra("el guerrero recolecta madera y piedra"))
print(bt.letras_unicas("el guerrero recolecta madera y piedra"))