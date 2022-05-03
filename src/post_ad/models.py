from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator
from authentication.models import User

class City(models.Model):
    city = models.CharField(max_length=20)  
    
    def __str__(self):
        return self.city   

class House(models.Model):
    house = models.CharField(max_length=20)
    
    def __str__(self):
        return self.house 
    
class District(models.Model):
    district = models.CharField(max_length=20, null=False)  

    def __str__(self):
        return self.district  
    
class PostAd(models.Model):
    type_renting_or_purchasing = [
        ("Renting", "Location"),
        ("Purchasing", "Vente"),
    ]
    
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    house = models.ForeignKey(House, on_delete=models.CASCADE)
    estate_type = models.CharField(max_length=25, choices=type_renting_or_purchasing)
    
    title_ad = models.CharField(max_length=30)
    description_ad = models.TextField(max_length=1000)
    price_ad = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1_000_000_000)])
    photo_ad = models.ImageField()
    
    date_create_ad = models.DateTimeField(default=timezone.now)
    user = models.CharField(max_length=150)

    def __str__(self):
        return self.title_ad  
    