from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from . import forms
from . import models


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


class EditInfo(View):
    template_name = "authentication/authentication_modify.html"
    

    
    def get(self, request):
        user = models.User.objects.get(username=request.user)
        form_edit_info = forms.EditInfoForm(instance=user)
        form_edit_photo = forms.EditPhotoProfileForm()
        
        context = {
            "form_edit_info": form_edit_info,
            "form_edit_photo": form_edit_photo
        }
        return render(request, self.template_name, context=context)
       
    #@login_required 
    def post(self, request):
        user = models.User.objects.get(username=request.user)
        form_edit_info = forms.EditInfoForm(request.POST, instance=user)    
            
        if form_edit_info.is_valid():
            print("oui oui ouio uo")
            form_edit_info.save()
            return redirect("update_profile")

def authentication_logout(request):  
    logout(request)
    return redirect("home")
        

        
        
        
        
        