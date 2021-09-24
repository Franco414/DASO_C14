#2. Crear una lista vacía, imprimir el campo id, el tipo y el valor de la lista. Luego agregar un número
#a la lista y volver a imprimir id,tipo y valor. ¿Cuáles son las diferencias?

l = []

print(id(l)) #imprimir el id de la lista
print(type(l)) #imprimir el tipo de la lista
print(l) #imprimir la lista

l.append(5)

print(id(l))
print(type(l))
print(l) 

#solo cambio el valor de la lista, paso de no tener ningún elemento a tener solamente uno.