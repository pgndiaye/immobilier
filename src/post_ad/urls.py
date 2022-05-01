from django.urls import path
from .views import PostAdFormPage

urlpatterns = [
    path("add/", PostAdFormPage.as_view(), name="poster_ad")
]