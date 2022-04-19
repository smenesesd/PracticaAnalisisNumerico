from django.urls import path
from metodoscerrados import views
urlpatterns = [
    path(
        route='incremental/', 
        view = views.metodo_incremental.as_view(),
        name='metodo incremental'
    )
]