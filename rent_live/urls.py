from django.urls import path
from rent_live import views

app_name = 'rent_live'

urlpatterns = [
    # Visitable Pages
    path('', views.IndexView.as_view(), name='index'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('serachData/', views.serachData.as_view(), name='serachData'),
    path('about/contact/', views.ContactView.as_view(), name='contact'),
    path('search/', views.SearchView.as_view(), name='search'),
    path('search/results/', views.SearchResultView.as_view(), name='searchresult'), # This is for Rental Property search results.
    path('search/results1/', views.SearchResultView1.as_view(), name='searchresult1'), # This is for letting agent search results
    path('search/propertyresult/', views.PropertySearchResult.as_view(), name='propertysearch'),
    path('city/<cityname>/', views.CityView.as_view(), name='city'),
    path('rentalproperty/<slug:rental_property_name_slug>/', views.Rental_PropertyView.as_view(), name='property'),
    path('lettingagents/<slug:letting_agent_name_slug>/', views.LettingAgentView.as_view(), name='agent'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('register/lettingagent/', views.LettingAgentRegisterView.as_view(), name='lettingagentregister'),
    path('login/', views.LogInView.as_view(), name='login'),
    path('logout/', views.LogOutView.as_view(), name='logout'),
    path('profile/<username>/', views.UserPageView.as_view(), name='profile'),
    path('addProperty/', views.AddRentalView.as_view(), name='addProperty'),
    path('profile/edit/<username>', views.EditProfileView.as_view(), name='editprofile'),
    path('profile/edit/password/', views.ChangePasswordView.as_view(), name='changepassword'),
    path('profile/delete/<username>/', views.DeleteUserView.as_view(), name='delete'),
    path('landlords/', views.LandLordView.as_view(), name='landlords'),
    path('agencies/', views.AgencyView.as_view(), name='agencies'),
    path('agents/', views.AgentView.as_view(), name='agents'),
    path('search/results/', views.SearchResultView.as_view(), name='searchresults'),
    
    # The below URL paths are exclusively used by AJAX functionality.
    path('follow_property/', views.FollowPropertyView.as_view(), name='followproperty'),
    path('suggestion/', views.CitySuggestionView.as_view(), name='suggestion'),
    path('follows/', views.ProfileFollowsView.as_view(), name='follows'),
    path('message/', views.SendMessageView.as_view(), name='message'),
    path('sent/', views.MessageSentView.as_view(), name='sent'),
    path('showmessages/', views.ShowMessagesView.as_view(), name='showmessages'),
    path('addcomment/', views.LeaveCommentView.as_view(), name='addcomment'),
    path('showcomments/', views.ShowUserCommentsView.as_view(), name='showcomment'),
    path('likecomment/', views.LikeCommentView.as_view(), name='likecomment'),
    path('agentcomment/', views.AgentCommentView.as_view(), name='agentcomment'),
    path('likeagentcomment/', views.LikeAgentComment.as_view(), name='likeagentcomment')
]