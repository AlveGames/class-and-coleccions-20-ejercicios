#intento 1...
#--------------------Ejercicio propuesto:------------------------
# Clase MezcladorTexto que:

# Tenga método intercalar_letras(palabra1, palabra2) que retorne un texto alternando letras 
# de ambas palabras.
# Tenga método intercalar_multiples(*palabras) que reutilice el anterior para varias palabras.
#-----------------------------EPS---------------------------------
#Entrada:
#dos o más palabras
#Proceso:
#recorrer con índices, alternando una letra de cada palabra
#Salida:
#un solo texto con las letras intercaladas

#-----------------------bosquejo----------------------------------
# BOSQUEJO (traza de intercalar_letras("valheim", "es")):
# largo_max = max(7,2) = 7
# i=0 | palabra1[0]="v" -> resultado="v" | palabra2[0]="e" -> resultado="ve"
# i=1 | palabra1[1]="a" -> resultado="vea" | palabra2[1]="s" -> resultado="veas"
# i=2 | palabra1[2]="l" -> resultado="veasl" | i<len(palabra2)? No, ya no hay más
# i=3 | palabra1[3]="h" -> resultado="veaslh"
# i=4 | palabra1[4]="e" -> resultado="veaslhe"
# i=5 | palabra1[5]="i" -> resultado="veaslhei"
# i=6 | palabra1[6]="m" -> resultado="veaslheim"
#
# resultado: "veaslheim"
#
# BOSQUEJO (traza de intercalar_multiples("gato","sol","rey")):
# paso 1: resultado = "gato" (primera palabra, sin intercalar aún)
# paso 2: intercalar_letras("gato","sol") -> "gsaotlo"
# paso 3: intercalar_letras("gsaotlo","rey") -> "grseayotlo"
# resultado final: "grseayotlo"
#----------------------Codigo--------------------------------------------------
class MezcladorTexto:
    def intercalar_letras(self, palabra1, palabra2):
        resultado = ""
        largo_max = max(len(palabra1), len(palabra2))
        for i in range(largo_max):
            if i < len(palabra1):
                resultado += palabra1[i]
            if i < len(palabra2):
                resultado += palabra2[i]
        return resultado

    def intercalar_multiples(self, *palabras):
        resultado = palabras[0]
        for i in range(1, len(palabras)):
            resultado = self.intercalar_letras(resultado, palabras[i])
        return resultado


mt = MezcladorTexto()
print(mt.intercalar_letras("valheim", "es"))
print(mt.intercalar_multiples("gato", "sol", "rey"))