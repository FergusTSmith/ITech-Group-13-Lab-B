from django.urls import path
from rent_live import views

app_name = 'rent_live'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('about/contact/', views.ContactView.as_view(), name='contact'),
    path('search/', views.SearchView.as_view(), name='search'),
    path('search/results/', views.SearchResultView.as_view(), name='searchresult'),
    path('city/<cityname>/', views.CityView.as_view(), name='city'),
    path('rentalproperty/', views.Rental_PropertyView.as_view(), name='rentalproperty'),
    path('rentalproperty/<propertyname>/', views.PropertyView.as_view(), name='property'),
    path('lettingagents/', views.LettingAgentsView.as_view, name='lettingagents'),
    path('lettingagents/<agentname>/', views.LettingAgentView.as_view(), name='agent'),
    path('lettingagents/<agentname>/comments/', views.LACommentsView.as_view(), name='LAComments'),
    path('lettingagents/<agentname>/properties/', views.LAPropertiesView.as_view(), name='LAProperties'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LogInView.as_view(), name='login'),
    path('<username>/', views.UserPageView.as_view(), name='userpage'),
    path('<username>/messages/', views.UserMessagesView.as_view(), name='messages'),
    path('<username>/comments/', views.UserCommentsView.as_view(), name='usercomments'),
    path('<username>/rentals/', views.UserRentalsView.as_view(), name='userrentals'),
]