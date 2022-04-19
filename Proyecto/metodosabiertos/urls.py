from django.urls import path
from metodosabiertos.views import home
urlpatterns = [
    path(
        route='registro/', 
        view = home,
        name='registro_premio'
    )
]