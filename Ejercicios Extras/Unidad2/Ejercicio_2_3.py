"""
Ejercicio 2.3. Utilice el programa anterior para generar una tabla de conversión de temperaturas, desde
0 ◦ F hasta 120 ◦ F, de 10 en 10.
"""

def convertir_temp_F2C(f):
    aux=f-32
    c=aux*5/9
    return c

print("Tabla de conversión de temperaturas Fahrenheit a Celsius")
print("/===============================================================/")
print("   Temperatura en Fahrenheit  ||   Temperatura en Celsius   ")
print("/===============================================================/")
Tc=0
Tf=0
for i in range(0,10):
    Tc=convertir_temp_F2C(Tf)
    print("               %3d°F          ||            %3.2f°C"%(Tf,Tc))
    Tf=Tf+10