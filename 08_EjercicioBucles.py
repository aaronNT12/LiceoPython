class Numero:
    def __init__(self, valor):
        self.valor = valor

    def es_mayor_que(self, otro_numero):
        return self.valor >= otro_numero.valor

def obtener_numero(mensaje):
    valor = int(input(mensaje))
    return Numero(valor)

while True:
    num1 = obtener_numero("Introduce primer número: ")
    num2 = obtener_numero("Introduce segundo número: ")
    num3 = obtener_numero("Introduce tercer número: ")

    if num1.es_mayor_que(num2) and num1.es_mayor_que(num3):
        print("El numero mayor es: ", num1.valor)
    elif num2.es_mayor_que(num1) and num2.es_mayor_que(num3):
        print("El numero mayor es: ", num2.valor)
    else:
        print("El numero mayor es: ", num3.valor)

    continuar = input("¿Deseas continuar? (s/n): ")
    if continuar.lower() != 's':
        break
