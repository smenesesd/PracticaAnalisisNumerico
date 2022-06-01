import sympy as sym

def splines_l(nx, ny):
    n = len(nx)                                 #Cantidad de puntos a unir
    x = sym.Symbol('x')                         #Definimos x como un simbolo
    lista_tramos = []
    for tramo in range(1,n):                    #Recorremos los puntos
        numerador = ny[tramo]-ny[tramo-1]       #Numerado va a ser Yactual -Yanterios
        denominador = nx[tramo]-nx[tramo-1]     #Denominador va ser Xactual -Yanterior
        m = numerador/denominador               #Pendiente de la grafica
        pxtramo = ny[tramo-1]                   
        pxtramo = pxtramo + m *(x-nx[tramo])    #Tramo va a ser la ecacion del punto en Yinicial + la prendiente * x -Xactual
        lista_tramos.append(pxtramo)    
    return lista_tramos                         #Retornamos la lista de tramos         
