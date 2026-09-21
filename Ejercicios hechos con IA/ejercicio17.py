#--------------------Ejercicio propuesto:------------------------
# Clase AgrupadorEdades que: 
# (1) tenga método clasificar_edad(edad) que retorne la categoría 
# ("niño", "adolescente", "adulto", "mayor"); 
# (2) tenga método agrupar_por_categoria(*edades) que retorne un diccionario con {categoría: [edades]}; 
# (3) tenga método edad_promedio_categoria(categoria).

#-----------------------------EPS---------------------------------
#Entrada:
#edades en lote
#Proceso:
#clasificar cada edad con if/elif según rango; agrupar en un diccionario por categoría
#Salida:
#diccionario agrupado por categoría, promedio de una categoría

#-----------------------bosquejo----------------------------------
# BOSQUEJO (traza de agrupar_por_categoria(5, 15, 30, 70)):
# edad=5  | clasificar_edad(5)="niño"        | grupos={"niño":[5]}
# edad=15 | clasificar_edad(15)="adolescente"| grupos={"niño":[5],"adolescente":[15]}
# edad=30 | clasificar_edad(30)="adulto"     | grupos={..., "adulto":[30]}
# edad=70 | clasificar_edad(70)="mayor"      | grupos={..., "mayor":[70]}
#
# resultado: {'niño':[5],'adolescente':[15],'adulto':[30],'mayor':[70]}
#----------------------Codigo--------------------------------------------------

class AgrupadorEdades:
    def clasificar_edad(self, edad):
        if edad <= 12:
            return "niño"
        elif edad <= 17:
            return "adolescente"
        elif edad <= 64:
            return "adulto"
        else:
            return "mayor"

    def agrupar_por_categoria(self, *edades):
        grupos = {}
        for edad in edades:
            categoria = self.clasificar_edad(edad)
            if categoria not in grupos:
                grupos[categoria] = []
            grupos[categoria].append(edad)
        self.grupos = grupos
        return grupos

    def edad_promedio_categoria(self, categoria):
        if categoria not in self.grupos or len(self.grupos[categoria]) == 0:
            return 0
        return sum(self.grupos[categoria]) / len(self.grupos[categoria])


ae = AgrupadorEdades()
print(ae.agrupar_por_categoria(5, 15, 30, 70))
print(ae.edad_promedio_categoria("adulto"))