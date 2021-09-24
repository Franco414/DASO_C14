"""
Ejercicio 5.12. Escribir una función que dada la cantidad de ejercicios de un examen, y el porcentaje
necesario de ejercicios bien resueltos necesario para aprobar dicho examen, revise un grupo de exame-
nes. Para ello, en cada paso debe preguntar la cantidad de ejercicios resueltos por el alumno, indicando
con un valor centinela que no hay más examenes a revisar. Debe mostrar por pantalla el porcentaje co-
rrespondiente a la cantidad de ejercicios resueltos respecto a la cantidad de ejercicios del examen y una
leyenda que indique si aprobó o no.
"""
def return_result_examen(n_exercises,min2pass):
    continuar=True
    while(continuar):
        x=int(input("Ingrese la cantidad de ejercicio resueltos por el alumno"))
        if(x==-1):
            continuar=False
        else:
            porcentaje=x/n_exercises*100
            print("El porcentaje de ejericios resueltos es de %d"%porcentaje)
            if(x>min2pass):
                print("El alumno aprobo el examen")
            else:
                print("El alumno no aprobo el examen")
    print("Fin del programa")

return_result_examen(6,4)