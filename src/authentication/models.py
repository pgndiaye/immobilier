from pyexpat import model
from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime

class User(AbstractUser):
    photo_profile = models.ImageField()   

class City(models.Model):
    choices_city = [
        ("Abidjan", "Abidjan"),
        ("Bouaké", "Bouaké"),
        ("San-Pédro", "San-Pédro"),
        ("Korhogo", "Korhogo"),
        ("Abengouro", "Abengouro"),
        ("Man", "Man"),
        ("Abengouro", "Abengouro"),
        ("Daloa", "Daloa"),
        ("Agboville", "Agboville"),
        ("Bingerville", "Bingerville"),
    ] 
    city = models.CharField(max_length=20, choices=choices_city)    

class House(models.Model):
    choices_house = [
        ("Maison", "Maison"),
        ("Château", "Château"),
        ("Hôtel particulier", "Hôtel particulier"),
        ("Manoir", "Manoir"),
        ("Villa", "Villa"),
        ("Appartement", "Appartement"),
        ("Chambre", "Chambre"),
        ("Duplex", "Duplex"),
        ("Place de parking", "Place de parking"),
        ("Terrain", "Terrain"),
        ("Autre", "Autre"),
    ]
    house = models.CharField(max_length=20)
    
class PostAd(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    house = models.ForeignKey(House, on_delete=models.CASCADE)
    
    title_ad = models.CharField(max_length=30)
    description_ad = models.CharField(max_length=1000)
    price_ad = models.IntegerField()
    phto_add = models.ImageField()
    
    date_post = models.DateTimeField(auto_now=True, )
    
    
	
	
	
	
	
	
	
	
	
	
	
	
	
	