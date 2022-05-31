from asyncio.format_helpers import _format_callback_source
from tkinter.tix import Tree
from django.shortcuts import render, HttpResponse
from django.views import View
#from Proyecto.metodosabiertos.forms import Formulario_newton
from metodosabiertos.forms import Formulario_punto_fijo
from metodosabiertos.forms import Formulario_newton
from metodosabiertos.forms import Formulario_raices
from metodosabiertos.forms import Formulario_secante

from metodosabiertos.puntofijo import fixed_point
# Create your views here.
class punto_fijo(View):
    template_name = 'punto_fijo/punto_fijo.html'
    form_class = Formulario_punto_fijo()

    def get(self, request, *args, **kwargs):
        form = self.form_class
        return render(request, self.template_name,{'form':form})

    def post(self, request, *args, **kwargs):
        form = Formulario_punto_fijo(request.POST)
        if form.is_valid():
            print("entre perra")
            funcion = form.cleaned_data['funcion']
            funciong = form.cleaned_data['funciong']
            xi = float(form.cleaned_data['xi'])
            tolerancia = int(form.cleaned_data['tolerancia'])
            opcion = form.cleaned_data['opcion']
            iteraciones = int(form.cleaned_data['iteraciones'])
            resultado =""
            try:
                if opcion == "1":
                    resultado = fixed_point(funcion,xi,tolerancia,True,funciong, iteraciones)
                else:
                    resultado = fixed_point(funcion,xi,tolerancia,False,funciong, iteraciones)
            except:
                print("Error en el metodo")
            print(resultado)
        return render(request, self.template_name, {'form':Formulario_punto_fijo})

class newton(View):
    template_name = 'newton/newton.html'
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
            tolerancia = int(form.cleaned_data['tolerancia'])
            opcion = form.cleaned_data['opcion']
            iteraciones = form.cleaned_data['iteraciones']
            resultado = ""
            try:   
                if opcion == "1":
                    resultado = fixed_point(funcion,xi,tolerancia,True,funciong,iteraciones)
                else:
                    resultado = fixed_point(funcion,xi,tolerancia,False,funciong,iteraciones)
            except:
                print("Error en el metodo")
            print(resultado)
        return render(request, self.template_name, {'form':Formulario_newton})

class raices(View):
    template_name = 'raices/raices.html'
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
            tolerancia = int(form.cleaned_data['tolerancia'])
            opcion = form.cleaned_data['opcion']
            iteraciones = form.cleaned_data['iteraciones']
            resultado = ""
            try:
                if opcion == "1":
                    resultado = fixed_point(funcion,fx1,fx2,xi,tolerancia,True,iteraciones)
                else:
                    resultado = fixed_point(funcion,fx1,fx2,xi,tolerancia,False,iteraciones)
            except:
                print("Error en el metodo")
            print(resultado)
        return render(request, self.template_name, {'form':Formulario_raices})
class secante(View):
    template_name = 'secante/secante.html'
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
            tolerancia = int(form.cleaned_data['tolerancia'])
            opcion = form.cleaned_data['opcion']
            iteraciones = form.cleaned_data['iteraciones']
            resultado = ""
            try:
                if opcion == "1":
                    resultado = fixed_point(funcion,x1,x2,tolerancia,True,iteraciones)
                else:
                    resultado = fixed_point(funcion,x1,x2,tolerancia,False,iteraciones)
            except:
                print("Error en el metodo")
            print(resultado)
        return render(request, self.template_name, {'form':Formulario_secante})
