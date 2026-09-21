#intento 1...

#--------------------Ejercicio propuesto:------------------------
# Clase ClasificadorIMC que:

# Tenga método clasificar_imc(imc) que retorne la categoría ("bajo", "normal", "alto", "obeso") 
# según rangos de IMC.
# Tenga método agrupar_por_categoria(*imcs) que retorne un diccionario {categoría: [imcs]}.
# Tenga método promedio_categoria(categoria).
#-----------------------------EPS---------------------------------
#Entrada:
#valores de IMC en lote
#Proceso:
#clasificar cada valor con if/elif según su rango; agrupar en diccionario por categoría
#Salida:
#diccionario agrupado por categoría, promedio de una categoría

#-----------------------bosquejo----------------------------------
# BOSQUEJO (traza de agrupar_por_categoria(19.2, 23.5, 27.8, 31.4, 24.1)):
# imc=19.2 | <18.5? No, <25? Sí -> "normal" -> grupos={"normal":[19.2]}
# imc=23.5 | <25? Sí -> "normal"            -> grupos={"normal":[19.2,23.5]}
# imc=27.8 | <25? No, <30? Sí -> "alto"     -> grupos={..., "alto":[27.8]}
# imc=31.4 | <30? No -> "obeso"             -> grupos={..., "obeso":[31.4]}
# imc=24.1 | <25? Sí -> "normal"            -> grupos={"normal":[19.2,23.5,24.1], "alto":[27.8], "obeso":[31.4]}
#
# resultado: {'normal':[19.2,23.5,24.1], 'alto':[27.8], 'obeso':[31.4]}
# promedio_categoria("normal") = (19.2+23.5+24.1)/3 = 22.27
#----------------------Codigo--------------------------------------------------
class ClasificadorIMC:
    def clasificar_imc(self, imc):
        if imc < 18.5:
            return "bajo"
        elif imc < 25:
            return "normal"
        elif imc < 30:
            return "alto"
        else:
            return "obeso"

    def agrupar_por_categoria(self, *imcs):
        grupos = {}
        for imc in imcs:
            categoria = self.clasificar_imc(imc)
            if categoria not in grupos:
                grupos[categoria] = []
            grupos[categoria].append(imc)
        self.grupos = grupos
        return grupos

    def promedio_categoria(self, categoria):
        if categoria not in self.grupos or len(self.grupos[categoria]) == 0:
            return 0
        return sum(self.grupos[categoria]) / len(self.grupos[categoria])


ci = ClasificadorIMC()
print(ci.agrupar_por_categoria(19.2, 23.5, 27.8, 31.4, 24.1))
print(ci.promedio_categoria("normal"))