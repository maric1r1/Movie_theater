from django.urls import path

from . import views

urlpatterns = [
    path("", views.Main_screen.as_view(), name="main"),
    path("meumalvadofavorito/", views.Meumalvadofavorito.as_view(), name="Meu malvado favorito"),
    path("kungfupanda/", views.Kungfupandas.as_view(), name="Kung fu panda"),
    path("garfield/", views.Garfield.as_view(), name="Garfield"),
    path("kungfupanda/", views.Sonic.as_view(), name="Sonic"),
    path("planetamacaco/", views.Planetamacaco.as_view(), name="Planeta macaco"),

]