class AnalizadorTexto:
    def __init__(self):
        self.set_palabras = set()   # conjunto: guarda solo palabras únicas
        self.lista_palabras = []    # lista: guarda todas, en orden (con repetidos)

    def agregar_palabra(self, palabra):
        self.set_palabras.add(palabra)      # el set descarta duplicados solo
        self.lista_palabras.append(palabra) # la lista guarda todo, en orden

    def contar_palabras(self):
        return len(self.set_palabras)       # cuántas hay ÚNICAS en el conjunto

    def agregar_multiples(self, *args):
        for palabra in args:
            self.agregar_palabra(palabra)   # reutiliza el método 1, palabra por palabra


# Programa principal
at = AnalizadorTexto()
at.agregar_multiples("hola", "mundo", "hola")
print(at.contar_palabras())   # 2
print(at.lista_palabras)      # ['hola', 'mundo', 'hola']  ← con repetido
print(at.set_palabras)        # {'hola', 'mundo'}          ← sin repetido