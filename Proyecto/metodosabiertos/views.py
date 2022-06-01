from asyncio.format_helpers import _format_callback_source
from re import template
from tkinter.tix import Tree
from django.shortcuts import render, HttpResponse
from django.views import View
from toml import TomlEncoder

from metodosabiertos.forms import Formulario_punto_fijo
from metodosabiertos.forms import Formulario_newton
from metodosabiertos.forms import Formulario_raices
from metodosabiertos.forms import Formulario_secante

from metodosabiertos.puntofijo import fixed_point
from metodosabiertos.newton import m_newton
from metodosabiertos.raices import root_m
from metodosabiertos.secante import secant
# Create your views here.
class punto_fijo(View):
    template_name = 'punto_fijo/punto_fijo.html'
    template_response = 'punto_fijo/punto_fijo_response.html'
    form_class = Formulario_punto_fijo()

    def get(self, request, *args, **kwargs):
        form = self.form_class
        return render(request, self.template_name,{'form':form})

    def post(self, request, *args, **kwargs):
        form = Formulario_punto_fijo(request.POST)
        if form.is_valid():                                                 #Si el formulario es valido
            funcion = form.cleaned_data['funcion']                          #Savamos la funcion y todas las partes
            funciong = form.cleaned_data['funciong']
            xi = float(form.cleaned_data['xi'])
            tolerancia = float(form.cleaned_data['tolerancia'])
            opcion = form.cleaned_data['opcion']
            iteraciones = int(form.cleaned_data['iteraciones'])
            resultado =""
            try:                                                                                    #Se trata de ejecutar el formulario
                if opcion == "1":                                                                   #En caso de ser opcion  de errrpr absoluto
                    resultado = fixed_point(funcion,xi,tolerancia,True,funciong, iteraciones)
                else:                                                                               #En caso de ser opcion de error relativo
                    resultado = fixed_point(funcion,xi,tolerancia,False,funciong, iteraciones)
                return render(request,self.template_response, {'tabla':resultado[1], 'resultado':resultado[0]} )              #Se envia la prespuesta
            except:
                print("Error en el metodo")
            print(resultado)
        return render(request, self.template_name, {'form':Formulario_punto_fijo})

class newton(View):
    template_name = 'newton/newton.html'
    template_response = 'newton/newton_response.html'
    form_class = Formulario_newton()

    def get(self,request,*args,**kwargs):
        form = self.form_class
        return render(request, self.template_name,{'form':form})  

    def post(self, request, *args, **kwargs):
        form = Formulario_newton(request.POST)
        if form.is_valid():
            
            funcion = form.cleaned_data['funcion']
            funciong = form.cleaned_data['funciong']
            xi = float(form.cleaned_data['xi'])
            tolerancia = float(form.cleaned_data['tolerancia']) 
            opcion = form.cleaned_data['opcion']
            iteraciones = int(form.cleaned_data['iteraciones'])
            resultado = ""
            print(funcion,funciong,xi, tolerancia, opcion, iteraciones)
            try:   
                if opcion == "1":
                    resultado = m_newton(funcion,xi,tolerancia,True,funciong,iteraciones)
                else:
                    resultado = m_newton(funcion,xi,tolerancia,False,funciong,iteraciones)
                return render(request,self.template_response, {'tabla': resultado[1], 'resultado':resultado[0]})
            except:
                print("Error en el metodo")
            print(resultado)
        return render(request, self.template_name, {'form':Formulario_newton})

class raices(View):
    template_name = 'raices/raices.html'
    template_response = 'raices/raices_response.html'
    form_class = Formulario_raices()

    def get(self,request,*args,**kwargs):
        form = self.form_class
        return render(request, self.template_name,{'form':form})
    
    def post(self, request, *args, **kwargs):
        form = Formulario_raices(request.POST)
        if form.is_valid():
            funcion = form.cleaned_data['funcion']
            fx1 = form.cleaned_data['funcionfx1']
            fx2 = form.cleaned_data['funcionfx2']
            xi = float(form.cleaned_data['xi'])
            tolerancia = float(form.cleaned_data['tolerancia'])
            opcion = form.cleaned_data['opcion']
            iteraciones = int(form.cleaned_data['iteraciones'])
            resultado = ""
            print(funcion, fx1, fx2, xi, tolerancia, opcion,iteraciones)
            try:
                if opcion == "1":
                    resultado = root_m(funcion,xi,fx1,fx2,tolerancia,True,iteraciones)
                else:
                    resultado = root_m(funcion,xi,fx1,fx2,tolerancia,False,iteraciones)
                return render(request,self.template_response, {'tabla':resultado[1], 'resultado':resultado[0]})
            except:
                print("Error en el metodo")
            print(resultado)
        return render(request, self.template_name, {'form':Formulario_raices})

class secante(View):
    template_name = 'secante/secante.html'
    template_response = 'secante/secante_response.html'
    form_class = Formulario_secante()

    def get(self,request,*args,**kwargs):
        form = self.form_class
        return render(request, self.template_name,{'form':form})
    
    def post(self, request, *args, **kwargs):
        form = Formulario_secante(request.POST)
        if form.is_valid():
            funcion = form.cleaned_data['funcion']
            x1 = float(form.cleaned_data['x1'])
            x2 = float(form.cleaned_data['x2'])
            tolerancia = float(form.cleaned_data['tolerancia'])
            opcion = form.cleaned_data['opcion']
            iteraciones = int(form.cleaned_data['iteraciones'])
            resultado = ""
            print(funcion, x1 ,x2, tolerancia, opcion, iteraciones)
            try:
                if opcion == "1":
                    resultado = secant(funcion,x1,x2,tolerancia,True,iteraciones)
                else:
                    resultado = secant(funcion,x1,x2,tolerancia,False,iteraciones)
                return render(request,self.template_response,{'tabla': resultado[1], 'resultado':resultado[0]})
            except:
                print("Error en el metodo")
            print(resultado)
        return render(request, self.template_name, {'form':self.form_class})
