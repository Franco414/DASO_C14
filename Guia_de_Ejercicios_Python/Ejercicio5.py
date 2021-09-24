#5. Escribir una función que reciba un string y reemplace los espacios por un caracter que reciba por
#argumento. La función debera devolver el nuevo string.

def my_conversion_string(ptr,caracter):
    aux = list(ptr)
    for i in range(0,len(aux)):
        if aux[i] == ' ':
            aux[i] = caracter
    aux2 = "".join(aux)
    return aux2

msg = "hola como estas hoy?"

msg2=my_conversion_string(msg,'X')

print("string original")
print(msg)

print("string convertido")
print(msg2)