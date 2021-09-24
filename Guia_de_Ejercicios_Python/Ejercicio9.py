"""
9. Crear un módulo llamado “myconfig”. Poner dentro del módulo las funciones para leer y escribir
el archivo de configuración. Crear un programa Main.py que importe el módulo y pruebe sus
funciones.
"""
import myconfig

d=myconfig.get_dic("config.txt")

print(d)

e = {"dia":"lunes","ahorro":30,"peso":89.30,"Good":"bye"}

myconfig.dic2txt(e,"config.txt")