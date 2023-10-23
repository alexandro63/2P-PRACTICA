# Ingresar las preguntas
p1 = input("Ingresa tu nombre: ")
p2 = int(input("Ingresa tu edad: "))
p3 = input("Ingresa tu cuidad: ")
p4 = input("Ingresa yu hobby: ")
p5 = bool(input("¿Te gusta programar? (si = 1/no = 0):" ))
# Logica
if p5 == 1:
    sn = "si"
else:
    sn = "no"
# Imprime el mensaje
print(f"Bienvenido a la clase de Introducción a la informática {p1}, tu edad es: {p2} años, eres de la cuidad de: {p3}, tu hobby es: {p4} y te gusta el fultbol: {sn}")