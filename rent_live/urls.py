from django.urls import path
from rent_live import views

app_name = 'rent_live'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('about/contact/', views.ContactView.as_view(), name='contact'),
    path('search/', views.Search.as_view(), name='search'),
    path('search/results/', views.SearchResult.as_view(), name='searchresult'),
    path('city/<cityname>/', views.City.as_view(), name='city'),
    path('rentalproperty/', views.Rental_Property.as_view(), name='rentalproperty'),
    path('rentalproperty/<propertyname>/', views.Property.as_view(), name='property'),
    path('lettingagents/', views.LettingAgents.as_view, name='lettingagents'),
    path('lettingagents/<agentname>/', views.LettingAgent.as_view(), name='agent'),
    path('lettingagents/<agentname>/comments/', views.LAComments.as_view(), name='LAComments'),
    path('lettingagents/<agentname>/properties/', views.LAProperties.as_view(), name='LAProperties'),
    path('register/', views.Register.as_view(), name='register'),
    path('login/', views.LogIn.as_view(), name='login'),
    path('<username>/', views.UserPage.as_view(), name='userpage'),
    path('<username>/messages/', views.UserMessages.as_view(), name='messages'),
    path('<username>/comments/', views.UserComments.as_view(), name='usercomments'),
    path('<username>/rentals/', views.UserRentals.as_view(), name='userrentals'),
]