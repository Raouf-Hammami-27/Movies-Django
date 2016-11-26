from django.contrib.auth.models import User
from django.db import models
from django.conf import settings

# Create your models here.
class Author(models.Model):
    date= models.DateField(auto_now=1)
    user = models.OneToOneField(settings.AUTH_USER_MODEL)

    def __str__(self):
        return '%s' % (self.user.username)


class Genre(models.Model):
    nom = models.CharField(max_length=255)

    def __str__(self):
        return self.nom


class Film(models.Model):
    nom = models.CharField(max_length=255)
    auteur = models.ForeignKey(Author)
    date_sortie  = models.DateField()
    disponible= models.BooleanField(default= True)
    genre = models.ManyToManyField(Genre)
    image= models.ImageField(upload_to='photos')
    auteurs = models.ManyToManyField(User,through='Favori')

    def __str__(self):
        return self.nom

class Favori(models.Model):
    auteur = models.ForeignKey(User,on_delete=models.CASCADE)
    film = models.ForeignKey(Film,on_delete=models.CASCADE)
    date_ajout = models.DateTimeField(auto_now_add=True)
    comment = models.TextField(max_length=512)


    def __str__(self):
        return '%s %s %s' % (self.auteur, self.film , self.date_ajout.date())
