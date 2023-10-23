import math
# Ingresamos el radio de la esfera 
radio  = float(input("Ingrese radio de la esfera: "))
# Calculamos
volumen = (4/3) * math.pi * (radio ** 3)
# Imprime el resultado
print(f"El volumen de la esfera es: {volumen:.2f}")