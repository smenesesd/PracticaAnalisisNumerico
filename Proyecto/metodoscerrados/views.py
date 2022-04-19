from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponse
from django.views import View

# Create your views here.
class metodo_incremental(View):
    template_name = 'incremental/incremental.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

def biseccion(request):
    return HttpResponse("hola perra")

def reglafalse(request):
    return HttpResponse("hola perra")