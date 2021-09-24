"""
Ejercicio 4.7. Escribir un programa que reciba como entrada un año escrito en números arábigos y
muestre por pantalla el mismo año escrito en números romanos.
Unidad=["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
Decena=["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
Centena=["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
Mil=["", "M", "MM"]
"""
#  0   1   2     3     4   5    6    7     8      9  
U=["","I","II","III","IV","V","VI","VII","VIII","IX"]

#   10  20    30   40   50  60   70     80    90   
D=["","X","XX","XXX","XL","L","LX","LXX","LIII","XC"]

#  100  200  300   400 500  600  700    800   900  
C=["","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"]

# 1000  2000 3000
M=["","M","MM","MMM"]

def convertir_año_dec2rom(numero):
    aux=numero
    año=[]
    while(aux):
        año.append(aux%10)
        aux=aux//10
    conversion=M[año[3]]+C[año[2]]+D[año[1]]+U[año[0]]
    return conversion

print("El año expresado en el sistema romano es ==>",convertir_año_dec2rom(1542))