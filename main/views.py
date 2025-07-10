from django.shortcuts import render, HttpResponse
from rest_framework.views import APIView
from .models import CatFact
from rest_framework.response import Response
from rest_framework import status
from .serializer import CatFactSerializer

# Create your views here.
def home(request):
    randomFact = CatFact.objects.order_by('?').first()
    return render(request, "home.html", {
        "title": "KittyFacts",
        "fact_title": randomFact.title,
        "fact_description": randomFact.description
    })

def fact(request, title:str):
    try:
        randomFact = CatFact.objects.get(title=title)
    except CatFact.DoesNotExist:
        return HttpResponse("Such Cat Fact not found", status=404)
    return render(request, "home.html", {
        "title": "KittyFacts",
        "fact_title": randomFact.title,
        "fact_description": randomFact.description
    })

def about(request):
    return render(request, "about.html", {"title": "About KittyFacts"})

def _404(request):
    return render(request, "home.html", {
        "title":"Not Found",
        "fact_title":"Ooops!!",
        "fact_description":"It seems the page you are looking for does not exist"
    })

class GetCatFacts(APIView):
    def get(self, request):
        title = request.GET.get("title")
        if title:
            cat_facts = CatFact.objects.filter(title__icontains=title)
            if cat_facts.exists():
                serializer = CatFactSerializer(cat_facts, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response("No cat facts found with the specified title", status=status.HTTP_404_NOT_FOUND)
        else:
            return Response("No title provided", status=status.HTTP_400_BAD_REQUEST)


