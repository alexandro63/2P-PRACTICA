# Ingrese base y altura de un trapecio
altura = float(input("Ingrese la altura: "))
baseA = float(input("Ingrese la base A: "))
baseB = float(input("Ingrese la base B: "))
# Calculamos
area = (baseA + baseB) * altura/2
# Imprime el resultado
print(f"El área del trapecio de {area:.2f}")