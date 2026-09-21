#intento 2...
#--------------------Ejercicio propuesto:------------------------
# Clase ClasificadorVentas que:

# Tenga método es_venta_alta(monto) que retorne True si el monto es mayor o igual a 100, False en caso contrario.
# Tenga método clasificar_ventas(*montos) que reutilice es_venta_alta y retorne {'altas': [...], 'bajas': [...]}.
# Tenga método promedio_por_categoria() que retorne una tupla (promedio_altas, promedio_bajas). 
# Si algún grupo está vacío, ese promedio debe ser 0.
#-----------------------------EPS---------------------------------
#Entrada:
#montos de ventas (en lote, con *args)
#Proceso:
#clasificar cada monto en alta (>=100) o baja, reutilizando es_venta_alta;
#calcular promedio de cada grupo, evitando dividir entre cero si algún grupo está vacío
#Salida:
#diccionario {'altas':[...], 'bajas':[...]}, y una tupla (promedio_altas, promedio_bajas)
#-----------------------bosquejo----------------------------------
# BOSQUEJO (traza de clasificar_ventas(200,250,130,50,30,25)):
# monto=200 | es_venta_alta=True  | altas=[200]            | bajas=[]
# monto=250 | es_venta_alta=True  | altas=[200,250]        | bajas=[]
# monto=130 | es_venta_alta=True  | altas=[200,250,130]    | bajas=[]
# monto=50  | es_venta_alta=False | altas=[200,250,130]    | bajas=[50]
# monto=30  | es_venta_alta=False | altas=[200,250,130]    | bajas=[50,30]
# monto=25  | es_venta_alta=False | altas=[200,250,130]    | bajas=[50,30,25]
#
# promedio_por_categoria():
# len(altas)=3 (no vacío) -> promedio_altas = (200+250+130)/3 = 193.33
# len(bajas)=3 (no vacío) -> promedio_bajas = (50+30+25)/3 = 35.0
# resultado: (193.33, 35.0)
#
# Caso con grupo vacío -> clasificar_ventas(200, 300):
# altas=[200,300] | bajas=[]
# len(bajas)=0 (vacío) -> promedio_bajas = 0 (sin dividir, se evita el ZeroDivisionError)
# resultado: (250.0, 0)
#----------------------Codigo--------------------------------------------------
class ClasificadorVentas:

    def es_venta_alta(self,monto):
        if monto >= 100:
            return True
        else:
            return False

    def clasificar_ventas(self,*montos):
        altas = []
        bajas = []

        for numero in montos:
            if self.es_venta_alta(numero):
                altas.append(numero)
            else:
                bajas.append(numero)

        self.altas = altas
        self.bajas = bajas

        return {
            'altas': altas,
            'bajas' : bajas
        }

    def promedio_por_categoria(self):
        if len(self.altas) == 0:
            promedio_altas = 0
        else:
            promedio_altas = sum(self.altas) / len(self.altas)

        if len(self.bajas) == 0:
            promedio_bajas = 0
        else:
            promedio_bajas = sum(self.bajas) / len(self.bajas)

        return (promedio_altas, promedio_bajas)

venta = ClasificadorVentas()

print(venta.es_venta_alta(200))
print(venta.clasificar_ventas(100,200))
print(venta.promedio_por_categoria())