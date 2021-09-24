"""
Ejercicio 3.1. Escribir dos funciones que permitan calcular:
a) La cantidad de segundos en un tiempo dado en horas, minutos y segundos.
b) La cantidad de horas, minutos y segundos de un tiempo dado en segundos.
"""

def get_seconds(h,m,s):
    sec = h*3600+m*60+s
    return sec

def get_time_h_m_s(sec):
    h=sec//3600
    sec=sec-h*3600
    m=sec//60
    sec=sec-m*60
    s=sec
    hora_actual = "%d:%d:%d"%(h,m,s)
    return hora_actual

horas=int(input("Ingrese la hora"))
while(horas<0 or horas>24):
    print("número invalido")
    horas=int(input("Ingrese la hora"))
minutos=int(input("Ingrese los minutos"))
while(minutos<0 or minutos>60):
    print("número invalido")
    minutos=int(input("Ingrese la hora"))
segundos=int(input("Ingrese los segundos"))
while(segundos<0 or segundos>60):
    print("número invalido")
    segundos=int(input("Ingrese la hora"))

res = get_seconds(horas,minutos,segundos)
print("la cantidad desegundo es: ",res)
hora_str=get_time_h_m_s(85813)
print(str(hora_str))