from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponse
from django.views import View
from metodoscerrados.forms import Formulario_biseccion
from metodoscerrados.forms import Formulario_regla_falsa
from metodoscerrados.forms import Formulario_incremental

# Create your views here.
class metodo_incremental(View):
    template_name = 'incremental/incremental.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

class metodo_biseccion(View):
    template_name = 'biseccion/biseccion.html'
    form_class = Formulario_biseccion()

    def get(self, request, *args, **kwargs):
        form = self.form_class
        return render(request, self.template_name,{'form':form})

    def post(self, request, *args, **kwargs):
        form = Formulario_biseccion(request.POST)
        if form.is_valid():
            print(form.cleaned_data['funcion'])
            print(form.cleaned_data['xi'])
            print(form.cleaned_data['xf'])
            print(form.cleaned_data['tolerancia'])
            print(form.cleaned_data['opcion'])
        return render(request, self.template_name, {'form':Formulario_biseccion})

    

class metodo_regla_faslsa(View):
    template_name = 'regla_falsa/reglafalsa.html'
    form_class = Formulario_regla_falsa()
    
    def get(self, request, *args, **kwargs):
        form = self.form_class
        return render(request, self.template_name,{'form':form})

    def post(self, request, *args, **kwargs):
        form = Formulario_regla_falsa(request.POST)
        if form.is_valid():
            print(form.cleaned_data['funcion'])
            print(form.cleaned_data['xi'])
            print(form.cleaned_data['xf'])
            print(form.cleaned_data['tolerancia'])
            print(form.cleaned_data['opcion'])
        return render(request, self.template_name, {'form':Formulario_regla_falsa})

class metodo_incremental(View):
    template_name = 'incremental/incremental.html'
    form_class = Formulario_incremental()
    
    def get(self, request, *args, **kwargs):
        form = self.form_class
        return render(request, self.template_name,{'form':form})

    def post(self, request, *args, **kwargs):
        form = Formulario_incremental(request.POST)
        if form.is_valid():
            print(form.cleaned_data['funcion'])
            print(form.cleaned_data['xi'])
            print(form.cleaned_data['maxite'])
            print(form.cleaned_data['difx'])
        return render(request, self.template_name, {'form':Formulario_incremental})

    