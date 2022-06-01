from django.urls import path
from metodoscerrados import views
urlpatterns = [
    path(route='crout/', view = views.metodo_crout.as_view(), name='crout'),
    path(route='doolittle/', view = views.metodo_doolittle.as_view(), name='dolittle'),
    path(route='elim_gaussiana/', view = views.metodo_elim_gaussiana.as_view(), name='elim_gaussiana'),
    path(route='elim_gauss_piv_parcial/', view = views.metodo_elim_gauss_piv_parcial.as_view(), name='elim_gauss_piv_parcial'),
    path(route='elim_gauss_piv_total/', view = views.metodo_elim_gauss_piv_total.as_view(), name='elim_gauss_piv_total'),
    path(route='factorizacion_LU/', view = views.metodo_factorizacion_LU.as_view(), name='factorizacion_LU'),
    path(route='seidel/', view = views.metodo_seidel.as_view(), name='seidel'),]