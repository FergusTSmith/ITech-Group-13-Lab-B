from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from rent_live.models import Category, LettingAgent, City, Rental_Property, User, Comment, UserProfile
from rent_live.forms import UserForm, UserProfileForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import logout


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
        response = render(request, 'rent_live/about.html', context={})
        return response

class ContactView(View):
    def get(self, request):
        response = render(request, 'rent_live/contact.html', context={})
        return response

class SearchView(View):
    def get(self, request):
        response = render(request, 'rent_live/search.html', context={})
        return response

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
        registered = False
        user_form = UserForm()
        profile_form = UserProfileForm()
        
        response = render(request, 'rent_live/register.html', context={'user_form': user_form, 'profile_form': profile_form, 'registered': registered})
        return response
    
    def post(self, request):
        registered = False
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILE['picture']

            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)

        response = render(request, 'rent_live/register.html', context={'user_form': user_form, 'profile_form':profile_form,'registered':registered})
        return response


class LogInView(View):
    def get(self, request):
        response = render(request, 'rent_live/login.html')
        return response

    def post(self, request):
        user = request.POST.get('username')
        passw = request.POST.get('password')

        user = authenticate(username=user, password=passw)

        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse('rent_live:index'))
            else:
                return HttpResponse("Your account has been disabled")
        else:
            print("Login Details not recognized for: {username}, {password}")
            return HttpResponse("Error: Please reenter your details and ensure that these are correct.")

class LogOutView(View):
    @method_decorator(login_required)
    def get(self, request):
        logout(request)
        response = redirect(reverse('rent_live:index'))
        return response

class UserPageView(View):
    def get_user_details(self, username):
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return None
        
        user_profile = UserProfile.objects.get_or_create(user=user)[0]
        form = UserProfileForm({'accessibleUser': user_profile.accessibleUser,'isAgent': user_profile.isAgent,'profilePic': user_profile.profilePic})

        return (user, user_profile, form)
    
    @method_decorator(login_required)
    def get(self, request, username):
        try:
            (user, user_profile, form) = self.get_user_details(username)
        except TypeError:
            return redirect(reverse('rent_live:index'))
        
        context_dict = {'user_profile': user_profile,'selected_user': user,'form': form}
        return render(request, 'rent_live/profile.html', context_dict)

    @method_decorator(login_required)
    def post(self, request, username):
        try:
            (user, user_profile, form) = self.get_user_details(username)
        except TypeError:
            return redirect(reverse('rent_live:index'))
        
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)

        if form.is_valid():
            form.save(commit=True)
            return redirect(reverse('rent_live:profile',kwargs={'username': username}))
        else:
            print(form.errors)
        
        context_dict = {'user_profile': user_profile,'selected_user': user,'form': form}
        
        return render(request, 'rango/profile.html', context_dict)

class UserMessagesView(View):
    def get(self, request):
        return HttpResponse("This page will show the messages for the user")

class UserCommentsView(View):
    def get(self, request):
        return HttpResponse("This page will show the comments for a user")
    
class UserRentalsView(View):
    def get(self, request):
        return HttpResponse("This page will show the previously rented properties for a user.")