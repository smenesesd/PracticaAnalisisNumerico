from asyncio.format_helpers import _format_callback_source
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
            tolerancia = int(form.cleaned_data['tolerancia'])
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
