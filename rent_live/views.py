from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.
class IndexView(View):
    def get(self, request):
        #property_list = Rental_Property.objects.order_by('-likes')[:3]
        #lettingagent_list = LettingAgent.objects.order_by('-qualityRating')[:3]

        #context_dict = {}
        #context_dict['properties'] = property_list
        #context_dict['lettingAgents'] = lettingagent_list

        #response = render(request, 'rentlive/index.html', context=context_dict)

        return HttpResponse("This is the Index Page")
       