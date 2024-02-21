def suma_numeros():
    numero = int(input("Introduce un número entero: "))
    suma = sum(range(1, numero + 1))
    print(f"La suma de los números hasta {numero} es {suma}")

suma_numeros()
