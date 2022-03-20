from django.test import TestCase
from rent_live.models import *
from django.urls import reverse
from django import template


# Create your tests here.

# Test model
class CategoryMethodTests(TestCase):
    def test_category(self):
        category = Category(name='test', description='abcd')
        category.save()
        self.assertEqual((category.name != 'null'), True)  
        self.assertEqual((category.description != 'null'), True)   

class RentalPropertyTests(TestCase):
    def test_rental_property(self):
        rental_property = Rental_Property(name='test', address='abcd', description='asdc', price=100, size=200, followers=200, state='True')
        rental_property.save()
        self.assertEqual((rental_property.name != 'null'), True)
        self.assertEqual((rental_property.address != 'null'), True)
        self.assertEqual((rental_property.description != 'null'), True)
        self.assertEqual((rental_property.price >= 0), True)
        self.assertEqual((rental_property.size >= 0), True)
        self.assertEqual((rental_property.followers >= 0), True)
        
class LettingAgentTests(TestCase):
    def test_letting_agent(self):
        letting_agent = LettingAgent(name='test', description='abcd', phone='123456', email='123@123.com')
        letting_agent.save()
        self.assertEqual((letting_agent.name != 'null'), True)
        self.assertEqual((letting_agent.description != 'null'), True)
        self.assertEqual((letting_agent.phone != 'null'), True)
        self.assertEqual((letting_agent.email != 'null'), True)
        
        
# Test view
class IndexViewTests(TestCase):
    def test_index_view(self):
        response = self.client.get(reverse('rent_live:index'))
        self.assertEqual(response.status_code, 200)
    
    def test_visit_a_nonexistent_category(self):
        url = reverse('rent_live:category')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

