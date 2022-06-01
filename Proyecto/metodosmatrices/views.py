from django.shortcuts import render, HttpResponse
from django.views import View
from django.contrib import messages
from metodosmatrices.forms import Formulario_doolittle
from metodosmatrices.forms import Formulario_crout
from metodosmatrices.forms import Formulario_gauss_piv_parcial
from metodosmatrices.forms import Formulario_gauss_piv_total
from metodosmatrices.forms import Formulario_gaussiana
from metodosmatrices.forms import Formulario_factorizacion_LU, Formulario_seidel
from metodosmatrices.Metodos.crout import crout
from metodosmatrices.Metodos.doolittle import doolittle
from metodosmatrices.Metodos.elim_gauss_piv_parcial import elim_gauss_piv_parcial
from metodosmatrices.Metodos.elim_gauss_piv_total import elim_gauss_piv_total
from metodosmatrices.Metodos.elim_gaussiana import elim_gaussiana
from metodosmatrices.Metodos.factorizacion_LU import fac_LU
from metodosmatrices.Metodos.seidel import met_seidel

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

class metodo_elim_gauss_piv_parcial(View):
    template_name = 'elim_gauss_piv_parcial/elim_gauss_piv_parcial.html'
    template_response = 'elim_gauss_piv_parcial/elim_gauss_piv_parcial_response.html'
    form_class = Formulario_gauss_piv_parcial

    def get(self, request, *args, **kwargs):
        form = self.form_class
        return render(request, self.template_name,{'form':form})

    def post(self, request, *args, **kwargs):
        form = Formulario_gauss_piv_parcial(request.POST)
        if form.is_valid():
            dimension= int(form.cleaned_data['tam'])
            matrizB = form.cleaned_data['matrizB']
            matrizA = form.cleaned_data['matrizA']
            resultadoA = validador_matriz(matrizA, dimension)
            resultadoB = validador_matriz_b(matrizB, dimension)
            if not resultadoA[1]:
                messages.error(request, resultadoA[0])
                return render(request, self.template_name, {'form':Formulario_gauss_piv_parcial})
            if not resultadoB[1]:
                messages.error(request, resultadoB[0])
                return render(request, self.template_name, {'form':Formulario_gauss_piv_parcial})
            resultado =""
            try:
                resultado = elim_gauss_piv_parcial(resultadoA[0],resultadoB[0],dimension)
                #resultado1 = resultado.tolist()
                print(resultado)
                lista =[]
                j = 1
                for i in resultado:
                    lis = []
                    pal = str(i)
                    pal1= "X"+str(j)
                    lis.append(pal1)
                    lis.append(pal)
                    lista.append(lis)
                    j +=1
                return render(request,'elim_gauss_piv_parcial/elim_gauss_piv_parcial_response.html',{'tabla':lista})
            except Exception as e:
                messages.error(request, "Error en el metodo")
                print(e)
        return render(request, self.template_name, {'form':Formulario_gauss_piv_parcial})

class metodo_elim_gauss_piv_total(View):
    template_name = 'elim_gauss_piv_total/elim_gauss_piv_total.html'
    template_response = 'elim_gauss_piv_total/elim_gauss_piv_total_response.html'
    form_class = Formulario_gauss_piv_total

    def get(self, request, *args, **kwargs):
        form = self.form_class
        return render(request, self.template_name,{'form':form})

    def post(self, request, *args, **kwargs):
        form = Formulario_gauss_piv_total(request.POST)
        if form.is_valid():
            dimension= int(form.cleaned_data['tam'])
            matrizB = form.cleaned_data['matrizB']
            matrizA = form.cleaned_data['matrizA']
            resultadoA = validador_matriz(matrizA, dimension)
            resultadoB = validador_matriz_b(matrizB, dimension)
            if not resultadoA[1]:
                messages.error(request, resultadoA[0])
                return render(request, self.template_name, {'form':Formulario_gauss_piv_total})
            if not resultadoB[1]:
                messages.error(request, resultadoB[0])
                return render(request, self.template_name, {'form':Formulario_gauss_piv_total})
            resultado =""
            try:
                resultado = elim_gauss_piv_total(resultadoA[0],resultadoB[0], dimension)
                #resultado1 = resultado.tolist()
                #print(resultado1)
                lista =[]
                j = 1
                for i in resultado:
                    lis = []
                    pal = str(i)
                    pal1= "X"+str(j)
                    lis.append(pal1)
                    lis.append(pal)
                    lista.append(lis)
                    j +=1
                return render(request,'elim_gauss_piv_total/elim_gauss_piv_total_response.html',{'tabla':lista})
            except Exception as e:
                messages.error(request, "Error en el metodo")
                print(e)
        return render(request, self.template_name, {'form':Formulario_gauss_piv_total})

class metodo_elim_gaussiana(View):
    template_name = 'elim_gaussiana/elim_gaussiana.html'
    template_response = 'elim_gaussiana/elim_gaussiana_response.html'
    form_class = Formulario_gaussiana

    def get(self, request, *args, **kwargs):
        form = self.form_class
        return render(request, self.template_name,{'form':form})

    def post(self, request, *args, **kwargs):
        form = Formulario_gaussiana(request.POST)
        if form.is_valid():
            dimension= int(form.cleaned_data['tam'])
            matrizB = form.cleaned_data['matrizB']
            matrizA = form.cleaned_data['matrizA']
            resultadoA = validador_matriz(matrizA, dimension)
            resultadoB = validador_matriz_b(matrizB, dimension)
            if not resultadoA[1]:
                messages.error(request, resultadoA[0])
                return render(request, self.template_name, {'form':Formulario_gaussiana})
            if not resultadoB[1]:
                messages.error(request, resultadoB[0])
                return render(request, self.template_name, {'form':Formulario_gaussiana})
            resultado =""
            try:
                resultado = elim_gaussiana(resultadoA[0],resultadoB[0], dimension)
                #resultado1 = resultado.tolist()
                #print(resultado1)
                lista =[]
                j = 1
                for i in resultado:
                    lis = []
                    pal = str(i)
                    pal1= "X"+str(j)
                    lis.append(pal1)
                    lis.append(pal)
                    lista.append(lis)
                    j +=1
                return render(request,'elim_gaussiana/elim_gaussiana_response.html',{'tabla':lista})
            except Exception as e:
                messages.error(request, "Error en el metodo")
                print(e)
        return render(request, self.template_name, {'form':Formulario_gaussiana})

class metodo_factorizacion_LU(View):
    template_name = 'factorizacion_LU/factorizacion_LU.html'
    template_response = 'factorizacion_LU/factorizacion_LU_response.html'
    form_class = Formulario_factorizacion_LU

    def get(self, request, *args, **kwargs):
        form = self.form_class
        return render(request, self.template_name,{'form':form})

    def post(self, request, *args, **kwargs):
        form = Formulario_factorizacion_LU(request.POST)
        if form.is_valid():
            dimension= int(form.cleaned_data['tam'])
            matrizB = form.cleaned_data['matrizB']
            matrizA = form.cleaned_data['matrizA']
            resultadoA = validador_matriz(matrizA, dimension)
            resultadoB = validador_matriz_b(matrizB, dimension)
            if not resultadoA[1]:
                messages.error(request, resultadoA[0])
                return render(request, self.template_name, {'form':Formulario_factorizacion_LU})
            if not resultadoB[1]:
                messages.error(request, resultadoB[0])
                return render(request, self.template_name, {'form':Formulario_factorizacion_LU})
            resultado =""
            try:
                resultado = fac_LU(resultadoA[0],resultadoB[0], dimension)
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
                return render(request,'factorizacion_LU/factorizacion_LU_response.html',{'tabla':lista})
            except Exception as e:
                messages.error(request, "Error en el metodo")
                print(e)
        return render(request, self.template_name, {'form':Formulario_factorizacion_LU})


class metodo_seidel(View):
    template_name = 'seidel/seidel.html'
    template_response = 'seidel/seidel_response.html'
    form_class = Formulario_seidel

    def get(self, request, *args, **kwargs):
        form = self.form_class
        return render(request, self.template_name,{'form':form})

    def post(self, request, *args, **kwargs):
        form = Formulario_seidel(request.POST)
        if form.is_valid():
            dimension= int(form.cleaned_data['tam'])
            maxite= int(form.cleaned_data['maxite'])
            tolerancia= float(form.cleaned_data['tolerancia'])
            matrizB = form.cleaned_data['matrizB']
            matrizA = form.cleaned_data['matrizA']
            resultadoA = validador_matriz(matrizA, dimension)
            resultadoB = validador_matriz_b(matrizB, dimension)
            if not resultadoA[1]:
                messages.error(request, resultadoA[0])
                return render(request, self.template_name, {'form':Formulario_seidel})
            if not resultadoB[1]:
                messages.error(request, resultadoB[0])
                return render(request, self.template_name, {'form':Formulario_seidel})
            resultado =""
            try:
                resultado = met_seidel(resultadoA[0],resultadoB[0], maxite, tolerancia)
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
                return render(request,self.template_response,{'tabla':lista})
            except Exception as e:
                messages.error(request, "Error en el metodo")
                print(e)
        return render(request, self.template_name, {'form':Formulario_seidel})