"""
6. Escribir una función que reciba una lista de tuplas, por ejemplo:

[('George', '4312 Abbey Road',22), ('John','54 Love Ave', 21)]

La función deberá generar un archivo CSV (separado por comas) en donde cada línea será un ítem
de la lista, el archivo debera contener:

name,address,age
George,4312 Abbey Road,22
John,54
Love Ave,21
"""
path="/home/franco-unt/Documents/14CESE2021/DASO/Guia_de_Ejercicios_Python/test.csv"

import csv

l= [('franco','m',25),('valeria','f',28),('flor','f',24),('Ethan','m',30)]

with open(path,'w') as out:
    csv_out =csv.writer(out)
    csv_out.writerow(['Nombre','Sexo','Edad'])
    for row in l:
        csv_out.writerow(row)