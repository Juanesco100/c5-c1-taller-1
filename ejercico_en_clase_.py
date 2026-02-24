# ejercicio en clase 

registro_persona = input("¿Cuantas personas desea registrar?: ")
registro_persona = int(registro_persona)

for i in range(registro_persona):
    nombre = input("Ingresa tu nombre: ")
    edad = input("ingresa tu edad: ")
    edad_entero = int(edad)
    tieneConocimiento = input("Tienes conocimientos basicos de computación? (s/n): ")
    print("\n")

    if edad_entero > 15 and tieneConocimiento == "s":
        print("Puede participar en el taller.")
        print("\n")
    else:
        print("No cumple los requisitos.")
        print("\n")


continuar = True

while continuar :

    if edad_entero < 15:
        print("Edad no validad, es menor.")
        edad_entero = input("Ingrese nuevamente la edad: ")
        edad_entero = int(edad_entero)
    else:
        print ("Proceso finalizado!...")
        print("\n")
        continuar = False
        
print("hola mundo")
