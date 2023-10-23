import math
# Ingresamos los metros
altura = float(input("Ingrese los metros de caida: "))
gravedad = 9.81
tiempo = math.sqrt((2 * altura)/gravedad)
# Imprime el resultado
print(f"El tiempo de caida libre desde {altura} metros, sera el tiempo de caida de {tiempo:.2f} segundos")
