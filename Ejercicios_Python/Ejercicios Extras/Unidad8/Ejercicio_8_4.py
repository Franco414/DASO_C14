"""
Se cuenta con una lista ordenada de productos, en la que uno consiste en una tupla de (identificador,
descripción, precio), y una lista de los productos a facturar, en la que cada uno consiste en una tupla de
(identificador, cantidad).
Se desea generar una factura que incluya la cantidad, la descripción, el precio unitario y el precio total
de cada producto comprado, y al final imprima el total general.
Escribir una función que reciba ambas listas e imprima por pantalla la factura solicitada.
"""
p1=("0001","Jabón Tocador",20)
p2=("0002","Kilo de bananas",45.5)
p3=("0003","Shampoo",120)
p4=("0004","Pasta dental",87.25)
p5=("0005","Arróz",25.99)
p6=("0006","Fideos",30.99)
p7=("0007","Desinfectante",144.99)
p8=("0008","Servilleta 3 rollos por unidad",69.99)
p9=("0009","Papel Higienico 6 rollos por unidad",79.99)
p10=("0010","Insecticida",85.99)
p11=("0011","Detergente",45.99)
p12=("0012","Lavandina",20.99)
p13=("0013","Toallas",255.5)
p14=("0014","Leche chocolatada",55.99)
p15=("0015","Cereal",69.99)
productos=[p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15]

lista_compras=[("0001",2),("0011",3),("0010",3),("0005",4),("0005",1),("0003",3),("0015",2),("0006",3),("0007",2)]

def facturacoin(compras,referencias):
    Total=0
    print("Factura de la compra")
    print("Descripción               Precio Unitario            Precio Total")
    print("                                 $                          $    ")
    for i in range(0,len(compras)):
        for j in range(0,len(referencias)):
            if(compras[i][0]==referencias[j][0]):
                Total=Total+compras[i][1]*referencias[i][2]
                print(referencias[i][1]+", "+"$"+str(referencias[i][2])+", $%3.2f"%(compras[i][1]*referencias[i][2]))
    print("Total: $%3.3f"%Total)

facturacoin(lista_compras,productos)