divisor = 2

while True:
    num = int(input("Introduce un número: "))
    resto = num % divisor

    if resto == 0:
        print("El número ", num, " es par")
    else:
        print("El número ", num, " es impar")

    repetir = input("¿Quieres repetir el ejercicio? (s/n): ")
    if repetir.lower() != 's':
        break
