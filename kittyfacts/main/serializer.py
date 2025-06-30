from rest_framework import serializers
from .models import CatFact

class CatFactSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CatFact
        fields = ['title' , 'description']