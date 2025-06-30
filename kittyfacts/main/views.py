from django.shortcuts import render , HttpResponse
from .models import CatFact

# Create your views here.
def home(request):
    randomFact = CatFact.objects.order_by('?').first()
    return HttpResponse(randomFact)

def about(request):
    return HttpResponse('About KittyFacts')

def myCatStory(request):
    return HttpResponse('Story of my cat')