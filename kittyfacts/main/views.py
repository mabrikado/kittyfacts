from django.shortcuts import render , HttpResponse
from .models import CatFact

# Create your views here.
def home(request):
    randomFact = CatFact.objects.order_by('?').first()
    return render(request, "home.html", {"title":"KittyFacts" , "fact_title":randomFact.title , "fact_description":randomFact.description})

def about(request):
    return render(request, "about.html", {"title":"About KittyFacts"})

def myCatStory(request):
    return render(request, "story.html", {"title":"Story of Kitty"})