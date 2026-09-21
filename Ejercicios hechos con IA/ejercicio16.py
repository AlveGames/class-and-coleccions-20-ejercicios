#--------------------Ejercicio propuesto:------------------------
# Clase CodificadorCesar que: 
# (1) tenga método codificar_letra(letra, desplazamiento) que 
# retorne la letra desplazada en el alfabeto (usar operador %); 
# (2) tenga método 
# codificar_palabra(palabra, desplazamiento) que reutilice para toda la palabra; 
# (3) tenga un diccionario como atributo para historial de codificaciones.

#-----------------------------EPS---------------------------------
#Entrada:
#una letra o palabra, y un número de desplazamiento (1-25)
#Proceso:
#convertir la letra a su código numérico (ord), desplazarla con %, volver a convertir a letra (chr)
#Salida:
#palabra codificada; se guarda en un diccionario historial

#-----------------------bosquejo----------------------------------
# BOSQUEJO (traza de codificar_letra("h", 3)):
# "h" es minúscula -> base = ord('a') = 97
# ord("h") = 104
# nueva = (104 - 97 + 3) % 26 + 97 = (10) % 26 + 97 = 10 + 97 = 107
# chr(107) = "k"
#
# Se repite para cada letra de "hola" con desplazamiento 3:
# h -> k
# o -> r
# l -> o
# a -> d
# resultado: "krod"
#----------------------Codigo--------------------------------------------------

class CodificadorCesar:
    def __init__(self):
        self.historial = {}

    def codificar_letra(self, letra, desplazamiento):
        if letra.isalpha():
            base = ord('a') if letra.islower() else ord('A')   # distingue mayúscula/minúscula
            nueva = (ord(letra) - base + desplazamiento) % 26 + base
            return chr(nueva)
        return letra   # si no es letra (ej. espacio), la deja igual

    def codificar_palabra(self, palabra, desplazamiento):
        resultado = ""
        for letra in palabra:
            resultado += self.codificar_letra(letra, desplazamiento)
        self.historial[palabra] = resultado
        return resultado


cc = CodificadorCesar()
print(cc.codificar_letra("h", 3))
print(cc.codificar_palabra("hola", 3))