# Ingresar peso y altura
peso = float(input("Ingrese el peso en kilogramos: "))
altura = float(input("Ingrese la altura en metros: "))
# Calculamos imc
imc = peso / (altura ** 2)
# Imprime el resultado
print(f"Tu IMC es {imc:.2f}")
# Imprime el estado de salud según el peso
if imc < 18.5:
 print("Tienes un bajo peso")
elif imc >= 18.5 and imc < 24.9:
 print("Tienes un peso saludable")
elif imc >= 25 and imc < 29.9:
 print("Tienes sobrepeso")
else:
 print("Tienes obesidad")
 