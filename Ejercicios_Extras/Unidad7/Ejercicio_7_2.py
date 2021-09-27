"""
a) Escribir una función que indique si dos fichas de dominó encajan o no. Las fichas son recibidas
en dos tuplas, por ejemplo: (3,4) y (5,4)
b) Escribir una función que indique si dos fichas de dominó encajan o no. Las fichas son recibidas
en una cadena, por ejemplo: 3-4 2-5. Nota: utilizar la función split de las cadenas.
"""
#a)
def get_match_domino_records(ficha_a,ficha_b):
    ret=False
    if(ficha_a[0]==ficha_b[0] or ficha_a[0]==ficha_b[1]):
        ret=True
    else:
        if(ficha_a[1]==ficha_b[0] or ficha_a[1]==ficha_b[1]):
            ret=True
    return ret

if(get_match_domino_records((3,4),(0,2))):
    print("Las fichas pueden encajar")
else:
    print("Las fichas no pueden encajar")