from math import sqrt
import math

palitos:int = 21 #La cantidad de palitos en total
numero:int = ((3*palitos) // 2) #"formula matemarica" sacada de chat gpt

filas_totales:int = math.ceil(sqrt(numero)) #raiz cuadrada del numero y luego lo redondeo hacia arriba
print(filas_totales)
