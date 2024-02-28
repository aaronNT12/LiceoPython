def main():
    # Crear un array de 10 posiciones
    numeros = [0] * 10

    # Rellenar el array con valores introducidos por el usuario
    for i in range(10):
        numeros[i] = int(input(f"Introduce el elemento {i + 1}: "))

    # Mostrar los elementos del array
    print("Los elementos del array son:")
    for i in range(10):
        print(f"Elemento {i + 1}: {numeros[i]}")

if __name__ == "__main__":
    main()
