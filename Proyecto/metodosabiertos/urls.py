from django.urls import path
from metodosabiertos import views
urlpatterns = [
    path(
        route='punto_fijo/', 
        view = views.punto_fijo.as_view(),
        name='punto_fijo'
    ),
    path(
        route='newton/', 
        view = views.newton.as_view(),
        name='newton'
    ),
    path(
        route='raices/', 
        view = views.raices.as_view(),
        name='raices'
    ),
    path(
        route='secante/', 
        view = views.secante.as_view(),
        name='secante'
    )
]