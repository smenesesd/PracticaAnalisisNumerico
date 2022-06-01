from django.urls import path
from metodosmatrices import views
urlpatterns = [
    path(route='crout/', view = views.metodo_crout.as_view(), name='crout'),
    path(route='doolittle/', view = views.metodo_doolittle.as_view(), name='dolittle'),
    ]