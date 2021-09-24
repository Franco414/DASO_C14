"""
10. Crear una función que devuelva una lista con todas las tty del sistema. Utilizando el módulo
“os”, usar la función popen() para ejecutar el comando “ls /dev/tty*” y construir una lista en donde
en cada item tenga un string con la ruta de cada tty que se encuentra en el /dev
Ejemplo:
import os
cmdOut = os.popen('df -h').read()
"""
import os
cmdOut =os.popen('ls /dev/tty*').read()
lista = cmdOut.split("\n")
print(lista)