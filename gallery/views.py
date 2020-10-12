from django.shortcuts import render
from django.http import HttpResponse
from .models import Image,Category,Location

# Create your views here.

#def welcome(request):
     #all_images = Image.objects.all()
    #category_results = Category.objects.all()
    #location_results = Location.objects.all()
    #return HttpResponse('Welcome to the Lucys-Gallery')
    #return render(request,'index.html', {'all_images':all_images,'location_results':location_results,'category_results':category_results})

def index(request):
        return render(request, 'index.html')

def gallery(request):
    images = Image.objects.all()
    categories = Category.objects.all()
    location = Location.objects.all()
    return render(request, 'gallery.html', locals())

def search_by_image_category(request):
    categories = Category.objects.all()
    locations = Location.objects.all()
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_image_category(search_term)
        message = f"{search_term}"

        return render(request, 'category.html', {"message": message, "images": searched_images,"categories":categories,
    "locations":locations})
    else:
        message = "You haven't searched for any term"
        return render(request, 'category.html', {"message": message})
