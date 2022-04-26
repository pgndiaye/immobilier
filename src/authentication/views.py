from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.views.generic import View
from . import forms


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


def authentication_logout(request):  
    logout(request)
    return redirect("home")
        
        
        
        
        
        
        
        