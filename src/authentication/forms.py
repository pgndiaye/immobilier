from django import forms
from .models import User

class LoginForm(forms.Form):
    username = forms.CharField(max_length=63, label="Nom d'utilisateur")
    password = forms.CharField(max_length=63, widget=forms.PasswordInput, label="Mot de passe")
        
class EditInfoForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email")
        labels = {
            "username": "Nom d'utilisateur",
            "email": "Addresse email", 
            "first_name": "Prénom", 
            "last_name": "Nom", 
        }

class EditPhotoProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("profile_photo",)
        