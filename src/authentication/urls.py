from django.urls import path
from .views import authentication_signup

urlpatterns = [
    path("", authentication_signup),
]