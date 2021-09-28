"""
Modelar una clase Mate que describa el funcionamiento de la conocida bebida tradicional
local. La clase debe contener como miembros:
a) Un atributo para la cantidad de cebadas restantes hasta que se lava el mate (representada por un
número).
b) Un atributo para el estado (lleno o vacío).
c) El constructor debe recibir como parámetro n, la cantidad máxima de cebadas en base a la
cantidad de yerba vertida en el recipiente.
d) Un método cebar, que llena el mate con agua. Si se intenta cebar con el mate lleno, se debe
lanzar una excepción que imprima el mensaje Çuidado! Te quemaste!"
e) Un método beber, que vacía el mate y le resta una cebada disponible. Si se intenta beber un
mate vacío, se debe lanzar una excepción que imprima el mensaje . El mate está vacío!"
f) Es posible seguir cebando y bebiendo el mate aunque no haya cebadas disponibes. En ese caso la
cantidad de cebadas restantes se mantendrá en 0, y cada vez que se intente beber se debe imprimir
un mensaje de aviso: . A dvertencia: el mate está lavado.", pero no se debe lanzar una excepción.
"""

class Mate:
    def __init__(self,numCebadas):
        if(numCebadas!=0):
            self.cebadasMax=numCebadas
            self.estado="vacio"
            self.cebadasDisp=0
        else:
            raise TypeError("La cantidad maxima de cebadas no puede ser cero")
    def __str__(self):
        return "El mate soporta %d cebadas como maximo, esta %s y tiene %d cebadas disponible"%(self.cebadasMax,self.estado,self.cebadasDisp)
    def cebar(self):
        if self.estado=="lleno":
            raise TypeError("Te quemaste!!")
        else:
            self.estado="lleno"
            self.cebadasDisp=self.cebadasMax
    def beber(self):
        if(self.estado!="vacio"):
            self.cebadasDisp=self.cebadasDisp-1
            if(self.estado=="lleno"):
                self.estado="tiene Agua"
            if(self.cebadasDisp==0):
                self.estado="vacio"
        else:
            print("El mate esta vacio")

mate_franco=Mate(3)
print(mate_franco)
mate_franco.cebar()
print(mate_franco)
mate_franco.beber()
print(mate_franco)
mate_franco.beber()
print(mate_franco)
mate_franco.beber()
print(mate_franco)
mate_franco.beber()
