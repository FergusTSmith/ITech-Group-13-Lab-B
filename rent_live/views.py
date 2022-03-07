from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from rent_live.models import Category, LettingAgent, City, Rental_Property, User, Comment

# Create your views here.
class IndexView(View):
    def get(self, request):
        property_list = Rental_Property.objects.order_by('-followers')[:3]
        lettingagent_list = LettingAgent.objects.order_by('-qualityRating')[:3]

        context_dict = {}
        context_dict['properties'] = property_list
        context_dict['lettingAgents'] = lettingagent_list

        response = render(request, 'rent_live/index.html', context=context_dict)

        return response
       
class AboutView(View):
    def get(self, request):
        return HttpResponse("This is the About Page <a href='/rentlive/'>Index</a>.")

class ContactView(View):
    def get(self, request):
        return HttpResponse("This is the page for contacting us")

class Search(View):
    def get(self, request):
        return HttpResponse("This is the search page, where you will be able to search for properties")

class SearchResult(View):
    def get(self, request):
        return HttpResponse("This is the search result page, which will show the search results for each search.")

class City(View):
    def get(self, request):
        return HttpResponse("This is the City page, will the information on the city's letting agents and properties.")

class Rental_Property(View):
    def get(self, request):
        return HttpResponse("This is the page containing different rental properties")

class Property(View):
    def get(self, request):
        return HttpResponse("This is the page for a specific property")

class LettingAgents(View):
    def get(self, request):
        return HttpResponse("This is the page detailing different letting agents")

class LettingAgent(View):
    def get(self, request):
        return HttpResponse("This is the page for a specific letting agent")

class LAComments(View):
    def get(self, request):
        return HttpResponse("This is the page detailing the comments for letting agent")

class LAProperties(View):
    def get(self, request):
        return HttpResponse("This is the page for seeing specific rental properties offered by a letting agent")

class Register(View):
    def get(self, request):
        return HttpResponse("This page will let you register a new account")

class LogIn(View):
    def get(self, request):
        return HttpResponse("This page will let you log in")

class UserPage(View):
    def get(self, request):
        return HttpResponse("This page will display the specific user's page and details")

class UserMessages(View):
    def get(self, request):
        return HttpResponse("This page will show the messages for the user")

class UserComments(View):
    def get(self, request):
        return HttpResponse("This page will show the comments for a user")
    
class UserRentals(View):
    def get(self, request):
        return HttpResponse("This page will show the previously rented properties for a user.")