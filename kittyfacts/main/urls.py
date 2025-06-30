from django.urls import path
from .views import *
from django.urls import path
from .views import home, about, fact

urlpatterns = [
    path('', home, name='home'),
    path('fact/<str:title>', fact, name='fact'),
    path('fact', GetCatFacts.as_view(), name='factQuery'),
    path('about/', about, name='about'),

]
