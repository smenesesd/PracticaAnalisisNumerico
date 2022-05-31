from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponse
from django.views import View
from metodoscerrados.forms import Formulario_biseccion
from metodoscerrados.forms import Formulario_regla_falsa
from metodoscerrados.forms import Formulario_incremental

from metodoscerrados.biseccion import biseccion
from metodoscerrados.regla_falsa import false_position_method
from metodoscerrados.incremental import incremental
# Create your views here.
class metodo_biseccion(View):
    template_name = 'biseccion/biseccion.html'
    template_response = 'biseccion/biseccion_response.html'
    form_class = Formulario_biseccion()

    def get(self, request, *args, **kwargs):
        form = self.form_class
        return render(request, self.template_name,{'form':form})

    def post(self, request, *args, **kwargs):
        form = Formulario_biseccion(request.POST)
        if form.is_valid():
            funcion = form.cleaned_data['funcion']
            xi = float(form.cleaned_data['xi'])
            xf = float(form.cleaned_data['xf'])
            tolerancia = float(form.cleaned_data['tolerancia'])
            opcion = form.cleaned_data['opcion']
            resultado =""
            try:
                if opcion == "1":
                    resultado = biseccion(funcion,xi,xf,tolerancia,True)
                else:
                    resultado = biseccion(funcion,xi,xf,tolerancia,True)
                return render(request,self.template_response, {'tabla':resultado[1], 'resultado':resultado[0]})
            except:
                print("Error en el metodo")
            print(resultado)
        return render(request, self.template_name, {'form':Formulario_biseccion})

    

class metodo_regla_faslsa(View):
    template_name = 'regla_falsa/reglafalsa.html'
    template_response = 'regla_falsa/reglafalsa_response'
    form_class = Formulario_regla_falsa()
    
    def get(self, request, *args, **kwargs):
        form = self.form_class
        return render(request, self.template_name,{'form':form})

    def post(self, request, *args, **kwargs):
        form = Formulario_regla_falsa(request.POST)
        if form.is_valid():
            funcion = form.cleaned_data['funcion']
            xi = float(form.cleaned_data['xi'])
            xf = float(form.cleaned_data['xf'])
            tolerancia = float(form.cleaned_data['tolerancia'])
            opcion = form.cleaned_data['opcion']
            resultado = ""
            try: 
                if opcion == "1":
                    resultado = false_position_method(funcion,xi,xf,tolerancia,True)
                else:
                    resultado = false_position_method(funcion,xi,xf,tolerancia,False)
                return render(request,self.template_response, {'tabla': resultado[1], 'resultado':resultado[0]})
            except:
                print("Error en el metodo")
            print(resultado)
        return render(request, self.template_name, {'form':Formulario_regla_falsa})

class metodo_incremental(View):
    template_name = 'incremental/incremental.html'
    template_response = 'incremental/incremental_response.html'
    form_class = Formulario_incremental()
    
    def get(self, request, *args, **kwargs):
        form = self.form_class
        return render(request, self.template_name,{'form':form})

    def post(self, request, *args, **kwargs):
        form = Formulario_incremental(request.POST)
        if form.is_valid():
            funcion = form.cleaned_data['funcion']
            xi = float(form.cleaned_data['xi'])
            maxite = int(form.cleaned_data['maxite'])
            difx = float(form.cleaned_data['difx'])
            resultado = ""
            try:
                resultado = incremental(funcion,xi,maxite,difx)
                return render(request,self.template_response, {'tabla': resultado[1], 'resultado':resultado[0]})
            except:
                print("Error en el metodo")
            print(resultado)
        return render(request, self.template_name, {'form':Formulario_incremental})

    