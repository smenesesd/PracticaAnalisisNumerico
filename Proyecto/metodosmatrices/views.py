from django.shortcuts import render, HttpResponse
from django.views import View


# Create your views here.
#[[2,34,4] [-2, 34,4]]
def validador_matriz_b(b,n):
    b = b.replace("[",'')
    b = b.replace("]",'')
    b = b.replace(" ",'')
    final = b.split(",")
    fila =[]
    try:
        for j in final:
            if "-" in j:
                j = j.replace("-",'')
                negativo = float(1-2)
                numero = float(j)*negativo
                fila.append(numero)
            else:
                numero = float(j)
                fila.append(numero)
    except:
        return "Ocurrio un error", False
    if len(fila) != n:
        return "Dimensiones erroreas", True
    return fila, True
    
def validador_matriz(a, n):
    division = a.split("] [")
    matriz = []
    for i in division:
        i = i.replace("[",'')
        i = i.replace("]",'')
        i = i.replace(" ",'')
        final = i.split(",")
        fila =[]
        try:
            for j in final:
                print(j)
                if "-" in j:
                    j = j.replace("-",'')
                    negativo = float(1-2)
                    numero = float(j)*negativo
                    fila.append(numero)
                else:
                    numero = float(j)
                    fila.append(numero)
        except:
            return "Ocurrio un error", False
        matriz.append(fila)
    for j in range(len(matriz)):
        if len(matriz) != len(matriz[j]) or len(matriz) !=n:
            return "dimensiones erroneas", False
    return matriz, True
