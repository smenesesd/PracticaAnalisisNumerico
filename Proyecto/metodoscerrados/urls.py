from django.urls import path
from metodoscerrados.views import home1
urlpatterns = [
    path(
        route='registro/', 
        view = home1,
        name='registro_premio'
    )
]