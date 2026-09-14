class NumeroPrimo:
    """Clase para validar números primos y guardar historial de búsquedas."""
    
    def __init__(self):
        # Historial: lista que guarda todos los números verificados
        self.historial = []
    
    def es_primo(self, numero):
        """Retorna True si numero es primo, False en caso contrario."""
        # Agregar a historial
        self.historial.append(numero)
        
        # Casos especiales
        if numero < 2:
            return False
        
        # Comprobar divisores desde 2 hasta sqrt(numero)
        for divisor in range(2, int(numero ** 0.5) + 1):
            if numero % divisor == 0:
                return False
        
        return True
    
    def primos_en_rango(self, *args):
        "Retorna una lista con los números primos de los pasados en *args."
        primos = []
        for numero in args:
            if self.es_primo(numero):
                primos.append(numero)
        return primos
    
    def cantidad_verificados(self):
        "Retorna cuántos números se han verificado."
        return len(self.historial)
    
    def limpiar_historial(self):
        "Borra el historial."
        self.historial = []


# --- Programa principal ---
np = NumeroPrimo()

# Probar un número individual
resultado = np.es_primo(7)
print(f"¿7 es primo? {resultado}")

# Probar varios números a la vez
primos = np.primos_en_rango(10, 11, 12, 13, 14, 15)
print(f"Primos en el rango [10-15]: {primos}")

# Ver historial y cantidad
print(f"Historial: {np.historial}")
print(f"Total verificados: {np.cantidad_verificados()}")