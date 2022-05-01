from django import forms
from .models import PostAd

class FormPostAd(forms.ModelForm):
    class Meta:
        model = PostAd
        fields = "__all__"
        labels = {
            "city": "Ville",
            "house": "Type de bien",
            "title_ad": "Titre de l'annonce",
            "description_ad": "Descrption de l'annonce",
            "price_ad": "Prix",
            "photo_ad": "Ajouter une photo",
        }
