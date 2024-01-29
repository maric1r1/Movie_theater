import datetime
from django.db import models
from django.utils import timezone

class Scheduling(models.Model):
    global MOVIES, SALA

    PANDA = "Kung Fu Panda 4"
    GARFIELD = "Garfield - Fora da Casa"
    PLANETAMACACO = "Planeta dos Macacos: O Reinado "
    SONIC3 = "Sonic 3"
    MEUMALVADOFAVORITO = "Meu Malvado  Favorito 4"
    MOVIES = (
        ((PANDA),'Kung Fu Pandas 4'),
        ((GARFIELD),'Garfield - Fora da Casa'),
        ((PLANETAMACACO),'Planeta dos Macacos: O Reinado '),
        ((SONIC3), 'Sonic 3'),
        ((MEUMALVADOFAVORITO),'Meu Malvado Favorito 4'),
    )

    SALA = [
        (u'01',u'SALA 1'),
        (u'02',u'SALA 2'),
        (u'03',u'SALA 3'),
    ]
    # movie = models.TextField(max_length=200,choices=MOVIES, default = MOVIES.index)
    movie = models.TextField(max_length=200)
    author = models.TextField(max_length=300, default='SOME STRING')
    duration = models.TextField(max_length=200 ,default='1hours')
    # sala = models.TextField(max_length=200,choices=SALA, default = MOVIES.index)
    sala = models.TextField(max_length=2,default='1hours')
    saladescricao = models.TextField(max_length=200,default='hd')
    hours = models.DateTimeField('date published')
    name_client = models.TextField(max_length=200,default='None')
    cpf_client = models.TextField(max_length=200,default='None')
    method_payment = models.TextField(max_length=200,default='dinner')

    def get_weekday_from_display(self):
        return MOVIES[self.movie]

    def get_weekday_to_display(self):
        return SALA[self.sala]

    def __str__(self):
        return self.name_client

    def return_movie(self):
        return [self.movie, self.sala, self.name_client,self.cpf_client, self.method_payment]
