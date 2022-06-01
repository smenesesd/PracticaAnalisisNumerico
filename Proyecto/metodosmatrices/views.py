from django.shortcuts import render, HttpResponse
from django.views import View
from django.contrib import messages
from metodosmatrices.forms import Formulario_doolittle
from metodosmatrices.forms import Formulario_crout
from metodosmatrices.Metodos.crout import crout
from metodosmatrices.Metodos.doolittle import doolittle
import numpy as np


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


class metodo_crout(View):
    template_name = 'crout/crout.html'
    template_response = 'crout/crout_response.html'
    form_class = Formulario_crout

    def get(self, request, *args, **kwargs):
        form = self.form_class
        return render(request, self.template_name,{'form':form})

    def post(self, request, *args, **kwargs):
        form = Formulario_crout(request.POST)
        if form.is_valid():
            dimension= int(form.cleaned_data['tam'])
            matrizB = form.cleaned_data['matrizB']
            matrizA = form.cleaned_data['matrizA']
            resultadoA = validador_matriz(matrizA, dimension)
            resultadoB = validador_matriz_b(matrizB, dimension)
            if not resultadoA[1]:
                messages.error(request, resultadoA[0])
                return render(request, self.template_name, {'form':Formulario_crout})
            if not resultadoB[1]:
                messages.error(request, resultadoB[0])
                return render(request, self.template_name, {'form':Formulario_crout})
            resultado =""
            try:
                resultado = crout(resultadoA[0],resultadoB[0])
                resultado1 = resultado.tolist()
                print(resultado1)
                lista =[]
                j = 1
                for i in resultado1:
                    lis = []
                    pal = str(i)
                    pal1= "X"+str(j)
                    lis.append(pal1)
                    lis.append(pal)
                    lista.append(lis)
                    j +=1
                return render(request,'crout/crout_response.html',{'tabla':lista})
            except Exception as e:
                messages.error(request, "Error en el metodo")
                print(e)
        return render(request, self.template_name, {'form':Formulario_crout})

class metodo_doolittle(View):
    template_name = 'doolittle/doolittle.html'
    template_response = 'doolittle/doolittle_response.html'
    form_class = Formulario_doolittle

    def get(self, request, *args, **kwargs):
        form = self.form_class
        return render(request, self.template_name,{'form':form})

    def post(self, request, *args, **kwargs):
        form = Formulario_doolittle(request.POST)
        if form.is_valid():
            dimension= int(form.cleaned_data['tam'])
            matrizB = form.cleaned_data['matrizB']
            matrizA = form.cleaned_data['matrizA']
            resultadoA = validador_matriz(matrizA, dimension)
            resultadoB = validador_matriz_b(matrizB, dimension)
            if not resultadoA[1]:
                messages.error(request, resultadoA[0])
                return render(request, self.template_name, {'form':Formulario_doolittle})
            if not resultadoB[1]:
                messages.error(request, resultadoB[0])
                return render(request, self.template_name, {'form':Formulario_doolittle})
            resultado =""
            try:
                resultado = doolittle(resultadoA[0],resultadoB[0])
                resultado1 = resultado.tolist()
                print(resultado1)
                lista =[]
                j = 1
                for i in resultado1:
                    lis = []
                    pal = str(i)
                    pal1= "X"+str(j)
                    lis.append(pal1)
                    lis.append(pal)
                    lista.append(lis)
                    j +=1
                return render(request,'crout/crout_response.html',{'tabla':lista})
            except:
                messages.error(request, "Error en el metodo")
        return render(request, self.template_name, {'form':Formulario_doolittle})