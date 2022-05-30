from asyncio.format_helpers import _format_callback_source
from django.shortcuts import render, HttpResponse
from django.views import View
#from Proyecto.metodosabiertos.forms import Formulario_newton
from metodosabiertos.forms import Formulario_punto_fijo
from metodosabiertos.forms import Formulario_newton
from metodosabiertos.forms import Formulario_raices
from metodosabiertos.forms import Formulario_secante
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
            print(form.cleaned_data['funcion'])
            print(form.cleaned_data['funciong'])
            print(form.cleaned_data['xi'])
            print(form.cleaned_data['tolerancia'])
            print(form.cleaned_data['opcion'])
            print(form.cleaned_data['iteraciones'])
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
            print(form.cleaned_data['funcion'])
            print(form.cleaned_data['funciong'])
            print(form.cleaned_data['xi'])
            print(form.cleaned_data['tolerancia'])
            print(form.cleaned_data['opcion'])
            print(form.cleaned_data['iteraciones'])
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
            print(form.cleaned_data['funcion'])
            print(form.cleaned_data['funcionfx1'])
            print(form.cleaned_data['funcionfx2'])
            print(form.cleaned_data['xi'])
            print(form.cleaned_data['tolerancia'])
            print(form.cleaned_data['opcion'])
            print(form.cleaned_data['iteraciones'])
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
            print(form.cleaned_data['funcion'])
            print(form.cleaned_data['x1'])
            print(form.cleaned_data['x2'])
            print(form.cleaned_data['tolerancia'])
            print(form.cleaned_data['opcion'])
            print(form.cleaned_data['iteraciones'])
        return render(request, self.template_name, {'form':Formulario_secante})
