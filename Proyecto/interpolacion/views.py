from django.shortcuts import render, HttpResponse
from django.views import View
from django.contrib import messages
from interpolacion.forms import Formulario_vander, Formulario_dif, Formulario_spline
from interpolacion.Metodos.vander import vandermonde
from interpolacion.Metodos.diferencias import dif_dividas
from interpolacion.Metodos.splines import splines_l
# Create your views here.

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

class metodo_vander(View):
    template_name = 'vander/vander.html'
    template_response = 'vander/vander_response.html'
    form_class = Formulario_vander

    def get(self, request, *args, **kwargs):
        form = self.form_class
        return render(request, self.template_name,{'form':form})

    def post(self, request, *args, **kwargs):
        form = Formulario_vander(request.POST)
        if form.is_valid():
            dimension= int(form.cleaned_data['tam'])
            matrizB = form.cleaned_data['matrizB']
            matrizA = form.cleaned_data['matrizA']
            resultadoA = validador_matriz_b(matrizA, dimension)
            resultadoB = validador_matriz_b(matrizB, dimension)
            if not resultadoA[1]:
                messages.error(request, resultadoA[0])
                return render(request, self.template_name, {'form':Formulario_vander})
            if not resultadoB[1]:
                messages.error(request, resultadoB[0])
                return render(request, self.template_name, {'form':Formulario_vander})
            resultado =""
            try:
                resultado = vandermonde(resultadoA[0],resultadoB[0])
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
                return render(request,'vander/vander_response.html',{'tabla':lista})
            except Exception as e:
                messages.error(request, "Error en el metodo")
                print(e)
        return render(request, self.template_name, {'form':Formulario_vander})

class metodo_internewton(View):
    template_name = 'diferencias/diferencias.html'
    template_response = 'diferencias/diferencias_response.html'
    form_class = Formulario_dif

    def get(self, request, *args, **kwargs):
        form = self.form_class
        return render(request, self.template_name,{'form':form})

    def post(self, request, *args, **kwargs):
        form = Formulario_dif(request.POST)
        if form.is_valid():
            dimension= int(form.cleaned_data['tam'])
            matrizB = form.cleaned_data['matrizB']
            matrizA = form.cleaned_data['matrizA']
            resultadoA = validador_matriz_b(matrizA, dimension)
            resultadoB = validador_matriz_b(matrizB, dimension)
            if not resultadoA[1]:
                messages.error(request, resultadoA[0])
                return render(request, self.template_name, {'form':Formulario_dif})
            if not resultadoB[1]:
                messages.error(request, resultadoB[0])
                return render(request, self.template_name, {'form':Formulario_dif})
            resultado =""
            try:
                resultado = dif_dividas(resultadoA[0],resultadoB[0])
                #resultado1 = resultado.tolist()
                #print(resultado1)
                
                return render(request,'diferencias/diferencias_response.html',{'tabla':resultado})
            except Exception as e:
                messages.error(request, "Error en el metodo")
                print(e)
        return render(request, self.template_name, {'form':Formulario_dif})

class metodo_spline(View):
    template_name = 'splines/splines.html'
    template_response = 'splines/splines_response.html'
    form_class = Formulario_spline

    def get(self, request, *args, **kwargs):
        form = self.form_class
        return render(request, self.template_name,{'form':form})

    def post(self, request, *args, **kwargs):
        form = Formulario_spline(request.POST)
        if form.is_valid():
            dimension= int(form.cleaned_data['tam'])
            matrizB = form.cleaned_data['matrizB']
            matrizA = form.cleaned_data['matrizA']
            resultadoA = validador_matriz_b(matrizA, dimension)
            resultadoB = validador_matriz_b(matrizB, dimension)
            if not resultadoA[1]:
                messages.error(request, resultadoA[0])
                return render(request, self.template_name, {'form':Formulario_spline})
            if not resultadoB[1]:
                messages.error(request, resultadoB[0])
                return render(request, self.template_name, {'form':Formulario_spline})
            resultado =""
            try:
                resultado = splines_l(resultadoA[0],resultadoB[0])
                print(resultado)
                return render(request,'splines/splines_response.html',{'tabla':resultado})
            except Exception as e:
                messages.error(request, "Error en el metodo")
                print(e)
        return render(request, self.template_name, {'form':Formulario_spline})