# Pedir un número entre 0 y 10 por teclado
num = int(input("Introduce un número entre 0 y 10: "))

# Comprobar si el número está en el rango válido
while num < 0 or num > 10:
    # Si no, mostrar un mensaje de error y pedir otro número
    print("Error: el número no es correcto")
    num = int(input("Introduce otro número entre 0 y 10: "))

# Si el número está en el rango, mostrar su tabla de multiplicar
print(f"La tabla de multiplicar del {num} es:")
for i in range(1, 11):
    # Mostrar el producto de num por i
    print(f"{num} x {i} = {num * i}")

