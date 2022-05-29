from django.shortcuts import render, HttpResponse
from django.views import View
from metodosabiertos.forms import Formulario_punto_fijo
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

    def get(self,request,*args,**kwargs):
        return render(request, self.template_name)   

class raices(View):
    template_name = 'raices/raices.html'

    def get(self,request,*args,**kwargs):
        return render(request, self.template_name)
class secante(View):
    template_name = 'secante/secante.html'

    def get(self,request,*args,**kwargs):
        return render(request, self.template_name)
