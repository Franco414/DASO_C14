"""
Botella y Sacacorchos
a) Escribir una clase Corcho, que contenga un atributo bodega (cadena con el nombre de la bodega).
b) Escribir una clase Botella que contenga un atributo corcho con una referencia al corcho que la
tapa, o None si está destapada.
c) Escribir una clase Sacacorchos que tenga un método destapar que le reciba una botella, le saque
el corcho y se guarde una referencia al corcho sacado. Debe lanzar una excepción en el caso en
que la botella ya esté destapada, o si el sacacorchos ya contiene un corcho.
d) Agregar un método limpiar, que saque el corcho del sacacorchos, o lance una excepción en el
caso en el que no haya un corcho.
"""
class Corcho:
    def __init__(self,nombre_bodega):
        if len(nombre_bodega)!=0:
            self.bodega=nombre_bodega
        else:
            raise TypeError("Nombre de bodega vacia")
    def __str__(self):
        return "El nombre de la bodega es => " + str(self.bodega)

class Botella:
    def __init__(self,corcho):
        if len(corcho.bodega)!=0:
            self.BotellaTapada=corcho.bodega
        else:
            self.BotellaTapada=None
    
    def __str__(self):
        if(self.BotellaTapada==None):
            return "La botella esta destapada"
        else:
            return "la botella esta tapada y tiene el corcho " + str(self.BotellaTapada)

class SacaCorchos:
    corchoRef=None
    def __init__(self,botella="",corcho=""):
        self.botella=botella
        self.corchoEnTapa=corcho
    def __str__(self):
        return "Tengo la botella %s que tiene el corcho %s"%(str(self.botella),str(self.corchoEnTapa))
    def destapar(self):
        if self.corchoEnTapa==None:
            raise TypeError("La botella ya esta destapada")
        else:
            self.corchoRef=self.corchoEnTapa
            self.corchoEnTapa=None
    def limpiar(self):
        if self.corchoRef!=None:
            corchoRef=None
        else:
            raise TypeError("El sacacorcho no tiene un corcho")

corcho = Corcho("Estancia 1960")
print(corcho)

corcho2 = Corcho("Cafayate 1922")
print(corcho2)

botella = Botella(corcho)
print(botella)

sacaCorcho = SacaCorchos("Termidor",corcho2.bodega)
print(sacaCorcho)

sacaCorcho.destapar()
print(sacaCorcho)

sacaCorcho.limpiar()
print(sacaCorcho)