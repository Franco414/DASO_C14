"""
Escribir una función que reciba una cadena que contiene un largo número entero y de-
vuelva una cadena con el número y las separaciones de miles. Por ejemplo, si recibe ’1234567890’,
debe devolver ’1.234.567.890’.
"""
def my_function_slip_string(cadena):
    lista=[]
    count=0
    i=0
    while(i<len(cadena)):
        if(count==3):
            lista.append(".")
            count=0
        else:
            lista.append(cadena[i])
            i=i+1
            count=count+1
    ret="".join(lista)
    return ret

cad=my_function_slip_string("123456789")
print(cad)