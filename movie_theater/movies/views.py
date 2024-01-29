from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Scheduling
import templates


class Main_screen(generic.DetailView):
    model = Scheduling
    template_name = "templates/first.html"
    pk_url_kwarg = 'rest_id'
    

    def get_queryset(self):
        return 0


class Kungfupandas(generic.DetailView):
    model = Scheduling
    template_name = "templates/kungfupandas.html"

    def get_queryset(self):
        return 0
    

class Garfield(generic.DetailView):
    model = Scheduling
    template_name = "templates/Garfield.html"

    def get_queryset(self):
        return 0


class Planetamacaco(generic.DetailView):
    model = Scheduling
    template_name = "templates/planetamacaco.html"

    def get_queryset(self):
        return 0


class Sonic(generic.DetailView):
    model = Scheduling
    template_name = "templates/sonic.html"

    def get_queryset(self):
        return 0
        # return Scheduling.objects.filter(duration=timezone.now())

class Meumalvadofavorito(generic.DetailView):
    model = Scheduling
    template_name = "templates/meumalvadofavorito.html"

    def get_queryset(self):
        return 0
        # return Scheduling.objects.filter(duration=timezone.now())