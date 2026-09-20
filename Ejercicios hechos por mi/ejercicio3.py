#intento 2...
#--------------------Ejercicio propuesto:------------------------
# Clase Biblioteca que:

# Tenga método agregar_libro(titulo, paginas) que guarde en un diccionario {titulo: paginas}.
# Tenga método total_paginas() que retorne la suma de todas las páginas.
# Tenga método libros_extensos(minimo) que retorne una lista con los títulos 
# cuyas páginas sean mayores al minimo dado (ojo: aquí es "mayor que", 
# no "menor que" como en el anterior — piensa bien qué símbolo usar).
#-----------------------------EPS---------------------------------
#Entrada:
#titulos y pag de libros
#Proceso:
#agregacion de los libros, suma total del total de las pag y verificacion de que libros son mas largos
#Salida:
#total de pag de todos libros e conjunto, libros con mas pag
#-----------------------bosquejo----------------------------------
#BOSQUEJO (traza de agregar_libro en orden):
# Paso 1 | titulo="manual de como usar un machete" | paginas=15  | self.pag={"manual de como usar un machete":15}
# Paso 2 | titulo="ciencuenta sombras de grey"      | paginas=550 | self.pag={..., "ciencuenta sombras de grey":550}
# Paso 3 | titulo="cocina lvl 2"                    | paginas=232 | self.pag={..., "cocina lvl 2":232}
# Paso 4 | titulo="mushoku tensei vol 15"           | paginas=380 | self.pag={..., "mushoku tensei vol 15":380}
#
# total_paginas() = 15+550+232+380 = 1177
#
# libros_extensos(200) -> recorre con .items():
# titulo="manual de como usar un machete" paginas=15  | 15 > 200? No  -> no entra
# titulo="ciencuenta sombras de grey"     paginas=550 | 550 > 200? Sí -> entra
# titulo="cocina lvl 2"                   paginas=232 | 232 > 200? Sí -> entra
# titulo="mushoku tensei vol 15"          paginas=380 | 380 > 200? Sí -> entra
# resultado = ["ciencuenta sombras de grey", "cocina lvl 2", "mushoku tensei vol 15"]
#----------------------Codigo--------------------------------------------------
class Biblioteca:
    def __init__(self):
        self.pag = {}

    def agregar_libro(self, titulo, paginas):
        self.pag[titulo] = paginas


    def total_paginas(self):
        return sum(self.pag.values())


    def libros_extensos(self,minimo):
        resultado = []
        
        for titulo,paginas in self.pag.items():
            if paginas > minimo:           
                resultado.append(titulo)
        return resultado


bibl = Biblioteca()

bibl.agregar_libro("manual de como usar un machete", 15)
bibl.agregar_libro("ciencuenta sombras de grey", 550)
bibl.agregar_libro("cocina lvl 2", 232)
bibl.agregar_libro("mushoku tensei vol 15", 380)

print("total de pag por todos los libros: ",bibl.total_paginas())
print("libros con mas de 200 pag:", bibl.libros_extensos(200))

#comentario:
#resulta que reutilizar codigo que ya uno entiende para que sirve es muy facil...
#de hecho en el primer intento fue culpa mia por no atender muy bien que decia el enunciado...