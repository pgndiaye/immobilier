from django.contrib import admin
from .models import City, House, PostAd, District

# Register your models here.
admin.site.register(City)
admin.site.register(House)
admin.site.register(PostAd)
admin.site.register(District)
