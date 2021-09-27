"""
a) Escribir una función que reciba dos matrices y devuelva la suma.
b) Escribir una función que reciba dos matrices y devuelva el producto.
c) Escribir una función que opere sobre una matriz y mediante eliminación gaussiana devuelva una
matriz triangular superior.
d) Escribir una función que indique si un grupo de vectores, recibidos mediante una lista, son
linealmente independientes o no.
"""
#a)
def suma_matrices(matriz_A,matriz_B):
    matriz_C=[]
    lista=[]
    for i in range(0,len(matriz_A)):
        lista=[]
        for j in range(0,len(matriz_A[0])):
            aux=matriz_A[i][j]+matriz_B[i][j]
            lista.append(aux)
        matriz_C.append(lista)
    return matriz_C

a=[[1,2,3],[4,5,6],[7,8,9]]
b=[[1,2,3],[4,5,6],[7,8,9]]
c=suma_matrices(a,b)
for i in c:
    print(i)

#b)
def producto_de_matrices(a,b):
    fila_A=len(a)
    fila_B=len(b)
    col_a=len(a[0])
    col_b=len(b[0])
    f=[]
    prod=[]
    for i in range(0,fila_A):
        f=[]
        for c in range(0,col_b):
            aux=0
            for j in range(0,col_a):
                aux=aux+a[i][j]*b[j][c]
            f.append(aux)
        prod.append(f)
    return prod

print("Apartado b")
c=[]
c=producto_de_matrices(a,b)
for i in c:
    print(i)

#c)
def encontrar_matriz_superior(a):
    ban=True
    ban2=False
    fila_A=len(a)
    col_A=len(a[0])
    indice_fila=0
    indice_columna=0
    filas_revisadas=[]
    contador_filas_nulas=0
    contador=0
    while(contador<len(a)-contador_filas_nulas):
        pivot=a[indice_fila][indice_columna]
        if(pivot!=0):
            ban=False
            contador=contador+1
            filas_revisadas.append([indice_fila,indice_columna])
        else:
            if(indice_fila==fila_A and indice_columna==col_A):
                contador==len(a)
            else:
                cambiar_a=indice_fila
                ban2=False
                while(a[indice_fila][indice_columna]==0 and ban2==False):
                    indice_fila=indice_fila+1
                    if(indice_fila>=fila_A):
                            indice_fila=0
                            ban2=True
                            contador=len(a)
                    for c in range(0,len(filas_revisadas)):
                        if(indice_fila==filas_revisadas[c][0]):
                            indice_fila=indice_fila+1
                            if(indice_fila==fila_A):
                                indice_fila=0
                if ban2==False:
                    contador=contador+1
                    aux=a[cambiar_a]
                    a[cambiar_a]=a[indice_fila]
                    a[indice_fila]=aux
                    ban_no_nulo=False
                    for f in aux:
                        if d!=0:
                            ban_no_nulo=True
                    if ban_no_nulo:
                        contador_filas_nulas=contador_filas_nulas+1
                    indice_fila=cambiar_a
                    filas_revisadas.append([indice_fila,indice_columna])
                    pivot=a[indice_fila][indice_columna]
                    ban=True
        if(ban==False and ban2==False):
            i=indice_fila+1
            if(i==fila_A):
                i=0
                contador==len(a)
            else:
                while(i<fila_A):
                    mul=a[i][indice_columna]
                    for j in range(indice_columna,col_A):
                        a[i][j]=a[i][j]-a[indice_fila][j]*mul/pivot
                    i=i+1
                indice_fila=indice_fila+1
                if(indice_fila==fila_A):
                    indice_fila=0
                indice_columna=indice_columna+1
                if(indice_columna>=col_A):
                    indice_columna=col_A-1
    return

print("Apartado c")
v1=[5,1,3,4]
v2=[5,1,3,4]
v3=[5,1,3,4]
v4=[5,1,3,4]
d=[v1,v2,v3,v4]
encontrar_matriz_superior(d)
print("matrix")
for i in d:
    print(i)

#d)

def det_vect_son_li(vectores):
    aux=vectores
    encontrar_matriz_superior(aux)
    det=1
    for i in range(0,len(vectores)):
        for j in range(0,len(aux[0])):
            if(i==j):
                det=det*aux[i][i]
    if(det==0):
        ret=False
    else:
        ret=True
    return ret
print("Apartado d")
e=[[1,3,4,5],[4,7,9,13],[2,6,8,10],[3,5,6,7]]
print("Matriz ingresada")
for i in e:
    print(i)
res=det_vect_son_li(e)
print("Matriz procesada")
for i in e:
    print(i)
if(res):
    print("Los vectores son li")
else:
    print("Los vectores son ld")