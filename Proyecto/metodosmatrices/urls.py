from django.urls import path
from metodoscerrados import views
urlpatterns = [
    path(route='crout/', view = views.metodo_incremental.as_view(), name='crout'),
    path(route='doolittle/', view = views.metodo_biseccion.as_view(), name='dolittle'),
    path(route='elim_gaussiana/', view = views.metodo_regla_faslsa.as_view(), name='elim_gaussiana'),
    path(route='elim_gauss_piv_parcial/', view = views.metodo_regla_faslsa.as_view(), name='elim_gauss_piv_parcial'),
    path(route='elim_gauss_piv_total/', view = views.metodo_regla_faslsa.as_view(), name='elim_gauss_piv_total'),
    path(route='factorizacion_LU/', view = views.metodo_regla_faslsa.as_view(), name='factorizacion_LU'),
    path(route='seidel/', view = views.metodo_regla_faslsa.as_view(), name='seidel'),]