from django.db import models

class PredictionModel(models.Model):
    chambres = models.IntegerField(default=0)
    salles_de_bain = models.FloatField(default=0.0)
    m2_habitable = models.IntegerField(default=0)
    m2_Lot = models.IntegerField(default=0)
    etages = models.IntegerField(default=0)
    vue_sur_leau = models.IntegerField(default=0)
    m2_cave = models.IntegerField(default=0)
    etat = models.IntegerField(default=0)
    m2_above = models.IntegerField(default=0)
    lat = models.FloatField(default=0.0)
    long = models.FloatField(default=0.0)
    prediction_house_price = models.FloatField(default=0.0)
    
# Create your models here.
