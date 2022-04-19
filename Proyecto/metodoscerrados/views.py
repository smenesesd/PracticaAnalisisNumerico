from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponse
from django.views import View

# Create your views here.
class metodo_incremental(View):
    template_name = 'incremental/incremental.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

class metodo_biseccion(View):
    template_name = 'biseccion/biseccion.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

class metodo_regla_faslsa(View):
    template_name = 'regla_falsa/reglafalsa.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)