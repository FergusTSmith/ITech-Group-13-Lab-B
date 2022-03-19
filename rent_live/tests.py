from django.test import TestCase
from rent_live.models import *
from django.urls import reverse
# Create your tests here.

class CategoryMethodTests(TestCase):
    def test_category(self):
        category = Category(name='test', description='abcd')
        category.save()
        self.assertEqual((category.name != 'null'), True)  
        self.assertEqual((category.description != 'null'), True)   

class RentalPropertyTests(TestCase):
    def test_rental_property(self):
        rental_property = Rental_Property(name='test', address='abcd', description='asdc', price='100', size='200', followers='200', state='True')
        rental_property.save()
        
class LettingAgentTests(TestCase):
    def test_letting_agent(self):
        letting_agent = LettingAgent(name='test', description='abcd', phone='123456', email='123@123.com')
        letting_agent.save()

class IndexViewTests(TestCase):
    def test_index_view_with_no_categories(self):
        response = self.client.get(reverse('rent_live:index'))
        self.assertEqual(response.status_code, 200)
