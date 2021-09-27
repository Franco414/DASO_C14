"""
Escribir un programa que vaya solicitando al usuario que ingrese nombres.
a) Si el nombre se encuentra en la agenda (implementada con un diccionario), debe mostrar el
teléfono y, opcionalmente, permitir modificarlo si no es correcto.
b) Si el nombre no se encuentra, debe permitir ingresar el teléfono correspondiente.
El usuario puede utilizar la cadena "*", para salir del programa.
"""
#a)
from hashlib import new


dic={"franco":"3874256781","Mercedes":"38142d381","Roberto":"3871452879","Zaida":"38742545678","Tamara":"3813324875","Luciana":"3875894671"}
def funcion_a(d):
    print("Bienvenido")
    continuar=True
    new_contact=False
    while(continuar):
        nombre=input("Por favor ingrese un nuevo nombre ==>")
        if(nombre=="*"):
            continuar=False
        else:
            if(d.get(nombre)!=None):
                tel_mostrar=d[nombre]
                print("El telefono de ==> %s es ==> %s"%(nombre,tel_mostrar))
                op=input("Desea modificarlo [y / n] ==> ")
                if(op.lower()=="y"):
                    print("ingrese el nuevo numero al finalizar presione enter ==>")
                    new_num=input()
                    while(new_num.isdigit()==False):
                        print("Numero invalido ingrese un nuevo numero")
                        new_num=input()
                    d[nombre]=new_num
                    print("El nuevo telefono de ==> %s es ==> %s"%(nombre,d[nombre]))
                    op="n"
            else:
                print("La persona %s no se encuentra registrada"%nombre)
                op=input("Desea registrarlo? [y /n")
                if(op.lower()=="y"):
                    new_contact=True
                    print("ingrese el nuevo numero al finalizar presione enter ==>")
                    new_num=input()
                    while(new_num.isdigit()==False):
                        print("Numero invalido ingrese un nuevo numero")
                        new_num=input()
                    d[nombre]=new_num
                op="n"
    print("Fin del programa")
    return

funcion_a(dic)