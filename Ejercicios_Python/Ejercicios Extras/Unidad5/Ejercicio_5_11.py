"""
Ejercicio 5.11. Escribir una función que reciba un dígito y un número natural, y decida numéricamente
si el dígito se encuentra en la notación decimal del segundo.
"""
def match_digit_into_number():
    n=int(input("Ingrese un numero"))
    d=int(input("Ingrese un digito"))
    aux=n
    res=False
    while(aux):
        if(aux%10==d):
            aux=0
            res=True
        aux=aux//10
    if(res):
        print("El digito ==> %d se encuentra en el numero ==> %d"%(d,n))
    else:
        print("El digito %d no se encuentra en el numero %d"%(d,n))

match_digit_into_number()