#Clase AnalizadorString que: 
# (1) tenga método solo_vocales(letra) que retorne True si es vocal; 
# (2) tenga método contar_por_tipo(texto) que retorne un diccionario {'vocales': cant, 'consonantes': cant, 'digitos': cant} reutilizando métodos; 
# (3) tenga atributo que guarde el texto más largo analizado.


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