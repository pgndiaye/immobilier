from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.views.generic import View
from . import forms

# Cette class va permetre de gérer l'authentification d'un utilisateur
class LoginPage(View):
    template_name = "authentication/authentication_login.html"
    form_class = forms.LoginForm
    
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
                return redirect("home")    
        return render(request, self.template_name, context={"form":form})
    
# Cette class va permetre de gérer la crféation de compte d'un utilisateur
class SingupPage(View):
    class_form = forms.SingupForm
    template_name = "authentication/authentication_singup.html"

    def get(self, request):
        form = self.class_form()
        return render(request, self.template_name, context={"form": form})
    
    def post(self, request):    
        form = self.class_form(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
        return render(request, self.template_name, context={"form": form})

            
        

def authentication_logout(request):  
    logout(request)
    return redirect("home")
        
        
        
        
        
        
        
        