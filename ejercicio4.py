import math
# Ingresamos el radio
r = float(input("Ingrese el radio del circulo: "))
# Calculamos
a  = math.pi * r ** 2
c = 2 * math.pi * r
# Imprime el resultado
print(f"El area del circulo es: {a:.2f}")
print(f"La circunferencia del circulo es: {c:.2f}")