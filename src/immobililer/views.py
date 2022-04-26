from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def immobilier_home(request):
    return render(request, "immobilier/immobilier_home.html") 