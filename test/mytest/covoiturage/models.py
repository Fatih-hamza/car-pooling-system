from django.db import models

# Create your models here.

class Proposition(models.Model):
    conducteur_id = models.IntegerField()
    depart = models.CharField(max_length=100)
    arrivee = models.CharField(max_length=100)
    date = models.DateField()
    places_libres = models.IntegerField()
    cotisation = models.IntegerField()
    description = models.CharField(max_length=500, null=True, blank=True)


class Commentaire(models.Model):
    rating = models.IntegerField()
    description = models.TextField(max_length=555)
    conducteur_id = models.IntegerField()
    passanger_id = models.IntegerField()


class Voiture(models.Model):
    marque = models.CharField(max_length=100)
    modele = models.CharField(max_length=100)
    voiture_pic = models.ImageField(null=True, blank=True, default="https://cdn.dribbble.com/users/365712/screenshots/2389289/media/533f0ec17432bb3cd02b46b308c2aa50.png?compress=1&resize=400x300&vertical=top")
    conducteur_id = models.IntegerField()









    