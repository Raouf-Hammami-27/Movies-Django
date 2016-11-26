"""exam URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url, include
from django.contrib.auth import views
from films import views as hv, models
from django.conf import settings
from django.conf.urls.static import static

from rest_framework import serializers,viewsets,routers

from films.models import Film, Author, Genre
import debug_toolbar



class FilmSerializer(serializers.ModelSerializer):

    genre = serializers.StringRelatedField(many=True)


    class Meta:
        model = Film
        fields = ['nom','genre','date_sortie','disponible']


class FilmViewSet(viewsets.ModelViewSet):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer


router = routers.DefaultRouter()
router.register(r'films',FilmViewSet)


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('registration.backends.hmac.urls')),
    url(r'^login/$', views.login, {'template_name': 'registration/login.html'}, name="login"),
    url(r'^logout/$', views.logout, {'template_name': 'registration/logged_out.html'}, name="logout"),


    url(r'^$', hv.FilmList.as_view(), name="Films-list"),
    url(r'^film/(?P<pk>\d+)$', hv.FilmDetail.as_view(), name="Film-detail"),
    #url(r'^films/genres/(?P<genre_id>\d+)$', hv.FilmList.as_view(), name="Film-genre"),
    url(r'^film/create$', hv.FilmCreate.as_view(), name="Film-create"),
    url(r'^film/update/(?P<pk>\d+)$', hv.FilmUpdate.as_view(), name="Film-update"),
    url(r'^film/delete/(?P<pk>\d+)$', hv.FilmDelete.as_view(), name="Film-delete"),

    url(r'^favori/create/(?P<pk>\d+)$', hv.FavoriCreate.as_view(), name="Favori-create"),
    url(r'^favoris$', hv.FavoriList.as_view(), name="favoris"),

    url(r'^genres$', hv.GenreList.as_view(), name="genres"),
    url(r'^api/', include((router.urls))),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^__debug__/', include(debug_toolbar.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
