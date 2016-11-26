from django.contrib.auth import get_user
from django.shortcuts import render

from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.views.generic.list import ListView

from films.forms import FavoriForm
from films.models import Film, Genre, Favori
from rest_framework import serializers,viewsets,routers



# Create your views here.
class GenreList(ListView):
    model = Genre
    context_object_name = 'genres'


class FilmCutomerList(ListView):
    model = Film
    context_object_name = 'Films'


class FilmList(ListView):
    model = Film
    context_object_name = 'Films'

    def get_queryset(self):

        genre_id = self.kwargs.get('genre_id', None)
        if genre_id:
            return Film.objects.filter(tags=genre_id)

        #return Film.objects.filter(disponible=1).order_by('title')
        return Film.objects.order_by('-date_sortie')

    def get_context_data(self, **kwargs):
        context = super(FilmList, self).get_context_data(**kwargs)
        context['genre'] = Genre.objects.all()
        return context


class FilmCreate(CreateView):
    model = Film
    fields = '__all__'
    success_url = '/'



class FilmUpdate(UpdateView):
    model = Film
    fields = '__all__'
    success_url = '/'


class FilmDetail(DetailView):
    model = Film
    fields = '__all__'


class FilmDelete(DeleteView):
    model = Film
    fields = '__all__'
    success_url = '/'

class FavoriCreate(FormView):
    template_name = 'films/Favori_form.html'
    form_class = FavoriForm
    success_url = '/'

    def form_valid(self, form):
        film_id = self.kwargs.get('pk', None)
        form.instance.film=Film.objects.get(id=film_id)
        form.instance.auteur=get_user(self.request)
        return super(FavoriCreate,self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(FavoriCreate, self).get_context_data(**kwargs)
        film_id = self.kwargs.get('pk', None)
        film = Film.objects.get(id=film_id)
        context['film'] = film.nom
        return context

class FavoriList(ListView):
    model = Favori
    context_object_name = 'Favoris'