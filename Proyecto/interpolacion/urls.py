from django.urls import path
from interpolacion import views
urlpatterns = [
    path(route='vander/', view = views.metodo_vander.as_view(), name='vander'),
    path(route='internewton/', view = views.metodo_internewton.as_view(), name='internewton'),
    path(route='spline/', view = views.metodo_spline.as_view(), name='spline'),
    ]