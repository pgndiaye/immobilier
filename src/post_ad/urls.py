from django.urls import path
from .views import PostAdFormPage, post_ad_post_list, post_ad_post_detailed, PostAdUpdate, PostAdDelete

urlpatterns = [
    path("add/", PostAdFormPage.as_view(), name="poster_add"),
    path("list/", post_ad_post_list, name="poster_list"),
    path("list/<int:number_ad>/detailed/", post_ad_post_detailed, name="poster_detailed"),
    path("list/<int:number_ad>/update/", PostAdUpdate.as_view(), name="poster_update"),
    path("list/<int:number_ad>/delete/", PostAdDelete.as_view(), name="poster_delete"),
]