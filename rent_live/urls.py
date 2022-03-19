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
    #path('rentalproperty/', views.Rental_PropertyView.as_view(), name='rentalproperty'),
    path('rentalproperty/<slug:rental_property_name_slug>/', views.Rental_PropertyView.as_view(), name='property'),

    path('rating/', views.rating.as_view(), name='rating'),

    #path('lettingagents/', views.LettingAgentsView.as_view, name='lettingagents'),
    path('lettingagents/<slug:letting_agent_name_slug>/', views.LettingAgentView.as_view(), name='agent'),
    path('lettingagents/<agentname>/comments/', views.LACommentsView.as_view(), name='LAComments'),
    path('lettingagents/<agentname>/properties/', views.LAPropertiesView.as_view(), name='LAProperties'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('register/lettingagent/', views.LettingAgentRegisterView.as_view(), name='lettingagentregister'),
    path('login/', views.LogInView.as_view(), name='login'),
    path('logout/', views.LogOutView.as_view(), name='logout'),
    path('profile/<username>/', views.UserPageView.as_view(), name='profile'),
    path('<username>/messages/', views.UserMessagesView.as_view(), name='messages'),
    path('<username>/comments/', views.UserCommentsView.as_view(), name='usercomments'),
    path('<username>/rentals/', views.UserRentalsView.as_view(), name='userrentals'),
    path('addProperty/', views.AddRentalView.as_view(), name='addProperty'),
    path('profile/edit/<username>', views.EditProfileView.as_view(), name='editprofile'),
    path('profile/edit/password/', views.ChangePasswordView.as_view(), name='changepassword'),
    path('profile/delete/<username>/', views.DeleteUserView.as_view(), name='delete'),
    path('landlords/', views.LandLordView.as_view(), name='landlords'),
    path('agencies/', views.AgencyView.as_view(), name='agencies'),
    path('agents/', views.AgentView.as_view(), name='agents'),
    path('search/results/', views.SearchResultView.as_view(), name='searchresults'),
    path('follow_property/', views.FollowPropertyView.as_view(), name='followproperty'),
    path('suggestion/', views.CitySuggestionView.as_view(), name='suggestion'),
    path('follows/', views.ProfileFollowsView.as_view(), name='follows'),
    path('message/', views.SendMessageView.as_view(), name='message'),
    path('sent/', views.MessageSentView.as_view(), name='sent'),
    path('showmessages/', views.ShowMessagesView.as_view(), name='showmessages')
]