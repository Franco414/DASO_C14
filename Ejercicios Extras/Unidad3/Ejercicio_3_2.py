"""
Ejercicio 3.2. Usando las funciones del ejercicio anterior, escribir un programa que lea de teclado dos
tiempos expresados en horas, minutos y segundos; las sume y muestre el resultado en horas, minutos y
segundos por pantalla.
"""
def split_time(cadena):
    lista=[]
    i=0
    aux=0
    for i in range(0,len(cadena)):
        if(cadena[i]>='0' and cadena[i]<='9'):
            aux=aux*10
            aux=aux+int(cadena[i])
        else:
            lista.append(aux)
            aux=0
    lista.append(aux)
    return lista

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

tiempo=input("ingrese una hora en formato hh:mm:ss")
a=split_time(tiempo)
tiempo2=input("ingrese una hora en formato hh:mm:ss")
b=split_time(tiempo2)
s1=get_seconds(a[0],a[1],a[2])
s2=get_seconds(b[0],b[1],b[2])
res=s1+s2
hora_final=get_time_h_m_s(res)
print(hora_final)