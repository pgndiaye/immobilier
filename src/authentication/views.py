from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import EditInfoForm, LoginForm, SingupForm
from . import models

class LoginPage(View):
    template_name = "authentication/authentication_login.html"
    form_class = LoginForm
    
    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, context={"form":form})

    def post(self, request):    
        form = self.form_class(request.POST)
        
        if form.is_valid():
            user = authenticate(
                password=form.cleaned_data["password"],
                username=form.cleaned_data["username"],
            )
        
            if user != None:
                login(request, user)
                messages.add_message(request, messages.SUCCESS, "Vous être connecté")
                return redirect("poster_list")   
        
        messages.add_message(request, messages.SUCCESS, "Veuillez vérifier les informations que vous avez entrer")
        return render(request, self.template_name, context={"form":form})
    
class SingupPage(View):
    class_form = SingupForm
    template_name = "authentication/authentication_singup.html"

    def get(self, request):
        form = self.class_form()
        return render(request, self.template_name, context={"form": form})
    
    def post(self, request):    
        form = self.class_form(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.add_message(request, messages.SUCCESS, "Vous être connecté")
            return redirect("poster_list")
        
        messages.add_message(request, messages.INFO, "Veuillez vérifier les informations que vous avez entrer")
        return render(request, self.template_name, context={"form": form})

class EditInfo(View):
    template_name = "authentication/authentication_modify.html"
    class_model = EditInfoForm
    
    def get(self, request):
        form = self.class_model(instance=request.user)
        return render(request, self.template_name, context={"form": form})
       
    def post(self, request):
        user = models.User.objects.get(username=request.user)
        form = self.class_model(request.POST, request.FILES, instance=user)

        if form.is_valid():
            photo = form.save(commit=False)
            photo.uploader = request.user
            photo.save()
            messages.add_message(request, messages.SUCCESS, "Vos informations on été mise ajour avec succès")
            return redirect("update_profile")
        
        messages.add_message(request, messages.INFO, "Une erreur c'est produite lors de la modifications de vos information")
        return render(request, self.template_name, context={"form": form})

class DeleteAccount(View):
    template_name = "authentication/authentiction_detele_account.html"
    model_class = models.User
    
    def get(self, request):
        return render(request, self.template_name)
    
    def post(self, request):
        user_delete = self.model_class.objects.get(username=request.user)
        user_delete.delete()
        messages.add_message(request, messages.SUCCESS, "Vôtre compte a été supprimer avec succès")
        return redirect("poster_list")
        

def authentication_logout(request):  
    logout(request)
    messages.add_message(request, messages.SUCCESS, "Vous venez de vous déconnecter")
    return redirect("poster_list")
        

        
        
        