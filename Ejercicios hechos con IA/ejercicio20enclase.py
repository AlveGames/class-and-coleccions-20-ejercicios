class AnalizadorPatrones:
    def __init__(self,texto = "asdqweasd qwsda"):
        self.texto = texto

    def encontrar_palabras(self, texto, patron):
        palabras = texto.split()
        resultado = []

        for palabra in palabras:
            if palabra.startswith(patron):
                resultado.append(palabra)

        return resultado


    def agrupar_por_longitud(self,texto):
        palabras = texto.split()
        grupos = {}

        for palabra in  palabras:
             longitud = len(palabra)
            
             if longitud not in grupos:
                grupos[longitud] = []
                
             grupos[longitud].append(palabra)
             
             return grupos
    
    
    def palabras_unicas(self):
        palabras = self.texto.split()
        unicas = set(palabras)


        return unicas   #si se quiere cambir a lista simplenente seria " return list(unicas) "
    
ana1 = AnalizadorPatrones()
print(ana1.encontrar_palabras("el gato de mi casa es una gata","ga"))
res = ana1.agrupar_por_longitud("la casa de la esquina")    
print(res)

unic = ana1.palabras_unicas()

print(unic)