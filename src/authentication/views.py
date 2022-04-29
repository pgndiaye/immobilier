from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from .forms import EditInfoForm, LoginForm, SingupForm
from . import models

# Cette class va permetre de gérer l'authentification d'un utilisateur
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
                return redirect("home")   
        return render(request, self.template_name, context={"form":form})
    
# Cette class va permetre de gérer la création de compte d'un utilisateur
class SingupPage(View):
    class_form = SingupForm
    template_name = "authentication/authentication_singup.html"

    def get(self, request):
        form = self.class_form()
        user = models.User.objects.get(username=request.user)
        print(user)
        return render(request, self.template_name, context={"form": form, "user": user})
    
    def post(self, request):    
        form = self.class_form(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
        return render(request, self.template_name, context={"form": form})

            
        

class EditInfo(View):
    template_name = "authentication/authentication_modify.html"
    class_model = EditInfoForm
    
    def get(self, request):
        form = self.class_model(instance=request.user)
        return render(request, self.template_name, context={"form": form})
       
    def post(self, request):
        user = models.User.objects.get(username=request.user)
        print(user.photo_profile)
        form = self.class_model(request.POST, request.FILES, instance=user)

        if form.is_valid():
            photo = form.save(commit=False)
            photo.uploader = request.user
            photo.save()
            return redirect("update_profile")

def authentication_logout(request):  
    logout(request)
    return redirect("home")
        

        
        
        
        
        