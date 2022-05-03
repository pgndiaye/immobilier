from django import forms
from .models import PostAd, SearchProperty

class FormPostAd(forms.ModelForm):
    class Meta:
        model = PostAd
        exclude  = [
            "date_create_ad", 
            "date_modified_ad",
        ]
        labels = {
            "city": "Ville",
            "house": "Type de bien",
            "title_ad": "Titre de l'annonce",
            "description_ad": "Descrption de l'annonce",
            "price_ad": "Prix",
            "photo_ad": "Ajouter une photo",
            "estate_type": "Type de vente",
        }
        
        widgets = {
            "user": forms.HiddenInput,
            "user_id_ad": forms.HiddenInput,
        }
        
class FormSearchProperty(forms.ModelForm):
    class Meta:
        model = SearchProperty
        fields = "__all__"
        labels = {
            "city": "Ville",
            "district": "Quartier",
            "district": "Quartier",
            "number_of_piece": "Nombr de piéce",
        }
        