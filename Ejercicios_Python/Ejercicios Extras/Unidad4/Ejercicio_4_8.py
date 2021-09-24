"""
Ejercicio 4.8. Programa de astrología: el usuario debe ingresar el día y mes de su cumpleaños y el pro-
grama le debe decir a que signo corresponde.
Nota:
Aries: 21 de marzo al 20 de abril.
Tauro: 21 de abril al 20 de mayo.
Geminis: 21 de mayo al 21 de junio.
Cancer: 22 de junio al 23 de julio.
Leo: 24 de julio al 23 de agosto.
Virgo: 24 de agosto al 23 de septiembre.
Libra: 24 de septiembre al 22 de octubre.
Escorpio: 23 de octubre al 22 de noviembre.
Sagitario: 23 de noviembre al 21 de diciembre.
Capricornio: 22 de diciembre al 20 de enero.
Acuario: 21 de enero al 19 de febrero.
Piscis: 20 de febrero al 20 de marzo.
"""

def obtener_signo(dia,mes):
    rango_fechas=[[[21,3],[20,4],"Aries"],[[21,4],[20,5],"Tauro"],[[21,5],[21,6],"Geminis"],[[22,6],[23,7],"Cancer"],[[24,7],[23,8],"Leo"],[[24,8],[23,9],"Virgo"],[[24,9],[22,10],"Libra"],[[23,10],[22,11],"Escorpio"],[[23,11],[21,12],"Sagitario"],[[22,12],[20,1],"Capricornio"],[[21,1],[19,2],"Acuario"],[[20,2],[20,3],"Piscis"]]
    encontre_signo=False
    indice=-1
    for i in range(0,12):
        tupla_fecha=rango_fechas[i][0]
        if(tupla_fecha[1]==mes):
            if(dia>=tupla_fecha[0]):
                encontre_signo=True
                indice=i
        else:
            tupla_fecha=rango_fechas[i][1]
            if(tupla_fecha[1]==mes):
                if(dia<=tupla_fecha[0]):
                    encontre_signo=True
                    indice=i
    return rango_fechas[indice][2]

dia=int(input("Ingrese el dia de su cumpleaños:  "))
mes=int(input("Ingrese el mes de su cumpleaños:  "))

print("Según tu fecha de cumpleaños eres: ==>",obtener_signo(dia,mes))