def imprimir_impares_en_intervalo():
    #Solicitar límites inferior y superior
    
    a = int(input("Introduce el límite interior: "))
    b = int(input("Introduce el límite superior: "))
    
    # Verificar si a < b y, si no, invertir los valores
    
    if a > b:
        a, b = b, a
        
    print(f"Números impares entre {a} y {b}:")
    
    # Iterar a través del rango y mostrar los números impares
    
    for num in range(a, b + 1):
        if num % 2 != 0:
            print(num)
            
# Llamar a la función principal
imprimir_impares_en_intervalo()

# OTRA VERSIÓN DEL PROGRAMA

# Solicitar límites inferior y superior
a = int(input("Introduce el límite inferior: "))
b = int(input("Introduce el límite superior: "))

# Verificar si a < b y, si no, invertir los valores
if a > b:
    a, b = b, a

print(f"Números impares entre {a} y {b}:")

# Iterar a través del rango y mostrar los números impares
current_num = a
while current_num <= b:
    if current_num % 2 != 0:
        print(current_num)
    current_num += 1
