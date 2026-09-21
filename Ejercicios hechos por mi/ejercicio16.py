#intento 1...
#--------------------Ejercicio propuesto:------------------------
# Clase CodificadorRot que:

# Tenga método codificar_letra(letra, desplazamiento) igual al cifrado César.
# Tenga método decodificar_letra(letra, desplazamiento) que reutilice codificar_letra pero con 
# el desplazamiento invertido (negativo).
# Tenga método decodificar_palabra(palabra, desplazamiento) para toda la palabra, guardando 
# historial en un diccionario.
#-----------------------------EPS---------------------------------
#Entrada:
#palabra codificada, y el desplazamiento original que se usó
#Proceso:
#aplicar el desplazamiento contrario (negativo) para deshacer la codificación
#Salida:
#la palabra original (decodificada)

#-----------------------bosquejo----------------------------------
# BOSQUEJO (traza de codificar_letra("v", 5), para entender la base del cifrado):
# "v" es minúscula -> base = ord('a') = 97
# ord("v") = 118
# nueva = (118 - 97 + 5) % 26 + 97 = 26 % 26 + 97 = 0 + 97 = 97 -> "a"
#
# BOSQUEJO (traza de decodificar_palabra("hfrnqf", 5)):
# decodificar_letra reutiliza codificar_letra, pero con desplazamiento NEGATIVO (-5)
# h -> (ord('h')-97-5)%26+97 = c
# f -> (ord('f')-97-5)%26+97 = a
# r -> ... = m
# n -> ... = i
# q -> ... = l
# f -> ... = a
#
# resultado: "camila"  (la palabra original antes de codificarla con desplazamiento 5)
#----------------------Codigo--------------------------------------------------
class CodificadorRot:
    def __init__(self):
        self.historial = {}

    def codificar_letra(self, letra, desplazamiento):
        if letra.isalpha():
            base = ord('a') if letra.islower() else ord('A')
            return chr((ord(letra) - base + desplazamiento) % 26 + base)
        return letra

    def decodificar_letra(self, letra, desplazamiento):
        return self.codificar_letra(letra, -desplazamiento)

    def decodificar_palabra(self, palabra, desplazamiento):
        resultado = ""
        for letra in palabra:
            resultado += self.decodificar_letra(letra, desplazamiento)
        self.historial[palabra] = resultado
        return resultado


cr = CodificadorRot()
print(cr.codificar_letra("v", 5))
print(cr.decodificar_palabra("hfrnqf", 5))   # "camila"