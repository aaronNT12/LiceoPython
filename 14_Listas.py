milista = ["manzana","plátano","fresa"]
milista[1:2] = ["mandarina","limon"]
print(milista)
milista [1:3] = ["mandarina"]
print(milista)

lista1 = ["azul","rojo","negro"]
lista1.insert(0,"blanco")
print (lista1)

lista1.append("verde")
print(lista1)
lista1.extend(milista)
print(lista1)


# Eliminar elementos de una lista

lista1.remove("mandarina")
print(lista1)
lista1.pop(4)
print(lista1)
lista1.pop()
print(lista1)

# Elimina un elemento que especifiquemos de la lista
del lista1[1]
print(lista1)

# Eliminar completamente una lista
del lista1
print(lista1)

# Para vaciar una lista

lista2 = ["azul","rojo","negro"]
lista2.clear()
print(lista2)

# Bucles con Listas
lista1 = ["azul","rojo","negro"]
for contador in range(len(lista1)):
    print(lista1[contador])
    
    
for contador in range(len(lista1)):
    print(lista1[contador])
    break

for x in lista1:
    print(x)



