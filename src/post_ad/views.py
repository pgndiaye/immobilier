from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import FormPostAd

class PostAdFormPage(View):
    template_name = "post_ad/post_ad_post.html"
    class_form = FormPostAd
    
    def get(self, request):
        form = self.class_form()
        return render(request, self.template_name, context={"form": form})
    
    def post(self, request):
        data = {
            "city": request.POST.get("city"),
            "house": request.POST.get("house"),
            "title_ad": request.POST.get("title_ad"),
            "description_ad": request.POST.get("description_ad"),
            "user": request.user,
            "price_ad": request.POST.get("price_ad"),
        }
        form = self.class_form(data, request.FILES)        
        

        if form.is_valid():
            photo = form.save(commit=False)
            photo.uploader = request.user
            photo.save()
            return redirect("home")
        return render(request, self.template_name, context={"form": form})
