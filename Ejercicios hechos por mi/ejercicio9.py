#intento1
#--------------------Ejercicio propuesto:------------------------
# Clase ValidadorContrasenas que:

# Tenga método es_simbolo(caracter) que retorne True si el carácter NO es letra y NO es número.
# Tenga método analizar_contrasena(contrasena) que recorra carácter por carácter, reutilice 
# es_simbolo, y retorne un diccionario {'letras': cant, 'numeros': cant, 'simbolos': cant}, 
# guardando esos conteos como atributos.
# Tenga método es_segura() que retorne True solo si hay al menos un número Y al menos un símbolo 
# (usando los atributos ya guardados, sin volver a recorrer).
#-----------------------------EPS---------------------------------
#Entrada:
#una contraseña (texto)
#Proceso:
#recorrer carácter por carácter, clasificar en letra/número/símbolo
#Salida:
#diccionario con los 3 conteos; True/False si es segura
#-----------------------bosquejo----------------------------------
# BOSQUEJO (traza de analizar_contrasena("Valheim2024#")):
# V(letra) a(letra) l(letra) h(letra) e(letra) i(letra) m(letra) -> letras=7
# 2,0,2,4 -> numeros=4
# # -> no es letra, no es digito -> es_simbolo=True -> simbolos=1
#
# resultado: {'letras':7, 'numeros':4, 'simbolos':1}
# self.numeros=4, self.simbolos=1
# es_segura(): numeros>0? Sí Y simbolos>0? Sí -> True
#----------------------Codigo--------------------------------------------------
class ValidadorContrasenas:
    def __init__(self):
        self.letras = 0
        self.numeros = 0
        self.simbolos = 0

    def es_simbolo(self, caracter):
        return not caracter.isalpha() and not caracter.isdigit()

    def analizar_contrasena(self, contrasena):
        letras = numeros = simbolos = 0
        for c in contrasena:
            if c.isalpha():
                letras += 1
            elif c.isdigit():
                numeros += 1
            elif self.es_simbolo(c):
                simbolos += 1
        self.letras, self.numeros, self.simbolos = letras, numeros, simbolos
        return {'letras': letras, 'numeros': numeros, 'simbolos': simbolos}

    def es_segura(self):
        return self.numeros > 0 and self.simbolos > 0


vc = ValidadorContrasenas()
print(vc.analizar_contrasena("Valheim2024#"))
print(vc.es_segura())