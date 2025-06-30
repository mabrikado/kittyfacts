from django.test import TestCase
from .models import CatFact
from django.urls import reverse
from .views import GetCatFacts
from rest_framework.test import APIRequestFactory
from rest_framework import status


# Create your tests here.
class TestAPI(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = GetCatFacts.as_view()
        self.fact = CatFact.objects.create(
            title="I love cats",
            description = "I love cats and wish to have more"
        )
        self.fact.save()
        self.fact2 = CatFact.objects.create(
            title="Cats are great",
            description="Cats can be very affectionate."
        )

        
    def test_fact_view_success(self):
        response = self.client.get(reverse('fact', args=[self.fact.title]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
        self.assertContains(response, self.fact.title)
        self.assertContains(response, self.fact.description)

    def test_fact_view_not_found(self):
        response = self.client.get(reverse('fact', args=['Nonexistent Cat Fact']))
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.content.decode(), "Such Cat Fact not found")
    
    def test_get_cat_facts_success(self):
        request = self.factory.get('fact', {'title': 'love'})
        response = self.view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], self.fact.title)
        self.assertEqual(response.data[0]['description'], self.fact.description)

    def test_get_cat_facts_not_found(self):
        request = self.factory.get('fact', {'title': 'nonexistent'})
        response = self.view(request)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data, "No cat facts found with the specified title")

    def test_get_cat_facts_no_title(self):
        request = self.factory.get('fact')
        response = self.view(request)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, "No title provided")