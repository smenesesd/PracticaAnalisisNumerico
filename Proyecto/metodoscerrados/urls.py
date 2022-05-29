from django.urls import path
from metodoscerrados import views
urlpatterns = [
    path(route='incremental/', view = views.metodo_incremental.as_view(), name='incremental'),
    path(route='biseccion/', view = views.metodo_biseccion.as_view(), name='biseccion'),
    path(route='regla/', view = views.metodo_regla_faslsa.as_view(), name='regla_falsa'),
]