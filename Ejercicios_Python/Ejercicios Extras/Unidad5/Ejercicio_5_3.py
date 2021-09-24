"""
Ejercicio 5.3. Manejo de contraseñas
a) Escribir un programa que contenga una contraseña inventada, que le pregunte al usuario la con-
traseña, y no le permita continuar hasta que la haya ingresado correctamente.
b) Modificar el programa anterior para que solamente permita una cantidad fija de intentos.
c) Modificar el programa anterior para que después de cada intento agregue una pausa cada vez
mayor, utilizando la función sleep del módulo time.
d) Modificar el programa anterior para que sea una función que devuelva si el usuario ingresó o no
la contraseña correctamente, mediante un valor booleano (True o False).
"""
contraseña="abc123MEF"
#a)
def validar_contraseña():
    contraseña_OK=False
    error=False
    while(contraseña_OK==False):
        ptr=input("Ingrese la contraseña ==>")
        error=False
        if(len(ptr)==len(contraseña)):
            for i in range(0,len(ptr)):
                if ptr[i]!=contraseña[i]:
                    print("Contraseña Incorrecta!!")
                    break
            if(error==False):
                contraseña_OK=True
    print("Contraseña valida!!")

#validar_contraseña()
#b)
def validar_contraseña2():
    continuar=True
    n_intentos=5
    count_intentos=1
    contraseña_OK=False
    error=False
    while(continuar):
        if(contraseña_OK==False):
            ptr=input("Ingrese la contraseña ==>")
            error=False
            if(len(ptr)==len(contraseña)):
                for i in range(0,len(ptr)):
                    if ptr[i]!=contraseña[i]:
                        print("Contraseña Incorrecta!!")
                        break
                if(error==False):
                    contraseña_OK=True
                    continuar=False
                else:
                    if(count_intentos<n_intentos):
                        count_intentos=count_intentos+1
                    else:
                        continuar=False
            else:
                print("Contraseña Incorrecta!!")
                if(count_intentos<n_intentos):
                    count_intentos=count_intentos+1
                else:
                    continuar=False
    if contraseña_OK:
        print("Contraseña valida!!")
    else:
        print("Contraseña invalida!!! Ha pasado los intentos de ingreso al sistema")

#validar_contraseña2()

#c)
def validar_contraseña3():
    from time import sleep
    continuar=True
    n_intentos=5
    count_intentos=1
    contraseña_OK=False
    error=False
    pausa=1
    while(continuar):
        if(contraseña_OK==False):
            ptr=input("Ingrese la contraseña ==>")
            error=False
            if(len(ptr)==len(contraseña)):
                for i in range(0,len(ptr)):
                    if ptr[i]!=contraseña[i]:
                        error=True
                        break
            else:
                error=True
            if error:
                print("Contraseña Incorrecta.")
                if(count_intentos<n_intentos):
                    count_intentos=count_intentos+1
                    print("Espere %d segundos antes de ingresar una nueva contraseña"%(pausa*count_intentos))
                    sleep(pausa*count_intentos)
                else:
                    continuar=False
            else:
                contraseña_OK=True
                continuar=False
    if contraseña_OK:
        print("Contraseña valida!!")
    else:
        print("Contraseña invalida!!! Ha pasado los intentos de ingreso al sistema")

#validar_contraseña3()

#d)

def validar_contraseña4():
    from time import sleep
    continuar=True
    n_intentos=5
    count_intentos=1
    contraseña_OK=False
    error=False
    pausa=1
    ret=False
    while(continuar):
        if(contraseña_OK==False):
            ptr=input("Ingrese la contraseña ==>")
            error=False
            if(len(ptr)==len(contraseña)):
                for i in range(0,len(ptr)):
                    if ptr[i]!=contraseña[i]:
                        error=True
                        break
            else:
                error=True
            if error:
                print("Contraseña Incorrecta.")
                if(count_intentos<n_intentos):
                    count_intentos=count_intentos+1
                    print("Espere %d segundos antes de ingresar una nueva contraseña"%(pausa*count_intentos))
                    sleep(pausa*count_intentos)
                else:
                    continuar=False
            else:
                contraseña_OK=True
                continuar=False
    if contraseña_OK:
        ret=True
    return ret


if validar_contraseña4():
    print("Contraseña valida!!")
else:
    print("Contraseña invalida!!! Ha pasado los intentos de ingreso al sistema")