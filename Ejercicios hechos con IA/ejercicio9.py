#--------------------Ejercicio propuesto:------------------------
# Clase AnalizadorString que: 
# (1) tenga método solo_vocales(letra) que retorne True si es vocal; 
# (2) tenga método contar_por_tipo(texto) que retorne un diccionario 
# {'vocales': cant, 'consonantes': cant, 'digitos': cant} reutilizando métodos; 
# (3) tenga atributo que guarde el texto más largo analizado.

#-----------------------------EPS---------------------------------
#Entrada:
#texto para analizar
#Proceso:
#recorrer carácter por carácter, clasificar cada uno como vocal, consonante o dígito
#Salida:
#diccionario con los 3 conteos

#-----------------------bosquejo----------------------------------
# BOSQUEJO (traza de contar_por_tipo("Hola123")):
# self.texto_mas_largo="" -> len("Hola123")=7 > len("")=0? Sí -> self.texto_mas_largo="Hola123"
#
# c="H" | isdigit=False | isalpha=True  | solo_vocales("H")=False -> consonantes=1
# c="o" | isdigit=False | isalpha=True  | solo_vocales("o")=True  -> vocales=1
# c="l" | isdigit=False | isalpha=True  | solo_vocales("l")=False -> consonantes=2
# c="a" | isdigit=False | isalpha=True  | solo_vocales("a")=True  -> vocales=2
# c="1" | isdigit=True  |                                         -> digitos=1
# c="2" | isdigit=True  |                                         -> digitos=2
# c="3" | isdigit=True  |                                         -> digitos=3
#
# resultado: {'vocales':2, 'consonantes':2, 'digitos':3}
#----------------------Codigo--------------------------------------------------

class AnalizadorString:
    def __init__(self):
        self.texto_mas_largo = ""

    def solo_vocales(self, letra):
        return letra.lower() in "aeiou"

    def contar_por_tipo(self, texto):
        if len(texto) > len(self.texto_mas_largo):
            self.texto_mas_largo = texto

        vocales = 0
        consonantes = 0
        digitos = 0

        for c in texto:
            if c.isdigit():
                digitos += 1
            elif c.isalpha():
                if self.solo_vocales(c):
                    vocales += 1
                else:
                    consonantes += 1

        return {'vocales': vocales, 'consonantes': consonantes, 'digitos': digitos}


astr = AnalizadorString()
print(astr.contar_por_tipo("Hola123"))