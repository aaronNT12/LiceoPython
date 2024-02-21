# Pedir un número entero positivo por pantalla
num = int(input("Introduce un número entero positivo: "))

# Comprobar si el número es par o impar
if num % 2 == 0:
    # Si el resto de dividir el número entre 2 es 0, es par
    print("El número es par")
else:
    # Si no, es impar
    print("El número es impar")
