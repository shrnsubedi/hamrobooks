from django.test import SimpleTestCase 
from django.urls import reverse

class HomepageTests(SimpleTestCase):
    def test_homepage_status_code(self):
        response = self.client.get(reverse("home")) 
        self.assertEqual(response.status_code, 200)
    
    def test_homepage_template(self): # new
        response = self.client.get(reverse("home")) 
        self.assertTemplateUsed(response, 'home.html')