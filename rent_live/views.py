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

class SearchView(View):
    def get(self, request):
        return HttpResponse("This is the search page, where you will be able to search for properties")

class SearchResultView(View):
    def get(self, request):
        return HttpResponse("This is the search result page, which will show the search results for each search.")

class CityView(View):
    def get(self, request):
        return HttpResponse("This is the City page, will the information on the city's letting agents and properties.")

class Rental_PropertyView(View):
    def get(self, request):
        return HttpResponse("This is the page containing different rental properties")

class PropertyView(View):
    def get(self, request):
        return HttpResponse("This is the page for a specific property")

class LettingAgentsView(View):
    def get(self, request):
        return HttpResponse("This is the page detailing different letting agents")

class LettingAgentView(View):
    def get(self, request):
        return HttpResponse("This is the page for a specific letting agent")

class LACommentsView(View):
    def get(self, request):
        return HttpResponse("This is the page detailing the comments for letting agent")

class LAPropertiesView(View):
    def get(self, request):
        return HttpResponse("This is the page for seeing specific rental properties offered by a letting agent")

class RegisterView(View):
    def get(self, request):
        return HttpResponse("This page will let you register a new account")

class LogInView(View):
    def get(self, request):
        return HttpResponse("This page will let you log in")

class UserPageView(View):
    def get(self, request):
        return HttpResponse("This page will display the specific user's page and details")

class UserMessagesView(View):
    def get(self, request):
        return HttpResponse("This page will show the messages for the user")

class UserCommentsView(View):
    def get(self, request):
        return HttpResponse("This page will show the comments for a user")
    
class UserRentalsView(View):
    def get(self, request):
        return HttpResponse("This page will show the previously rented properties for a user.")